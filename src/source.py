# Main template 

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

ui, _ = loadUiType('gui.ui')

class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        # function to setup buttons
        self.HandleButtons()

    def HandleButtons(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()

if __name__ == "__main__" :
    main()


