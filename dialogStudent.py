# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogStudent.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import DB.Student as dbStudent
import ICONS.resource_rc


class Ui_dgStud(object):
    def __init__(self, student):
        self._student = student

    def setupUi(self, dgStud):
        self.dgStudent = dgStud
        dgStud.setObjectName("dgStud")
        dgStud.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dgStud.sizePolicy().hasHeightForWidth())
        dgStud.setSizePolicy(sizePolicy)
        dgStud.setMinimumSize(QtCore.QSize(800, 600))
        dgStud.setMaximumSize(QtCore.QSize(800, 600))
        dgStud.setStyleSheet("QDialog, QFormLayout, QLabel{\n"
                             "font-family:\'Open Sans\';\n"
                             "font-size:12pt;\n"
                             "background-color: rgba(0,238,191,1);\n"
                             "color:white;\n"
                             "}\n"
                             "QTextEdit, KDateComboBox{\n"
                             "font-family:\'Open Sans\';\n"
                             "font-size:12pt;\n"
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
        dgStud.setModal(False)
        self.gridLayoutWidget = QtWidgets.QWidget(dgStud)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(22, 22, 22, 22)
        self.gridLayout_2.setSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCourse = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblCourse.setObjectName("lblCourse")
        self.gridLayout_2.addWidget(self.lblCourse, 2, 3, 1, 1)
        self.txtCourse = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtCourse.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtCourse.setFont(font)
        self.txtCourse.setTabChangesFocus(True)
        self.txtCourse.setObjectName("txtCourse")
        self.gridLayout_2.addWidget(self.txtCourse, 2, 4, 1, 1)
        self.txtXTName = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtXTName.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtXTName.setFont(font)
        self.txtXTName.setTabChangesFocus(True)
        self.txtXTName.setTabStopDistance(20.0)
        self.txtXTName.setObjectName("txtXTName")
        self.gridLayout_2.addWidget(self.txtXTName, 4, 2, 1, 1)
        self.txtLName = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtLName.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtLName.setFont(font)
        self.txtLName.setTabChangesFocus(True)
        self.txtLName.setTabStopDistance(20.0)
        self.txtLName.setObjectName("txtLName")
        self.gridLayout_2.addWidget(self.txtLName, 3, 2, 1, 1)
        self.txtMName = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtMName.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtMName.setFont(font)
        self.txtMName.setTabChangesFocus(True)
        self.txtMName.setTabStopDistance(20.0)
        self.txtMName.setObjectName("txtMName")
        self.gridLayout_2.addWidget(self.txtMName, 2, 2, 1, 1)
        self.txtContactNo = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtContactNo.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtContactNo.setFont(font)
        self.txtContactNo.setTabChangesFocus(True)
        self.txtContactNo.setObjectName("txtContactNo")
        self.gridLayout_2.addWidget(self.txtContactNo, 0, 4, 1, 1)
        self.btnCancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCancel.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setMouseTracking(False)
        self.btnCancel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout_2.addWidget(self.btnCancel, 5, 3, 1, 1)
        self.txtEmail = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtEmail.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtEmail.setFont(font)
        self.txtEmail.setTabChangesFocus(True)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout_2.addWidget(self.txtEmail, 1, 4, 1, 1)
        self.lblEmail = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout_2.addWidget(self.lblEmail, 1, 3, 1, 1)
        self.dtDOB = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dtDOB.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(True)
        self.dtDOB.setFont(font)
        self.dtDOB.setObjectName("dtDOB")
        self.gridLayout_2.addWidget(self.dtDOB, 5, 2, 1, 1)
        self.btnPrimary = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnPrimary.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnPrimary.setFont(font)
        self.btnPrimary.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPrimary.setMouseTracking(False)
        self.btnPrimary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnPrimary.setObjectName("btnPrimary")
        self.gridLayout_2.addWidget(self.btnPrimary, 5, 4, 1, 1)
        self.lblFName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblFName.setObjectName("lblFName")
        self.gridLayout_2.addWidget(self.lblFName, 1, 0, 1, 1)
        self.lblSection = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSection.setObjectName("lblSection")
        self.gridLayout_2.addWidget(self.lblSection, 3, 3, 1, 1)
        self.lblXTName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblXTName.setObjectName("lblXTName")
        self.gridLayout_2.addWidget(self.lblXTName, 4, 0, 1, 1)
        self.txtSchoolYear = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtSchoolYear.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtSchoolYear.setFont(font)
        self.txtSchoolYear.setTabChangesFocus(True)
        self.txtSchoolYear.setObjectName("txtSchoolYear")
        self.gridLayout_2.addWidget(self.txtSchoolYear, 4, 4, 1, 1)
        self.txtFName = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtFName.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtFName.setFont(font)
        self.txtFName.setTabChangesFocus(True)
        self.txtFName.setTabStopDistance(20.0)
        self.txtFName.setObjectName("txtFName")
        self.gridLayout_2.addWidget(self.txtFName, 1, 2, 1, 1)
        self.lblLName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblLName.setObjectName("lblLName")
        self.gridLayout_2.addWidget(self.lblLName, 3, 0, 1, 1)
        self.txtStudentNo = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtStudentNo.setEnabled(False)
        self.txtStudentNo.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtStudentNo.setFont(font)
        self.txtStudentNo.setTabChangesFocus(True)
        self.txtStudentNo.setObjectName("txtStudentNo")
        self.gridLayout_2.addWidget(self.txtStudentNo, 0, 2, 1, 1)
        self.lblContactNo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblContactNo.setObjectName("lblContactNo")
        self.gridLayout_2.addWidget(self.lblContactNo, 0, 3, 1, 1)
        self.lblDOB = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblDOB.setObjectName("lblDOB")
        self.gridLayout_2.addWidget(self.lblDOB, 5, 0, 1, 1)
        self.lblMName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblMName.setObjectName("lblMName")
        self.gridLayout_2.addWidget(self.lblMName, 2, 0, 1, 1)
        self.txtSection = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.txtSection.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setItalic(False)
        self.txtSection.setFont(font)
        self.txtSection.setTabChangesFocus(True)
        self.txtSection.setObjectName("txtSection")
        self.gridLayout_2.addWidget(self.txtSection, 3, 4, 1, 1)
        self.lblSchoolYear = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSchoolYear.setObjectName("lblSchoolYear")
        self.gridLayout_2.addWidget(self.lblSchoolYear, 4, 3, 1, 1)
        self.lblStudentNo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblStudentNo.setObjectName("lblStudentNo")
        self.gridLayout_2.addWidget(self.lblStudentNo, 0, 0, 1, 1)
        self.lblStudentNo.raise_()
        self.txtFName.raise_()
        self.lblFName.raise_()
        self.txtMName.raise_()
        self.lblMName.raise_()
        self.lblLName.raise_()
        self.txtLName.raise_()
        self.lblXTName.raise_()
        self.txtXTName.raise_()
        self.lblEmail.raise_()
        self.lblContactNo.raise_()
        self.lblDOB.raise_()
        self.lblCourse.raise_()
        self.lblSection.raise_()
        self.lblSchoolYear.raise_()
        self.btnPrimary.raise_()
        self.btnCancel.raise_()
        self.txtContactNo.raise_()
        self.txtEmail.raise_()
        self.txtCourse.raise_()
        self.txtSection.raise_()
        self.txtSchoolYear.raise_()
        self.txtStudentNo.raise_()
        self.dtDOB.raise_()

        self.retranslateUi(dgStud)
        QtCore.QMetaObject.connectSlotsByName(dgStud)
        dgStud.setTabOrder(self.txtStudentNo, self.txtFName)
        dgStud.setTabOrder(self.txtFName, self.txtMName)
        dgStud.setTabOrder(self.txtMName, self.txtLName)
        dgStud.setTabOrder(self.txtLName, self.txtXTName)
        dgStud.setTabOrder(self.txtXTName, self.dtDOB)
        dgStud.setTabOrder(self.dtDOB, self.txtContactNo)
        dgStud.setTabOrder(self.txtContactNo, self.txtEmail)
        dgStud.setTabOrder(self.txtEmail, self.txtCourse)
        dgStud.setTabOrder(self.txtCourse, self.txtSection)
        dgStud.setTabOrder(self.txtSection, self.txtSchoolYear)
        dgStud.setTabOrder(self.txtSchoolYear, self.btnPrimary)
        dgStud.setTabOrder(self.btnPrimary, self.btnCancel)

    def retranslateUi(self, dgStud):
        _translate = QtCore.QCoreApplication.translate
        dgStud.setWindowTitle(_translate("dgStud", "Dialog"))
        self.lblCourse.setText(_translate("dgStud", "Course"))
        self.txtCourse.setPlaceholderText(_translate("dgStud", "Course"))
        self.txtXTName.setPlaceholderText(
            _translate("dgStud", "Extension Name (e.g. Sr.)"))
        self.txtLName.setPlaceholderText(_translate("dgStud", "Last Name"))
        self.txtMName.setPlaceholderText(_translate("dgStud", "Middle Name"))
        self.txtContactNo.setPlaceholderText(_translate("dgStud", "ContactNo"))
        self.btnCancel.setText(_translate("dgStud", "CANCEL"))
        self.txtEmail.setPlaceholderText(_translate("dgStud", "Email"))
        self.lblEmail.setText(_translate("dgStud", "Email"))
        self.btnPrimary.setText(_translate("dgStud", "ADD"))
        self.lblFName.setText(_translate("dgStud", "First Name"))
        self.lblSection.setText(_translate("dgStud", "Section"))
        self.lblXTName.setText(_translate("dgStud", "Extension Name"))
        self.txtSchoolYear.setPlaceholderText(
            _translate("dgStud", "School Year"))
        self.txtFName.setPlaceholderText(_translate("dgStud", "First Name"))
        self.lblLName.setText(_translate("dgStud", "Last Name"))
        self.txtStudentNo.setPlaceholderText(_translate("dgStud", "StudentNo"))
        self.lblContactNo.setText(_translate("dgStud", "Contact No."))
        self.dtDOB.setDisplayFormat(_translate("dgStud", "yyyy-MM-dd"))
        self.lblDOB.setText(_translate("dgStud",
                                       "Date of Birth\n(YYYY-MM-DD)"))
        self.lblMName.setText(_translate("dgStud", "Middle Name"))
        self.txtSection.setPlaceholderText(_translate("dgStud", "Section"))
        self.lblSchoolYear.setText(_translate("dgStud", "School Year"))
        self.lblStudentNo.setText(_translate("dgStud", "StudentNo"))

        ##### CUSTOM #####
        self.btnCancel.clicked.connect(self.confirmExit)

        if self._student != []:
            self._studentNo = self._student[0]
            self._student = []
            _student = dbStudent.getStudentByNo(self._studentNo)

            self._ACTION = "UPDATE"
            self.txtStudentNo.setEnabled(False)
            self.txtStudentNo.setText(_student[0][0])
            self.txtFName.setText(_student[0][1])
            self.txtMName.setText(_student[0][2])
            self.txtLName.setText(_student[0][3])
            self.txtXTName.setText(_student[0][4])
            self.txtContactNo.setText(_student[0][5])
            self.txtEmail.setText(_student[0][6])
            self.dtDOB.setDate(_student[0][8])
            self.txtCourse.setText(_student[0][9])
            self.txtSection.setText(_student[0][10])
            self.txtSchoolYear.setText(str(_student[0][11]))
        else:
            self._ACTION = "ADD"
            self.txtStudentNo.setEnabled(True)

        self.btnPrimary.setText(self._ACTION)
        self.btnPrimary.clicked.connect(self.actionClicked)

    def actionClicked(self):
        self._StudentNo = self.txtStudentNo.toPlainText()
        self._FName = self.txtFName.toPlainText()
        self._MName = self.txtMName.toPlainText()
        self._LName = self.txtLName.toPlainText()
        self._XTName = self.txtXTName.toPlainText()
        self._ContactNo = self.txtContactNo.toPlainText()
        self._Email = self.txtEmail.toPlainText()
        self._DOB = self.dtDOB.date()
        self._Course = self.txtCourse.toPlainText()
        self._Section = self.txtSection.toPlainText()
        self._SchoolYear = self.txtSchoolYear.toPlainText()

        if self._StudentNo != '':
            if self._ACTION == "ADD":
                msg = self.msgBox()
                if dbStudent.getStudentByNo(self._StudentNo) is None:
                    dbStudent.newStudent(self._StudentNo, self._FName,
                                         self._MName, self._LName,
                                         self._XTName, self._ContactNo,
                                         self._Email,
                                         self._DOB.toString("yyyy-MM-dd"),
                                         self._Course, self._Section,
                                         self._SchoolYear)
                    msg.setText(
                        f"New Sudent Added!\nStudent with StudentNo='{self._studentNo}' "
                    )
                    msg.exec_()
                    self.dgStudent.hide()
                else:
                    msg.setText(f"USER ALREADY EXIST!")
                    msg.setIcon(QMessageBox.Warning)
            else:
                dbUser.updateUser(self._StudentNo, self._FName, self._MName,
                                  self._LName, self._XTName,
                                  self._ContactNo, self._Email,
                                  self._DOB.toString("yyyy-MM-dd"),
                                  self._Course, self._Section,
                                  self._SchoolYear)
                msg = self.msgBox()
                msg.setText(
                    f"Update successful!\nStudent with StudentNo='{self._studentNo}' "
                )
                self.clearForm()
            msg.exec_()

        else:
            msg = self.msgBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please fill up the form!")
            msg.exec_()

    def msgBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sanction Management System - Student")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        return msg

    def confirmExit(self):
        msg = self.msgBox()
        msg.setWindowTitle("Sanction Management System - Confirmation")
        msg.setText("Are you sure you want to cancel transaction?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        ans = msg.exec_()
        if (ans == 16384):
            self.dgStudent.hide()

    def clearForm(self):
        self.txtStudentNo.setEnabled('')
        self.txtStudentNo.setText('')
        self.txtFName.setText('')
        self.txtMName.setText('')
        self.txtLName.setText('')
        self.txtXTName.setText('')
        self.txtContactNo.setText('')
        self.txtEmail.setText('')
        self.dtDOB.setDate('2020-11-19')
        self.txtCourse.setText('')
        self.txtSection.setText('')
        self.txtSchoolYear.setText('')
