from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton

from guinew import Ui_MainWindow
from components.fsm import LogicalSquareFSM
from components import graph_gen as gg


class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fsm = LogicalSquareFSM()
        self.parent_id = 0
        self.expanded_states = []
        self.class_code = None
        self.transition_code = None
        self.qt_code = None
        self.sml_code = None
        self.expanded = False

        self.ui.inputA.returnPressed.connect(lambda: self.move_focus(self.ui.inputE))
        self.ui.inputE.returnPressed.connect(lambda: self.move_focus(self.ui.inputI))
        self.ui.inputI.returnPressed.connect(lambda: self.move_focus(self.ui.inputO))
        self.ui.inputO.returnPressed.connect(self.add_square)

        self.ui.add_square_button.clicked.connect(self.add_square)
        self.ui.name_button.clicked.connect(self.show_name_widget)
        self.ui.namebox.currentTextChanged.connect(self.update_assertion)
        self.ui.change_name_button.clicked.connect(self.add_name)

        self.ui.ifinput.returnPressed.connect(self.add_transition)
        self.ui.frombox.currentIndexChanged.connect(self.update_state_box)

        self.ui.tree_button.clicked.connect(self.show_tree_widget)
        self.ui.sm_button.clicked.connect(self.show_sm_widget)
        self.ui.assertions_button.clicked.connect(self.show_assertions_widget)
        self.ui.expand_button.clicked.connect(self.show_square_widget)
        self.ui.gen_button.clicked.connect(self.show_code_widget)

        self.gen_buttons = [self.ui.class_button, self.ui.trans_button, self.ui.qt_button, self.ui.sml_button]
        for button in self.gen_buttons:
            button.clicked.connect(self.show_sm_code)

        self.ui.reset_button.clicked.connect(self.reset_action)

    def move_focus(self, next_widget):
        next_widget.setFocus()

    def show_tree_widget(self):
        for widget in self.ui.main_widget.children():
            if isinstance(widget, QWidget) and widget != self.ui.tree:
                widget.setVisible(False)
        self.ui.tree.setVisible(True)
        self.display_tree_graph()

    def show_name_widget(self):
        for widget in self.ui.main_widget.children():
            if isinstance(widget, QWidget) and widget != self.ui.names:
                widget.setVisible(False)
        self.ui.names.setVisible(True)
        all_state_ids = [state_id for state_id in self.fsm.span_tree.keys()
                         if state_id not in self.expanded_states]
        self.fill_states_box(all_state_ids, self.ui.namebox)

    def update_assertion(self):
        state_id = self.ui.namebox.currentText()
        node = self.fsm.span_tree[state_id]
        state = node["state"]
        assertion = state.assert_state()
        self.ui.assertlabel.setText(f"State Assertion: {assertion}")

    def show_sm_widget(self):
        for widget in self.ui.main_widget.children():
            if isinstance(widget, QWidget) and widget != self.ui.transitions:
                widget.setVisible(False)
        self.ui.transitions.setVisible(True)
        self.ui.frombox.clear()
        for state_id in self.fsm.span_tree.keys():
            if state_id not in self.expanded_states:
                self.ui.frombox.addItem(str(state_id))
        all_states = [state for state in self.fsm.span_tree.keys() if state != 0]
        transitions = [(t[0], t[1], t[2]) for t in self.fsm.transitions]
        gg.draw_state_machine(self.ui.sm_plot, transitions, all_states)

    def show_assertions_widget(self):
        for widget in self.ui.main_widget.children():
            if isinstance(widget, QWidget) and widget != self.ui.assertions:
                widget.setVisible(False)
        self.ui.assertions.setVisible(True)
        tree_str = self.fsm.display_tree()
        self.ui.assert_tree.clear()
        self.ui.assert_tree.append(tree_str)

    def show_square_widget(self):
        self.fill_states_box(self.fsm.latest_states, self.ui.expandbox)
        for widget in self.ui.main_widget.children():
            if isinstance(widget, QWidget) and widget != self.ui.square:
                widget.setVisible(False)
        self.ui.square.setVisible(True)

    def show_solver_widget(self):
        return

    def show_code_widget(self):
        for widget in self.ui.main_widget.children():
            if isinstance(widget, QWidget) and widget != self.ui.code:
                widget.setVisible(False)
        self.ui.code.setVisible(True)
        self.ui.smcode.setText("Choose code generation method from options below.\n"
                               "Your state machine code will appear here...")

        for button in self.gen_buttons:
            button.setEnabled(True)

    def display_tree_graph(self):
        """
        Rysuje drzewo stanów w widżecie PyQtGraph.
        """
        edges = self.fsm.get_tree_edges()
        node_names = self.fsm.get_state_names()
        gg.draw_tree(self.ui.tree_plot, edges, node_names=node_names)

    def add_square(self):
        a = self.ui.inputA.text() or "true"
        e = self.ui.inputE.text() or "true"
        i = self.ui.inputI.text() or "true"
        o = self.ui.inputO.text() or "true"

        if a == o:
            QtWidgets.QMessageBox.warning(
                self,
                "Data error",
                "Fields 'A' and 'O' cannot have the same value."
            )
            return

        if e == i:
            QtWidgets.QMessageBox.warning(
                self,
                "Data error",
                "Fields 'E' and 'I' cannot have the same value."
            )
            return

        if self.ui.expandbox.isVisible():
            self.parent_id = self.ui.expandbox.currentText()

        self.fsm.add_square(a, e, i, o, self.parent_id)
        self.expanded_states.append(self.parent_id)
        self.remove_transitions_for_expanded_state(self.parent_id)

        if len(self.fsm.latest_states) > 0:
            for input in [self.ui.inputA, self.ui.inputE, self.ui.inputI, self.ui.inputO]:
                input.clear()

            self.show_tree_widget()
            self.ui.buttonwidget.setEnabled(True)
            if not self.expanded:
                self.expanded = True
                self.create_expand_widget()
        else:
            return

    def create_expand_widget(self):
        self.ui.expandbox.setVisible(True)
        for widget in [self.ui.add_square_button, self.ui.inputA, self.ui.inputE, self.ui.inputI,
                       self.ui.inputO, self.ui.labelA, self.ui.labelE, self.ui.labelI, self.ui.labelO]:
            geometry = widget.geometry()
            widget.setGeometry(geometry.x(), geometry.y() + 50, geometry.width(), geometry.height())
        self.ui.addsquare.setText("Expand States")
        self.ui.addlabel.setText("Choose a state to expand from box below and "
                                 "replace it with a new logical square.")

    def fill_states_box(self, item_list, combo_box):
        combo_box.clear()
        for item in item_list:
            combo_box.addItem(str(item))

    def add_name(self):
        state_id = self.ui.namebox.currentText()
        state_name = self.ui.name_input.text()
        self.fsm.assign_name_to_state(state_id, state_name)
        self.ui.name_input.clear()
        self.show_tree_widget()

    def update_state_box(self):
        current_state = self.ui.frombox.currentText()

        all_states = [state for state in self.fsm.span_tree.keys() if state not in self.expanded_states]
        existing_transitions = self.fsm.state_transitions_map.get(current_state, {}).values()

        available_states = [state for state in all_states
                            if state not in existing_transitions and state]

        self.ui.tobox.clear()
        for state in available_states:
            self.ui.tobox.addItem(str(state))

    def add_transition(self):
        event = self.ui.ifinput.text()

        if not event.strip():
            return

        from_state = self.ui.frombox.currentText()
        to_state = self.ui.tobox.currentText()

        if to_state:
            self.fsm.add_transition(from_state, to_state, event)
            transitions = [(t[0], t[1], t[2]) for t in self.fsm.transitions]
            all_states = [state for state in self.fsm.span_tree.keys()
                          if state not in self.expanded_states]
            gg.draw_state_machine(self.ui.sm_plot, transitions, all_states)

            self.ui.ifinput.clear()
            self.update_state_box()

    def remove_transitions_for_expanded_state(self, state_id):
        self.fsm.transitions = [transition for transition in self.fsm.transitions
                                if transition[0] != state_id and transition[1] != state_id]

    def show_sm_code(self):
        sender = self.sender()

        for button in self.gen_buttons:
            button.setEnabled(True)

        sender.setEnabled(False)
        self.ui.smcode.clear()

        if sender == self.ui.class_button:
            if self.class_code is None:
                self.class_code = self.fsm.generate_class_code()
                with open("gen/sm_class_code.py", "w") as f:
                    f.write(self.class_code)
            self.ui.smcode.append(self.class_code)

        elif sender == self.ui.trans_button:
            if self.transition_code is None:
                self.transition_code = self.fsm.generate_transition_code()
                with open("gen/sm_transitions.py", "w") as f:
                    f.write(self.transition_code)
            self.ui.smcode.append(self.transition_code)

        elif sender == self.ui.qt_button:
            if self.qt_code is None:
                self.qt_code = self.fsm.generate_qt_code()
                with open("gen/sm_qt.py", "w") as f:
                    f.write(self.qt_code)
            self.ui.smcode.append(self.qt_code)

        elif sender == self.ui.sml_button:
            if self.sml_code is None:
                self.fsm.generate_sml()
                with open("gen/sml_sm.py", 'r') as file:
                    code = file.read()
                    self.sml_code = code
            self.ui.smcode.append(self.sml_code)

    def reset_action(self):
        self.close()
        self.__init__()
        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindowController()
    mainWindow.show()
    sys.exit(app.exec_())
