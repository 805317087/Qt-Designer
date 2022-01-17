from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Title.setText("hello Python")
        self.World.clicked.connect(lambda : self.onWorldClicked(5))
        self.China.clicked.connect(self.onChinaClicked)
        self.lineEdit.textChanged.connect(self.onlineEditTextChanged)

    def onWorldClicked(self, remark):
        print(remark)
        self.Title.setText("Hello World")

    def onChinaClicked(self):
        self.Title.setText("zz")

    def onlineEditTextChanged(self,p_str):
        print(p_str)
        self.World.setText(p_str)
