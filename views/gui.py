from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("central_widget")

        font = QtGui.QFont("MS Shell Dlg 2", 9)
        MainWindow.setFont(font)

        font_16 = QtGui.QFont("MS Shell Dlg 2", 16)
        font_16.setBold(True)
        font_14 = QtGui.QFont("MS Shell Dlg 2", 14)
        font_14.setBold(True)
        font_12 = QtGui.QFont("MS Shell Dlg 2", 12)
        font_10 = QtGui.QFont("MS Shell Dlg 2", 10)

        with open("views/styles.qss", "r") as f:
            MainWindow.setStyleSheet(f.read())

        # main area
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(29, 129, 1141, 580))

        # add square widget
        self.square = QtWidgets.QWidget(self.main_widget)
        self.square.setGeometry(QtCore.QRect(175, 20, 790, 560))

        self.addsquare = QtWidgets.QLabel(self.square)
        self.addsquare.setGeometry(QtCore.QRect(0, 0, 791, 81))
        self.addsquare.setFont(font_16)
        self.addsquare.setAlignment(QtCore.Qt.AlignCenter)
        self.addsquare.setText("Add First Logical Square")

        self.addlabel = QtWidgets.QLabel(self.square)
        self.addlabel.setGeometry(QtCore.QRect(0, 80, 791, 81))
        self.addlabel.setFont(font_12)
        self.addlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addlabel.setWordWrap(True)
        self.addlabel.setText("Add chosen corners to create first states. "
                         "If you leave any vertex empty it will be assigned the \'true\' value.")

        self.expandbox = QtWidgets.QComboBox(self.square)
        self.expandbox.setGeometry(QtCore.QRect(335, 180, 111, 31))
        self.expandbox.setVisible(False)

        self.inputA = QtWidgets.QLineEdit(self.square)
        self.inputA.setGeometry(QtCore.QRect(260, 200, 271, 31))
        self.inputA.setFont(font)

        self.inputE = QtWidgets.QLineEdit(self.square)
        self.inputE.setGeometry(QtCore.QRect(260, 260, 271, 31))
        self.inputE.setFont(font)

        self.inputI = QtWidgets.QLineEdit(self.square)
        self.inputI.setGeometry(QtCore.QRect(260, 320, 271, 31))
        self.inputI.setFont(font)

        self.inputO = QtWidgets.QLineEdit(self.square)
        self.inputO.setGeometry(QtCore.QRect(260, 380, 271, 31))
        self.inputO.setFont(font)

        self.labelA = QtWidgets.QLabel(self.square)
        self.labelA.setGeometry(QtCore.QRect(200, 190, 51, 51))
        self.labelA.setFont(font_14)
        self.labelA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelA.setText("A")

        self.labelE = QtWidgets.QLabel(self.square)
        self.labelE.setGeometry(QtCore.QRect(200, 250, 51, 51))
        self.labelE.setFont(font_14)
        self.labelE.setAlignment(QtCore.Qt.AlignCenter)
        self.labelE.setText("E")

        self.labelI = QtWidgets.QLabel(self.square)
        self.labelI.setGeometry(QtCore.QRect(200, 310, 51, 51))
        self.labelI.setFont(font_14)
        self.labelI.setAlignment(QtCore.Qt.AlignCenter)
        self.labelI.setText("I")

        self.labelO = QtWidgets.QLabel(self.square)
        self.labelO.setGeometry(QtCore.QRect(200, 370, 51, 51))
        self.labelO.setFont(font_14)
        self.labelO.setAlignment(QtCore.Qt.AlignCenter)
        self.labelO.setText("O")

        self.add_square_button = QtWidgets.QPushButton(self.square)
        self.add_square_button.setGeometry(QtCore.QRect(305, 450, 171, 41))
        self.add_square_button.setFont(font)
        self.add_square_button.setText("Add")

        # state tree widget
        self.tree = QtWidgets.QWidget(self.main_widget)
        self.tree.setGeometry(QtCore.QRect(175, 20, 790, 560))
        self.tree.setVisible(False)

        widget_title = QtWidgets.QLabel(self.tree)
        widget_title.setGeometry(QtCore.QRect(0, 0, 791, 81))
        widget_title.setFont(font_16)
        widget_title.setAlignment(QtCore.Qt.AlignCenter)
        widget_title.setText("State Tree")

        self.statetree = GraphicsLayoutWidget(self.tree)
        self.statetree.setGeometry(QtCore.QRect(30, 70, 731, 411))
        self.statetree.setBackground('w')
        self.statetree.setObjectName("graph")
        self.tree_plot = self.statetree.addPlot()
        self.tree_plot.hideAxis('left')
        self.tree_plot.hideAxis('bottom')

        self.name_button = QtWidgets.QPushButton(self.tree)
        self.name_button.setGeometry(QtCore.QRect(305, 500, 171, 41))
        self.name_button.setFont(font)
        self.name_button.setText("Set Names")

        # set name widget
        self.names = QtWidgets.QWidget(self.main_widget)
        self.names.setGeometry(QtCore.QRect(175, 20, 790, 560))
        self.names.setVisible(False)

        widget_title = QtWidgets.QLabel(self.names)
        widget_title.setGeometry(QtCore.QRect(0, 0, 791, 81))
        widget_title.setFont(font_16)
        widget_title.setAlignment(QtCore.Qt.AlignCenter)
        widget_title.setText("Set Names For States")

        addlabel = QtWidgets.QLabel(self.names)
        addlabel.setGeometry(QtCore.QRect(0, 80, 791, 81))
        addlabel.setFont(font_12)
        addlabel.setAlignment(QtCore.Qt.AlignCenter)
        addlabel.setWordWrap(True)
        addlabel.setText("Here you can choose your state names. Select a state "
                         "from box below and input new name in the line edit.")

        self.namebox = QtWidgets.QComboBox(self.names)
        self.namebox.setGeometry(QtCore.QRect(340, 190, 111, 31))

        self.assertlabel = QtWidgets.QLabel(self.names)
        self.assertlabel.setGeometry(QtCore.QRect(0, 250, 790, 50))
        self.assertlabel.setFont(font)
        self.assertlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.assertlabel.setText("State Assertion: ")

        self.name_input = QtWidgets.QLineEdit(self.names)
        self.name_input.setGeometry(QtCore.QRect(260, 350, 271, 31))
        self.name_input.setFont(font)

        self.change_name_button = QtWidgets.QPushButton(self.names)
        self.change_name_button.setGeometry(QtCore.QRect(305, 500, 171, 41))
        self.change_name_button.setFont(font)
        self.change_name_button.setText("Change Name")

        # state machine code widget
        self.code = QtWidgets.QWidget(self.main_widget)
        self.code.setGeometry(QtCore.QRect(175, 20, 790, 560))
        self.code.setVisible(False)

        widget_title = QtWidgets.QLabel(self.code)
        widget_title.setGeometry(QtCore.QRect(0, 0, 791, 81))
        widget_title.setFont(font_16)
        widget_title.setAlignment(QtCore.Qt.AlignCenter)
        widget_title.setText("Generate State Machine Code")

        self.smcode = QtWidgets.QTextEdit(self.code)
        self.smcode.setGeometry(QtCore.QRect(30, 70, 731, 411))
        self.smcode.setReadOnly(True)
        self.smcode.setFont(font_10)

        # code generation buttons
        self.generate_buttons = QtWidgets.QWidget(self.code)
        self.generate_buttons.setGeometry(QtCore.QRect(0, 500, 790, 41))
        buttons = QtWidgets.QHBoxLayout(self.generate_buttons)
        buttons.setContentsMargins(0, 0, 0, 0)
        buttons.setSpacing(40)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.class_button = QtWidgets.QPushButton(self.generate_buttons)
        self.class_button.setSizePolicy(sizePolicy)
        self.class_button.setText("Class Code")
        self.class_button.setObjectName("class_button")
        buttons.addWidget(self.class_button)

        self.qt_button = QtWidgets.QPushButton(self.generate_buttons)
        self.qt_button.setSizePolicy(sizePolicy)
        self.qt_button.setObjectName("qt_button")
        self.qt_button.setText("Qt Code")
        buttons.addWidget(self.qt_button)

        self.trans_button = QtWidgets.QPushButton(self.generate_buttons)
        self.trans_button.setSizePolicy(sizePolicy)
        self.trans_button.setObjectName("trans_button")
        self.trans_button.setText("Transition Code")
        buttons.addWidget(self.trans_button)

        self.sml_button = QtWidgets.QPushButton(self.generate_buttons)
        self.sml_button.setSizePolicy(sizePolicy)
        self.sml_button.setObjectName("sml_button")
        self.sml_button.setText("SML Code")
        buttons.addWidget(self.sml_button)

        # sm graph and transitions widget
        self.transitions = QtWidgets.QWidget(self.main_widget)
        self.transitions.setGeometry(QtCore.QRect(175, 20, 790, 560))
        self.transitions.setVisible(False)

        widget_title = QtWidgets.QLabel(self.transitions)
        widget_title.setGeometry(QtCore.QRect(0, 0, 791, 81))
        widget_title.setFont(font_16)
        widget_title.setAlignment(QtCore.Qt.AlignCenter)
        widget_title.setText("State Machine Diagram")

        self.sm_graph = GraphicsLayoutWidget(self.transitions)
        self.sm_graph.setGeometry(QtCore.QRect(30, 70, 731, 321))
        self.sm_graph.setObjectName("graph")
        self.sm_graph.setBackground('w')
        self.sm_plot = self.sm_graph.addPlot()
        self.sm_plot.hideAxis('left')
        self.sm_plot.hideAxis('bottom')

        translabel = QtWidgets.QLabel(self.transitions)
        translabel.setGeometry(QtCore.QRect(0, 380, 791, 111))
        translabel.setFont(font_12)
        translabel.setAlignment(QtCore.Qt.AlignCenter)
        translabel.setWordWrap(True)
        translabel.setText("Here you can add transitions between states. "
                           "Select suitable states from boxes, put transition "
                           "condition in the input line and click ENTER.")

        fromlabel = QtWidgets.QLabel(self.transitions)
        fromlabel.setGeometry(QtCore.QRect(0, 500, 81, 41))
        fromlabel.setFont(font)
        fromlabel.setAlignment(QtCore.Qt.AlignCenter)
        fromlabel.setText("FROM")

        self.frombox = QtWidgets.QComboBox(self.transitions)
        self.frombox.setGeometry(QtCore.QRect(80, 505, 111, 31))

        tolabel = QtWidgets.QLabel(self.transitions)
        tolabel.setGeometry(QtCore.QRect(230, 500, 61, 41))
        tolabel.setFont(font)
        tolabel.setAlignment(QtCore.Qt.AlignCenter)
        tolabel.setText("TO")

        self.tobox = QtWidgets.QComboBox(self.transitions)
        self.tobox.setGeometry(QtCore.QRect(290, 505, 111, 31))

        iflabel = QtWidgets.QLabel(self.transitions)
        iflabel.setGeometry(QtCore.QRect(450, 500, 51, 41))
        iflabel.setFont(font)
        iflabel.setAlignment(QtCore.Qt.AlignCenter)
        iflabel.setText("IF")

        self.ifinput = QtWidgets.QLineEdit(self.transitions)
        self.ifinput.setGeometry(QtCore.QRect(500, 505, 271, 31))
        self.ifinput.setFont(font)

        # assertions widget
        self.assertions = QtWidgets.QWidget(self.main_widget)
        self.assertions.setGeometry(QtCore.QRect(175, 20, 790, 560))
        self.assertions.setVisible(False)

        widget_title = QtWidgets.QLabel(self.assertions)
        widget_title.setGeometry(QtCore.QRect(0, 0, 791, 81))
        widget_title.setFont(font_16)
        widget_title.setAlignment(QtCore.Qt.AlignCenter)
        widget_title.setText("State Assertions")

        self.assert_tree = QtWidgets.QTextEdit(self.assertions)
        self.assert_tree.setGeometry(QtCore.QRect(30, 70, 731, 411))
        self.assert_tree.setReadOnly(True)
        self.assert_tree.setFont(font_10)

        # solver widget
        self.solver = QtWidgets.QWidget(self.main_widget)
        self.solver.setGeometry(QtCore.QRect(175, 20, 790, 560))
        self.solver.setVisible(False)

        widget_title = QtWidgets.QLabel(self.solver)
        widget_title.setGeometry(QtCore.QRect(0, 0, 791, 81))
        widget_title.setFont(font_16)
        widget_title.setAlignment(QtCore.Qt.AlignCenter)
        widget_title.setText("Logical Disjointness Verification")

        self.solver_input = QtWidgets.QTextEdit(self.solver)
        self.solver_input.setGeometry(QtCore.QRect(30, 70, 731, 150))
        self.solver_input.setFont(font_10)

        self.solver_feedback = QtWidgets.QTextEdit(self.solver)
        self.solver_feedback.setGeometry(QtCore.QRect(30, 240, 731, 150))
        self.solver_feedback.setReadOnly(True)
        self.solver_feedback.setFont(font_10)

        solverlabel = QtWidgets.QLabel(self.solver)
        solverlabel.setGeometry(QtCore.QRect(0, 380, 791, 111))
        solverlabel.setFont(font_12)
        solverlabel.setAlignment(QtCore.Qt.AlignCenter)
        solverlabel.setWordWrap(True)
        solverlabel.setText("Here you can check whether all pairs of given "
                            "states are logically disjoint, meaning that "
                            "no two states share a common truth assignment.")

        self.check_states_button = QtWidgets.QPushButton(self.solver)
        self.check_states_button.setGeometry(QtCore.QRect(305, 500, 171, 41))
        self.check_states_button.setFont(font)
        self.check_states_button.setObjectName("check_states_button")
        self.check_states_button.setText("Check States")

        # ai widget
        self.ai = QtWidgets.QWidget(self.main_widget)
        self.ai.setGeometry(QtCore.QRect(175, 20, 790, 560))
        self.ai.setVisible(False)

        widget_title = QtWidgets.QLabel(self.ai)
        widget_title.setGeometry(QtCore.QRect(0, 0, 791, 81))
        widget_title.setFont(font_16)
        widget_title.setAlignment(QtCore.Qt.AlignCenter)
        widget_title.setText("LLM Chat")

        self.ai.ai_feedback = QtWidgets.QTextEdit(self.ai)
        self.ai.ai_feedback.setGeometry(QtCore.QRect(30, 70, 731, 150))
        self.ai.ai_feedback.setReadOnly(True)
        self.ai.ai_feedback.setFont(font_10)

        ailabel = QtWidgets.QLabel(self.ai)
        ailabel.setGeometry(QtCore.QRect(0, 210, 791, 111))
        ailabel.setFont(font_12)
        ailabel.setAlignment(QtCore.Qt.AlignCenter)
        ailabel.setWordWrap(True)
        ailabel.setText("Here you can ask LLM to help you complete logical squares. "
                        "Give it a domain name and selected square corners and it will try "
                        "to generate remaining vertices.")

        self.ai.ai_input = QtWidgets.QTextEdit(self.ai)
        self.ai.ai_input.setGeometry(QtCore.QRect(30, 310, 731, 80))
        self.ai.ai_input.setFont(font_10)

        ailabel = QtWidgets.QLabel(self.ai)
        ailabel.setGeometry(QtCore.QRect(0, 380, 791, 111))
        ailabel.setFont(font_12)
        ailabel.setAlignment(QtCore.Qt.AlignCenter)
        ailabel.setWordWrap(True)
        ailabel.setText("Example input can look like this:\n"
                        "Airport traffic management system, A=taxiing")

        self.send_request_button = QtWidgets.QPushButton(self.ai)
        self.send_request_button.setGeometry(QtCore.QRect(305, 500, 171, 41))
        self.send_request_button.setFont(font)
        self.send_request_button.setText("Send Request")





        # menu buttons

        self.buttonwidget = QtWidgets.QWidget(self.centralwidget)
        self.buttonwidget.setGeometry(QtCore.QRect(30, 50, 1141, 51))
        # self.buttonwidget.setEnabled(False)
        self.buttonwidget.setObjectName("buttons")
        buttons = QtWidgets.QHBoxLayout(self.buttonwidget)
        buttons.setContentsMargins(0, 0, 0, 0)
        buttons.setSpacing(20)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.square_button = QtWidgets.QPushButton(self.buttonwidget)
        self.square_button.setSizePolicy(sizePolicy)
        self.square_button.setObjectName("square_button")
        self.square_button.setText("Add Square")
        buttons.addWidget(self.square_button)

        self.tree_button = QtWidgets.QPushButton(self.buttonwidget)
        self.tree_button.setSizePolicy(sizePolicy)
        self.tree_button.setObjectName("tree_button")
        self.tree_button.setText("State Tree")
        self.tree_button.setVisible(False)
        buttons.addWidget(self.tree_button)

        self.sm_button = QtWidgets.QPushButton(self.buttonwidget)
        self.sm_button.setSizePolicy(sizePolicy)
        self.sm_button.setObjectName("sm_button")
        self.sm_button.setText("State Machine")
        self.sm_button.setVisible(False)
        buttons.addWidget(self.sm_button)

        self.assertions_button = QtWidgets.QPushButton(self.buttonwidget)
        self.assertions_button.setSizePolicy(sizePolicy)
        self.assertions_button.setObjectName("assertions_button")
        self.assertions_button.setText("Assertions")
        self.assertions_button.setVisible(False)
        buttons.addWidget(self.assertions_button)

        self.expand_button = QtWidgets.QPushButton(self.buttonwidget)
        self.expand_button.setSizePolicy(sizePolicy)
        self.expand_button.setObjectName("expand_button")
        self.expand_button.setText("Expand State")
        self.expand_button.setVisible(False)
        buttons.addWidget(self.expand_button)

        self.ai_button = QtWidgets.QPushButton(self.buttonwidget)
        self.ai_button.setSizePolicy(sizePolicy)
        self.ai_button.setObjectName("ai_button")
        self.ai_button.setText("LLM Chat")
        buttons.addWidget(self.ai_button)

        self.solver_button = QtWidgets.QPushButton(self.buttonwidget)
        self.solver_button.setSizePolicy(sizePolicy)
        self.solver_button.setObjectName("solver_button")
        self.solver_button.setText("Solver")
        buttons.addWidget(self.solver_button)

        self.gen_button = QtWidgets.QPushButton(self.buttonwidget)
        self.gen_button.setSizePolicy(sizePolicy)
        self.gen_button.setObjectName("gen_button")
        self.gen_button.setText("Generate Code")
        self.gen_button.setVisible(False)
        buttons.addWidget(self.gen_button)

        self.reset_button = QtWidgets.QPushButton(self.buttonwidget)
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setText("Reset")
        buttons.addWidget(self.reset_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "State Machine Generator"))

