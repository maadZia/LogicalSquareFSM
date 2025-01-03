from PyQt5 import QtWidgets, QtCore
from gui import Ui_MainWindow
from fsm import LogicalSquareFSM


class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fsm = LogicalSquareFSM()
        self.parent_id = 0
        self.expanded_states = []
        self.class_code = None

        self.ui.inputA.returnPressed.connect(lambda: self.move_focus(self.ui.inputE))
        self.ui.inputE.returnPressed.connect(lambda: self.move_focus(self.ui.inputI))
        self.ui.inputI.returnPressed.connect(lambda: self.move_focus(self.ui.inputO))
        self.ui.inputO.returnPressed.connect(self.add_square)

        self.ui.addButton_1.clicked.connect(self.add_square)
        # napisac funkcje dodajaca nazwy dla stanow - ma sie aktualizowac state tree od razu po dodaniu kazdej nazwy
        self.ui.nameinput.returnPressed.connect(self.add_name)
        self.ui.nextButton_1.clicked.connect(self.show_state_widget)

        self.ui.expandButton.clicked.connect(self.expand_state)
        self.ui.nextButton_2.clicked.connect(self.add_transitions)
        self.ui.conditioninput.returnPressed.connect(self.add_transition)

        # zmiana w `fromComboBox` aktualizuje opcje `toComboBox`
        self.ui.frombox.currentIndexChanged.connect(self.update_state_box)

        self.ui.nextButton_3.clicked.connect(self.show_sm_widget)

        self.gen_buttons = [self.ui.genButton_1, self.ui.genButton_2, self.ui.genButton_3, self.ui.genButton_4]
        for button in self.gen_buttons:
            button.clicked.connect(self.show_sm_code)

        self.ui.resetButton.clicked.connect(self.reset_action)


    def move_focus(self, next_widget):
        next_widget.setFocus()

    def add_square(self):
        a = self.ui.inputA.text() or "true"
        e = self.ui.inputE.text() or "true"
        i = self.ui.inputI.text() or "true"
        o = self.ui.inputO.text() or "true"

        self.fsm.add_square(a, e, i, o, self.parent_id)
        self.expanded_states.append(self.parent_id)

        if len(self.fsm.latest_states) > 0:
            self.ui.statetree.clear()
            tree_str = self.fsm.display_tree()

            self.ui.statetree.append(tree_str)

            self.ui.inputA.clear()
            self.ui.inputE.clear()
            self.ui.inputI.clear()
            self.ui.inputO.clear()

            self.ui.squarewidget.setEnabled(False)
            self.ui.namewidget.setEnabled(True)
            self.fill_states_box(self.fsm.latest_states, self.ui.namebox)
        else:
            return

    def fill_states_box(self, item_list, combo_box):
        combo_box.clear()
        for item in item_list:
            combo_box.addItem(str(item))

    def add_name(self):
        state_id = self.ui.namebox.currentText()
        state_name = self.ui.nameinput.text()
        self.fsm.assign_name_to_state(state_id, state_name)
        self.ui.nameinput.clear()
        self.ui.statetree.clear()
        tree_str = self.fsm.display_tree()
        self.ui.statetree.append(tree_str)

    def show_state_widget(self):
        self.ui.squarewidget.setEnabled(True)
        self.ui.namebox.setCurrentText("")
        self.ui.namewidget.setEnabled(False)
        self.ui.addwidget.hide()
        self.ui.statewidget.show()
        self.fill_states_box(self.fsm.latest_states, self.ui.expandbox)

    def expand_state(self):
        self.parent_id = self.ui.expandbox.currentText()
        self.ui.statewidget.hide()
        self.ui.addwidget.show()

    def add_transitions(self):
        self.ui.expandwidget.setEnabled(False)
        self.ui.transwidget.setEnabled(True)

        self.ui.frombox.clear()
        for state_id in self.fsm.span_tree.keys():
            if state_id not in self.expanded_states:
                self.ui.frombox.addItem(str(state_id))

    def update_state_box(self):
        current_state = self.ui.frombox.currentText()

        all_states = [state for state in self.fsm.span_tree.keys() if state not in self.expanded_states]
        existing_transitions = self.fsm.state_transitions_map.get(current_state, {}).values()

        available_states = [state for state in all_states
                            if state not in existing_transitions and state != current_state]

        self.ui.tobox.clear()
        for state in available_states:
            self.ui.tobox.addItem(str(state))

    def add_transition(self):
        event = self.ui.conditioninput.text()

        if not event.strip():
            return

        from_state = self.ui.frombox.currentText()
        to_state = self.ui.tobox.currentText()
        transition_message = self.fsm.add_transition(from_state, to_state, event)

        self.ui.transitions.append(transition_message)
        self.ui.conditioninput.clear()
        self.update_state_box()

    def show_sm_widget(self):
        self.ui.expandwidget.setEnabled(True)
        self.ui.transwidget.setEnabled(False)
        self.ui.statewidget.hide()
        self.ui.genwidget.hide()
        self.ui.smwidget.show()

    def show_sm_code(self):
        sender = self.sender()

        for button in self.gen_buttons:
            button.setEnabled(True)

        sender.setEnabled(False)
        self.ui.smcode.clear()

        if sender == self.ui.genButton_1:
            tree_str = self.fsm.display_tree()
            self.ui.smcode.append(tree_str)

            self.ui.smcode.append("\nTransitions:")
            for state_id, node in self.fsm.span_tree.items():
                transitions_for_state = self.fsm.state_transitions_map.get(state_id, {})
                if transitions_for_state:
                    for event, to_state in transitions_for_state.items():
                        self.ui.smcode.append(f"State{state_id}  ->  State{to_state}  on event  '{event}'")

        elif sender == self.ui.genButton_2:
            if self.class_code is None:
                self.class_code = self.fsm.generate_class_code()
                with open("gen/state_machine.py", "w") as f:
                    f.write(self.class_code)
            self.ui.smcode.append(self.class_code)
            # self.fsm.export_to_dot()

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
