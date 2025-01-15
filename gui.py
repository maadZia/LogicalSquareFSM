from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1062, 712)
        MainWindow.setFixedSize(1062, 712)

        font = QtGui.QFont("Arial", 9)
        MainWindow.setFont(font)

        font_16 = QtGui.QFont("Arial Black", 16)
        font_14 = QtGui.QFont("Arial Black", 14)
        font_12 = QtGui.QFont("Arial Black", 12)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.addwidget = QtWidgets.QWidget(self.centralwidget)
        self.addwidget.setGeometry(QtCore.QRect(20, 20, 531, 671))

        self.squarewidget = QtWidgets.QWidget(self.addwidget)
        self.squarewidget.setGeometry(QtCore.QRect(0, 0, 531, 361))

        self.addlabel = QtWidgets.QLabel(self.squarewidget)
        self.addlabel.setGeometry(QtCore.QRect(0, 0, 531, 81))
        self.addlabel.setFont(font_16)
        self.addlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addlabel.setText("Add logical square")

        self.inputA = QtWidgets.QLineEdit(self.squarewidget)
        self.inputA.setGeometry(QtCore.QRect(170, 110, 191, 31))

        self.inputE = QtWidgets.QLineEdit(self.squarewidget)
        self.inputE.setGeometry(QtCore.QRect(170, 160, 191, 31))

        self.inputI = QtWidgets.QLineEdit(self.squarewidget)
        self.inputI.setGeometry(QtCore.QRect(170, 210, 191, 31))

        self.inputO = QtWidgets.QLineEdit(self.squarewidget)
        self.inputO.setGeometry(QtCore.QRect(170, 260, 191, 31))

        self.labelA = QtWidgets.QLabel(self.squarewidget)
        self.labelA.setGeometry(QtCore.QRect(120, 100, 51, 51))
        self.labelA.setFont(font_12)
        self.labelA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelA.setText("A")

        self.labelE = QtWidgets.QLabel(self.squarewidget)
        self.labelE.setGeometry(QtCore.QRect(120, 150, 51, 51))
        self.labelE.setFont(font_12)
        self.labelE.setAlignment(QtCore.Qt.AlignCenter)
        self.labelE.setText("E")

        self.labelI = QtWidgets.QLabel(self.squarewidget)
        self.labelI.setGeometry(QtCore.QRect(120, 200, 51, 51))
        self.labelI.setFont(font_12)
        self.labelI.setAlignment(QtCore.Qt.AlignCenter)
        self.labelI.setText("I")

        self.labelO = QtWidgets.QLabel(self.squarewidget)
        self.labelO.setGeometry(QtCore.QRect(120, 250, 51, 51))
        self.labelO.setFont(font_12)
        self.labelO.setAlignment(QtCore.Qt.AlignCenter)
        self.labelO.setText("O")

        self.addButton_1 = QtWidgets.QPushButton(self.squarewidget)
        self.addButton_1.setGeometry(QtCore.QRect(210, 310, 111, 31))
        self.addButton_1.setText("Add")

        self.namewidget = QtWidgets.QWidget(self.addwidget)
        self.namewidget.setEnabled(False)
        self.namewidget.setGeometry(QtCore.QRect(0, 370, 531, 301))

        self.namelabel = QtWidgets.QLabel(self.namewidget)
        self.namelabel.setGeometry(QtCore.QRect(0, 0, 531, 81))
        self.namelabel.setFont(font_16)
        self.namelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namelabel.setText("Choose names for states")

        self.namebox = QtWidgets.QComboBox(self.namewidget)
        self.namebox.setGeometry(QtCore.QRect(70, 130, 101, 31))

        self.nameinput = QtWidgets.QLineEdit(self.namewidget)
        self.nameinput.setGeometry(QtCore.QRect(220, 130, 241, 31))

        self.nextButton_1 = QtWidgets.QPushButton(self.namewidget)
        self.nextButton_1.setGeometry(QtCore.QRect(210, 240, 111, 31))
        self.nextButton_1.setText("Next")

        self.statewidget = QtWidgets.QWidget(self.centralwidget)
        self.statewidget.setGeometry(QtCore.QRect(20, 20, 531, 671))
        self.statewidget.hide()

        self.expandwidget = QtWidgets.QWidget(self.statewidget)
        self.expandwidget.setGeometry(QtCore.QRect(-1, -1, 531, 241))

        self.expandlabel = QtWidgets.QLabel(self.expandwidget)
        self.expandlabel.setGeometry(QtCore.QRect(0, 0, 531, 81))
        self.expandlabel.setFont(font_16)
        self.expandlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.expandlabel.setText("Choose a state to expand")

        self.expandbox = QtWidgets.QComboBox(self.expandwidget)
        self.expandbox.setGeometry(QtCore.QRect(130, 100, 101, 31))

        self.expandButton = QtWidgets.QPushButton(self.expandwidget)
        self.expandButton.setGeometry(QtCore.QRect(300, 100, 111, 31))
        self.expandButton.setText("Expand")

        self.nextButton_2 = QtWidgets.QPushButton(self.expandwidget)
        self.nextButton_2.setGeometry(QtCore.QRect(210, 180, 111, 31))
        self.nextButton_2.setText("Next")

        self.transwidget = QtWidgets.QWidget(self.statewidget)
        self.transwidget.setEnabled(False)
        self.transwidget.setGeometry(QtCore.QRect(-1, 249, 531, 421))

        self.translabel = QtWidgets.QLabel(self.transwidget)
        self.translabel.setGeometry(QtCore.QRect(0, 0, 531, 81))
        self.translabel.setFont(font_14)
        self.translabel.setAlignment(QtCore.Qt.AlignCenter)
        self.translabel.setText("Add transitions between states")

        self.fromlabel = QtWidgets.QLabel(self.transwidget)
        self.fromlabel.setGeometry(QtCore.QRect(100, 100, 201, 51))
        self.fromlabel.setFont(font_12)
        self.fromlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fromlabel.setText("From state")

        self.frombox = QtWidgets.QComboBox(self.transwidget)
        self.frombox.setGeometry(QtCore.QRect(300, 110, 101, 31))

        self.tolabel = QtWidgets.QLabel(self.transwidget)
        self.tolabel.setGeometry(QtCore.QRect(90, 160, 201, 51))
        self.tolabel.setFont(font_12)
        self.tolabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tolabel.setText("To state")

        self.tobox = QtWidgets.QComboBox(self.transwidget)
        self.tobox.setGeometry(QtCore.QRect(300, 170, 101, 31))

        self.conditionlabel = QtWidgets.QLabel(self.transwidget)
        self.conditionlabel.setGeometry(QtCore.QRect(40, 240, 201, 51))
        self.conditionlabel.setFont(font_12)
        self.conditionlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.conditionlabel.setText("On condition")

        self.conditioninput = QtWidgets.QLineEdit(self.transwidget)
        self.conditioninput.setGeometry(QtCore.QRect(240, 250, 221, 31))

        self.nextButton_3 = QtWidgets.QPushButton(self.transwidget)
        self.nextButton_3.setGeometry(QtCore.QRect(210, 360, 111, 31))
        self.nextButton_3.setText("Next")

        self.smwidget = QtWidgets.QWidget(self.centralwidget)
        self.smwidget.setGeometry(QtCore.QRect(20, 20, 1021, 681))
        self.smwidget.hide()

        self.smlabel = QtWidgets.QLabel(self.smwidget)
        self.smlabel.setGeometry(QtCore.QRect(0, 0, 531, 51))
        self.smlabel.setFont(font_12)
        self.smlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.smlabel.setText("State machine code")

        self.smcode = QtWidgets.QTextEdit(self.smwidget)
        self.smcode.setGeometry(QtCore.QRect(0, 40, 531, 631))
        self.smcode.setReadOnly(True)

        self.resetButton = QtWidgets.QPushButton(self.smwidget)
        self.resetButton.setGeometry(QtCore.QRect(720, 650, 111, 31))
        self.resetButton.setText("Reset")

        self.genlabel = QtWidgets.QLabel(self.smwidget)
        self.genlabel.setGeometry(QtCore.QRect(530, 60, 491, 61))
        self.genlabel.setFont(font_12)
        self.genlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.genlabel.setText("Choose code generation method")

        self.genButton_1 = QtWidgets.QPushButton(self.smwidget)
        self.genButton_1.setGeometry(QtCore.QRect(620, 140, 141, 31))
        self.genButton_1.setText("Class code")

        self.genButton_2 = QtWidgets.QPushButton(self.smwidget)
        self.genButton_2.setGeometry(QtCore.QRect(620, 190, 141, 31))
        self.genButton_2.setText("Transition code")

        self.genButton_3 = QtWidgets.QPushButton(self.smwidget)
        self.genButton_3.setGeometry(QtCore.QRect(790, 140, 131, 31))
        self.genButton_3.setText("Qt code")

        self.genButton_4 = QtWidgets.QPushButton(self.smwidget)
        self.genButton_4.setGeometry(QtCore.QRect(790, 190, 131, 31))
        self.genButton_4.setText("SML code")

        self.genwidget = QtWidgets.QWidget(self.centralwidget)
        self.genwidget.setGeometry(QtCore.QRect(569, 19, 471, 671))

        self.stlabel = QtWidgets.QLabel(self.genwidget)
        self.stlabel.setGeometry(QtCore.QRect(0, 0, 471, 51))
        self.stlabel.setFont(font_12)
        self.stlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stlabel.setText("State tree")

        # self.statetree = QtWidgets.QTextEdit(self.genwidget)
        # self.statetree.setGeometry(QtCore.QRect(0, 50, 471, 281))
        # self.statetree.setReadOnly(True)
        self.statetree = GraphicsLayoutWidget(self.genwidget)
        self.statetree.setGeometry(QtCore.QRect(0, 50, 471, 281))
        self.statetree.setBackground('w')  # Ustawienie białego tła
        self.statetree.setStyleSheet("""
            border: 1px solid black;  /* Cienka czarna ramka */
        """)
        self.graph_plot = self.statetree.addPlot()
        self.graph_plot.hideAxis('left')  # Ukrycie osi pionowej
        self.graph_plot.hideAxis('bottom')

        self.stlabel_2 = QtWidgets.QLabel(self.genwidget)
        self.stlabel_2.setGeometry(QtCore.QRect(0, 340, 471, 51))
        self.stlabel_2.setFont(font_12)
        self.stlabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.stlabel_2.setText("Transitions")

        self.transitions = QtWidgets.QTextEdit(self.genwidget)
        self.transitions.setGeometry(QtCore.QRect(0, 390, 471, 281))
        self.transitions.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "State Machine Generator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
