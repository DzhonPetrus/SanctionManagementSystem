# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import ICONS.resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class Ui_wndwLogin(object):
    def setupUi(self, wndwLogin):
        wndwLogin.setObjectName("wndwLogin")
        wndwLogin.setWindowModality(QtCore.Qt.NonModal)
        wndwLogin.resize(1024, 768)
        wndwLogin.setMinimumSize(QtCore.QSize(1024, 768))
        wndwLogin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        wndwLogin.setStyleSheet("QWidget{\n"
                                "    font-family:\'Open Sans\';\n"
                                "    font-size:16pt;\n"
                                "}\n"
                                "\n"
                                "QFrame{\n"
                                "  background-color: rgb(255,255,255);\n"
                                "  color: black;\n"
                                "}\n"
                                "\n"
                                "QPushButton {\n"
                                "  background-color: #4CAF50;\n"
                                "  color: white;\n"
                                "  font-weight:bold;\n"
                                "  padding: 14px 20px;\n"
                                "  margin: 8px 0;\n"
                                "  border: none;\n"
                                "  width: 100%;\n"
                                "}\n"
                                "#btnLogin {\n"
                                "  background-color: rgba(255,200,80,1)\n"
                                "}\n"
                                "#btnLogin:hover {\n"
                                "  background-color: rgba(255,200,80,.8)\n"
                                "}\n"
                                "#btnExit {\n"
                                "  background-color: rgba(0,238,191,1);\n"
                                "}\n"
                                "#btnExit:hover {\n"
                                "  background-color: rgba(0,238,191,.8);\n"
                                "}\n"
                                "#frmBG{\n"
                                "  background-color:rgba(255,200,80,1);\n"
                                "}")
        wndwLogin.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        wndwLogin.setAnimated(True)
        wndwLogin.setTabShape(QtWidgets.QTabWidget.Rounded)
        wndwLogin.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(wndwLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.frmBG = QtWidgets.QFrame(self.centralwidget)
        self.frmBG.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.frmBG.setAutoFillBackground(False)
        self.frmBG.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmBG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmBG.setLineWidth(0)
        self.frmBG.setObjectName("frmBG")
        self.frmLogin = QtWidgets.QFrame(self.frmBG)
        self.frmLogin.setGeometry(QtCore.QRect(140, 80, 750, 600))
        self.frmLogin.setAutoFillBackground(False)
        self.frmLogin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmLogin.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmLogin.setObjectName("frmLogin")
        self.btnLogin = QtWidgets.QPushButton(self.frmLogin)
        self.btnLogin.setGeometry(QtCore.QRect(70, 450, 621, 63))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.setMouseTracking(False)
        self.btnLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnLogin.setObjectName("btnLogin")
        self.btnExit = QtWidgets.QPushButton(self.frmLogin)
        self.btnExit.setGeometry(QtCore.QRect(70, 510, 621, 63))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExit.setMouseTracking(False)
        self.btnExit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnExit.setObjectName("btnExit")
        self.txtUsername = QtWidgets.QTextEdit(self.frmLogin)
        self.txtUsername.setGeometry(QtCore.QRect(70, 320, 621, 50))
        self.txtUsername.setTabChangesFocus(True)
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QTextEdit(self.frmLogin)
        self.txtPassword.setGeometry(QtCore.QRect(70, 380, 621, 50))
        self.txtPassword.setTabChangesFocus(True)
        self.txtPassword.setObjectName("txtPassword")
        self.label = QtWidgets.QLabel(self.frmLogin)
        self.label.setGeometry(QtCore.QRect(260, 50, 261, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ICONS/browser.png"))
        self.label.setObjectName("label")
        wndwLogin.setCentralWidget(self.centralwidget)
        self.retranslateUi(wndwLogin)
        QtCore.QMetaObject.connectSlotsByName(wndwLogin)

    def retranslateUi(self, wndwLogin):
        _translate = QtCore.QCoreApplication.translate
        wndwLogin.setWindowTitle(
            _translate("wndwLogin", "Sanction Management System - LOGIN"))
        self.btnLogin.setText(_translate("wndwLogin", "LOGIN"))
        self.btnExit.setText(_translate("wndwLogin", "EXIT"))
        self.txtUsername.setPlaceholderText(_translate("wndwLogin",
                                                       "Username"))
        self.txtPassword.setPlaceholderText(_translate("wndwLogin",
                                                       "Password"))

        #CUSTOM CODE
        self.btnExit.clicked.connect(self.confirmationExit)
        self.btnLogin.clicked.connect(self.Login)

    def confirmationExit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sanction Management System - Confirmation")
        msg.setText("Are you sure you want to exit the program?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        x = msg.exec_()
        if (x == 16384):
            sys.exit()

    def Login(self):
        import connector
        import DB.User as dbUser

        self.txtUsername.setStyleSheet(
            "#txtUsername{background-color:rgba(255,255,255,.8);}")
        self.txtPassword.setStyleSheet(
            "#txtPassword{background-color:rgba(255,255,255,.8);}")
        username = self.txtUsername.toPlainText()
        password = self.txtPassword.toPlainText()
        if username == '':
            self.txtUsername.setPlaceholderText('PLEASE ENTER A USERNAME')
            self.txtUsername.setStyleSheet(
                "#txtUsername{background-color:rgba(255,112,80,.7);}")
            self.txtUsername.setFocus()
        elif password == '':
            self.txtPassword.setPlaceholderText('PLEASE ENTER A PASSWORD')
            self.txtPassword.setStyleSheet(
                "#txtPassword{background-color:rgba(255,112,80,.7);}")
            self.txtUsername.setFocus()
        else:
            exist = dbUser.checkExistingUser(username, password)
            if not exist:
                msg = QMessageBox()
                msg.setWindowTitle("Sanction Management System - Login Failed")
                msg.setText(
                    "INVALID CREDENTIALS!\nPlease Enter correct Username and Password!"
                )
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec_()
                self.txtPassword.clear()
                self.txtPassword.setFocus()
            else:
                _userID = exist[0]
                _userRole = exist[3]
                print("id:", _userID, "role: ", _userRole)
