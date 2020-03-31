# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogUser.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import ICONS.resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import connector
import DB.User as dbUser
from PyQt5.QtWidgets import QMessageBox


class Ui_dgUser(object):
    def __init__(self, _id, username, password, role):
        self._userID = _id
        self._username = username
        self._password = password
        self._role = role

    def setupUi(self, dgUser):
        self.dgUser = dgUser
        dgUser.setObjectName("dgUser")
        dgUser.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dgUser.sizePolicy().hasHeightForWidth())
        dgUser.setSizePolicy(sizePolicy)
        dgUser.setMinimumSize(QtCore.QSize(800, 600))
        dgUser.setMaximumSize(QtCore.QSize(800, 600))
        dgUser.setStyleSheet("QDialog, QFormLayout, QLabel{\n"
                             "font-family:\'Open Sans\';\n"
                             "font-size:14pt;\n"
                             "background-color: rgba(0,238,191,1);\n"
                             "color:white;\n"
                             "}\n"
                             "QPushButton {\n"
                             "color:rgb(189,189,189);\n"
                             "}\n"
                             "QPushButton:hover {\n"
                             "color:rgb(255,255,255);\n"
                             "}\n"
                             "QPushButton#btnPrimary:hover {\n"
                             "color: rgba(0,238,191,1);\n"
                             "background-color: rgb(255,255,255);\n"
                             "}\n"
                             "")
        self.formLayoutWidget = QtWidgets.QWidget(dgUser)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 70, 801, 485))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight
                                          | QtCore.Qt.AlignTrailing
                                          | QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter
                                         | QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(19, 19, 19, 19)
        self.formLayout.setSpacing(19)
        self.formLayout.setObjectName("formLayout")
        self.lblUserID = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblUserID.setObjectName("lblUserID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.lblUserID)
        self.txtUserID = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txtUserID.setEnabled(False)
        self.txtUserID.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(False)
        self.txtUserID.setFont(font)
        self.txtUserID.setTabChangesFocus(True)
        self.txtUserID.setObjectName("txtUserID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.txtUserID)
        self.lblUsername = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblUsername.setObjectName("lblUsername")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.lblUsername)
        self.txtUsername = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txtUsername.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(False)
        self.txtUsername.setFont(font)
        self.txtUsername.setTabChangesFocus(True)
        self.txtUsername.setObjectName("txtUsername")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.txtUsername)
        self.lblPassword = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblPassword.setObjectName("lblPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.lblPassword)
        self.txtPassword = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txtPassword.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(False)
        self.txtPassword.setFont(font)
        self.txtPassword.setTabChangesFocus(True)
        self.txtPassword.setObjectName("txtPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.txtPassword)
        self.lblRole = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblRole.setObjectName("lblRole")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.lblRole)
        self.cbRole = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbRole.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(False)
        self.cbRole.setFont(font)
        self.cbRole.setObjectName("cbRole")
        self.cbRole.addItem("")
        self.cbRole.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.cbRole)
        self.btnPrimary = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnPrimary.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnPrimary.setFont(font)
        self.btnPrimary.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPrimary.setMouseTracking(False)
        self.btnPrimary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnPrimary.setObjectName("btnPrimary")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                  self.btnPrimary)

        self.retranslateUi(dgUser)
        QtCore.QMetaObject.connectSlotsByName(dgUser)

    def retranslateUi(self, dgUser):
        _translate = QtCore.QCoreApplication.translate
        dgUser.setWindowTitle(_translate("dgUser", "Dialog"))
        self.lblUserID.setText(_translate("dgUser", "userID"))
        self.txtUserID.setPlaceholderText(_translate("dgUser", "userID"))
        self.lblUsername.setText(_translate("dgUser", "Username"))
        self.txtUsername.setPlaceholderText(_translate("dgUser", "Username"))
        self.lblPassword.setText(_translate("dgUser", "Password"))
        self.txtPassword.setPlaceholderText(_translate("dgUser", "Password"))
        self.lblRole.setText(_translate("dgUser", "Role"))
        self.cbRole.setItemText(0, _translate("dgUser", "ADMIN"))
        self.cbRole.setItemText(1, _translate("dgUser", "STAFF"))
        self.btnPrimary.setText(_translate("dgUser", "ADD"))

        ##### CUSTOM #####

        self.clearForm()
        if self._userID != '':
            self.txtUserID.setText(self._userID)
            self.txtUsername.setText(self._username)
            self.txtPassword.setText(self._password)
            self.cbRole.setCurrentIndex(eval(self._role))
            self._ACTION = "UPDATE"
        else:
            self._ACTION = "ADD"
            self.lblUserID.setVisible(False)
            self.txtUserID.setVisible(False)

        self.btnPrimary.setText(self._ACTION)
        self.btnPrimary.clicked.connect(self.actionClicked)

    def actionClicked(self):
        self._userID = self.txtUserID.toPlainText()
        self._username = self.txtUsername.toPlainText()
        self._password = self.txtPassword.toPlainText()
        self._role = self.cbRole.currentIndex()

        if self._username != '' and self._password != '':
            if self._ACTION == "ADD":
                dbUser.newUser(self._username, self._password, self._role)
                msg = self.msgBox()
                msg.setText(f"New user '{self._username}' Added!")
                msg.exec_()
                self.clearForm()
            else:
                dbUser.updateUser(self._userID, self._username, self._password,
                                  self._role)
                msg = self.msgBox()
                msg.setText(
                    f"Update successful!\nUser with userID={self._userID} ")
                msg.exec_()
            self.dgUser.hide()
        else:
            msg = self.msgBox()
            msg.setText("Please fill up the form!")
            msg.exec_()

    def msgBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sanction Management System - User")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        return msg

    def clearForm(self):
        self.txtUserID.setText('')
        self.txtUsername.setText('')
        self.txtPassword.setText('')
