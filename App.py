from LOGIN import *
from PyQt5 import *
from PyQt5.QtWidgets import QMessageBox
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wndwLogin = QtWidgets.QMainWindow()
    ui = Ui_wndwLogin()
    ui.setupUi(wndwLogin)
    wndwLogin.show()
    sys.exit(app.exec_())

