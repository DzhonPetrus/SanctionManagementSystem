# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADMIN.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import ICONS.resource_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import connector
import DB.User as dbUser
import DB.Student as dbStudent
from dialogUser import Ui_dgUser
from dialogStudent import Ui_dgStud


class Ui_wndwAdmin(object):
    def __init__(self, wndwLogin, userID):
        self.wndwLogin = wndwLogin
        self._currentUserID = userID

    def setupUi(self, wndwAdmin):
        self.wndwAdmin = wndwAdmin
        wndwAdmin.setObjectName("wndwAdmin")
        wndwAdmin.setWindowModality(QtCore.Qt.NonModal)
        wndwAdmin.resize(1280, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            wndwAdmin.sizePolicy().hasHeightForWidth())
        wndwAdmin.setSizePolicy(sizePolicy)
        wndwAdmin.setMinimumSize(QtCore.QSize(1024, 768))
        wndwAdmin.setMaximumSize(QtCore.QSize(1280, 768))
        wndwAdmin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        wndwAdmin.setStyleSheet(
            "QWidget{\n"
            "    font-family:\'Open Sans\';\n"
            "    font-size:14pt;\n"
            "}\n"
            "\n"
            "QFrame{\n"
            "  background-color: rgb(255,255,255);\n"
            "  color: black;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "  font-weight:bold;\n"
            "  padding: 14px 20px;\n"
            "  margin: 8px 0;\n"
            "  border: none;\n"
            "  width: 100%;\n"
            "  background-color: rgb(255,255,255);\n"
            "  color: rgba(255,200,80,1);\n"
            "    font-size:16pt;\n"
            "}\n"
            "QPushButton:hover {\n"
            "  background-color: rgba(255,200,80,1);\n"
            "  color: white;\n"
            "}\n"
            "#btnUser, #btnService, #btnSanctionLog, #btnSanctionType, #btnSanction, #btnStudent, #btnAddress, #btnLogout {\n"
            "  background-color: rgba(255,200,80,1);\n"
            "  color: white;\n"
            "\n"
            "}\n"
            "\n"
            "#btnUser:hover, #btnService:hover, #btnSanctionLog:hover, #btnSanctionType:hover, #btnSanction:hover, #btnStudent:hover, #btnAddress:hover , #btnLogout:hover{\n"
            "  background-color: rgb(255,255,255);\n"
            "  color: rgba(255,200,80,1)\n"
            "\n"
            "}\n"
            "#btnExit {\n"
            "  background-color: rgba(0,238,191,1);\n"
            "}\n"
            "#btnExit:hover {\n"
            "  background-color: rgba(0,238,191,.8);\n"
            "}\n"
            "#frmLeft, #iconTitle, #lblCurrent, #lblCurrentUser{\n"
            "  background-color:rgba(255,200,80,1);\n"
            "   color: white;\n"
            "   font-size:16pt;\n"
            "}\n"
            "#lblCurrent {font-size:14pt;}\n"
            "\n"
            "#lblTitleUser,#lblTitleService,#lblTitleLog,#lblTitleType,#lblTitleSanction,#lblTitleStudent,#lblTitleAddress{\n"
            "    font-size:24pt;\n"
            "  color:rgba(255,200,80,1);\n"
            "}\n"
            "\n"
            "#lblTitleMain{\n"
            "  font-size:22pt;\n"
            "  background-color:rgba(255,200,80,1);\n"
            "  color: rgba(171,255,219,1);\n"
            "}\n"
            "\n"
            "QTableView::item:selected, QTableView::item:hover {\n"
            "  background-color:rgba(255,200,80,1);\n"
            "  color: white;\n"
            "}\n"
            "")
        wndwAdmin.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        wndwAdmin.setAnimated(True)
        wndwAdmin.setTabShape(QtWidgets.QTabWidget.Rounded)
        wndwAdmin.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(wndwAdmin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 768))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 768))
        self.centralwidget.setObjectName("centralwidget")
        self.frmLeft = QtWidgets.QFrame(self.centralwidget)
        self.frmLeft.setGeometry(QtCore.QRect(0, 0, 280, 768))
        self.frmLeft.setAutoFillBackground(False)
        self.frmLeft.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmLeft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmLeft.setLineWidth(0)
        self.frmLeft.setObjectName("frmLeft")
        self.btnUser = QtWidgets.QPushButton(self.frmLeft)
        self.btnUser.setGeometry(QtCore.QRect(0, 255, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnUser.setFont(font)
        self.btnUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUser.setMouseTracking(False)
        self.btnUser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnUser.setObjectName("btnUser")
        self.btnService = QtWidgets.QPushButton(self.frmLeft)
        self.btnService.setGeometry(QtCore.QRect(0, 300, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnService.setFont(font)
        self.btnService.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnService.setMouseTracking(False)
        self.btnService.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnService.setObjectName("btnService")
        self.btnSanctionLog = QtWidgets.QPushButton(self.frmLeft)
        self.btnSanctionLog.setGeometry(QtCore.QRect(0, 345, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnSanctionLog.setFont(font)
        self.btnSanctionLog.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSanctionLog.setMouseTracking(False)
        self.btnSanctionLog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSanctionLog.setObjectName("btnSanctionLog")
        self.btnSanctionType = QtWidgets.QPushButton(self.frmLeft)
        self.btnSanctionType.setGeometry(QtCore.QRect(0, 390, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnSanctionType.setFont(font)
        self.btnSanctionType.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSanctionType.setMouseTracking(False)
        self.btnSanctionType.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSanctionType.setObjectName("btnSanctionType")
        self.btnSanction = QtWidgets.QPushButton(self.frmLeft)
        self.btnSanction.setGeometry(QtCore.QRect(0, 435, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnSanction.setFont(font)
        self.btnSanction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSanction.setMouseTracking(False)
        self.btnSanction.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSanction.setObjectName("btnSanction")
        self.btnStudent = QtWidgets.QPushButton(self.frmLeft)
        self.btnStudent.setGeometry(QtCore.QRect(0, 480, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnStudent.setFont(font)
        self.btnStudent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStudent.setMouseTracking(False)
        self.btnStudent.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnStudent.setObjectName("btnStudent")
        self.btnAddress = QtWidgets.QPushButton(self.frmLeft)
        self.btnAddress.setGeometry(QtCore.QRect(0, 520, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnAddress.setFont(font)
        self.btnAddress.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddress.setMouseTracking(False)
        self.btnAddress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAddress.setObjectName("btnAddress")
        self.btnLogout = QtWidgets.QPushButton(self.frmLeft)
        self.btnLogout.setGeometry(QtCore.QRect(0, 700, 280, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnLogout.setFont(font)
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setMouseTracking(False)
        self.btnLogout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnLogout.setObjectName("btnLogout")
        self.lblTitleMain = QtWidgets.QLabel(self.frmLeft)
        self.lblTitleMain.setGeometry(QtCore.QRect(110, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleMain.setFont(font)
        self.lblTitleMain.setScaledContents(False)
        self.lblTitleMain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitleMain.setWordWrap(True)
        self.lblTitleMain.setObjectName("lblTitleMain")
        self.iconTitle = QtWidgets.QLabel(self.frmLeft)
        self.iconTitle.setGeometry(QtCore.QRect(20, 10, 111, 101))
        self.iconTitle.setAutoFillBackground(False)
        self.iconTitle.setText("")
        self.iconTitle.setPixmap(QtGui.QPixmap(":/ICONS/browser.png"))
        self.iconTitle.setScaledContents(True)
        self.iconTitle.setObjectName("iconTitle")
        self.lblCurrentUser = QtWidgets.QLabel(self.frmLeft)
        self.lblCurrentUser.setGeometry(QtCore.QRect(40, 169, 241, 41))
        self.lblCurrentUser.setAlignment(QtCore.Qt.AlignLeading
                                         | QtCore.Qt.AlignLeft
                                         | QtCore.Qt.AlignTop)
        self.lblCurrentUser.setWordWrap(True)
        self.lblCurrentUser.setObjectName("lblCurrentUser")
        self.lblCurrent = QtWidgets.QLabel(self.frmLeft)
        self.lblCurrent.setGeometry(QtCore.QRect(10, 140, 241, 31))
        self.lblCurrent.setObjectName("lblCurrent")
        self.btnUser.raise_()
        self.btnService.raise_()
        self.btnSanctionLog.raise_()
        self.btnSanctionType.raise_()
        self.btnSanction.raise_()
        self.btnStudent.raise_()
        self.btnAddress.raise_()
        self.btnLogout.raise_()
        self.iconTitle.raise_()
        self.lblTitleMain.raise_()
        self.lblCurrentUser.raise_()
        self.lblCurrent.raise_()
        self.frmAddress = QtWidgets.QFrame(self.centralwidget)
        self.frmAddress.setGeometry(QtCore.QRect(279, 0, 1001, 768))
        self.frmAddress.setAutoFillBackground(False)
        self.frmAddress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmAddress.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmAddress.setObjectName("frmAddress")
        self.txtAddressSearch = QtWidgets.QTextEdit(self.frmAddress)
        self.txtAddressSearch.setGeometry(QtCore.QRect(10, 99, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.txtAddressSearch.setFont(font)
        self.txtAddressSearch.setTabChangesFocus(True)
        self.txtAddressSearch.setObjectName("txtAddressSearch")
        self.lblTitleAddress = QtWidgets.QLabel(self.frmAddress)
        self.lblTitleAddress.setGeometry(QtCore.QRect(60, 25, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleAddress.setFont(font)
        self.lblTitleAddress.setObjectName("lblTitleAddress")
        self.btnAddressAdd = QtWidgets.QPushButton(self.frmAddress)
        self.btnAddressAdd.setGeometry(QtCore.QRect(460, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnAddressAdd.setFont(font)
        self.btnAddressAdd.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddressAdd.setMouseTracking(False)
        self.btnAddressAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAddressAdd.setObjectName("btnAddressAdd")
        self.btnAddressUpdate = QtWidgets.QPushButton(self.frmAddress)
        self.btnAddressUpdate.setEnabled(False)
        self.btnAddressUpdate.setGeometry(QtCore.QRect(580, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnAddressUpdate.setFont(font)
        self.btnAddressUpdate.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddressUpdate.setMouseTracking(False)
        self.btnAddressUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAddressUpdate.setObjectName("btnAddressUpdate")
        self.btnAddressDelete = QtWidgets.QPushButton(self.frmAddress)
        self.btnAddressDelete.setEnabled(False)
        self.btnAddressDelete.setGeometry(QtCore.QRect(700, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnAddressDelete.setFont(font)
        self.btnAddressDelete.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddressDelete.setMouseTracking(False)
        self.btnAddressDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAddressDelete.setObjectName("btnAddressDelete")
        self.tblAddress = QtWidgets.QTableWidget(self.frmAddress)
        self.tblAddress.setGeometry(QtCore.QRect(0, 150, 1001, 621))
        self.tblAddress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblAddress.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblAddress.setAutoScrollMargin(20)
        self.tblAddress.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblAddress.setProperty("showDropIndicator", False)
        self.tblAddress.setDragDropOverwriteMode(False)
        self.tblAddress.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblAddress.setAlternatingRowColors(False)
        self.tblAddress.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblAddress.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblAddress.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblAddress.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tblAddress.setShowGrid(True)
        self.tblAddress.setGridStyle(QtCore.Qt.SolidLine)
        self.tblAddress.setWordWrap(True)
        self.tblAddress.setCornerButtonEnabled(False)
        self.tblAddress.setRowCount(20)
        self.tblAddress.setColumnCount(0)
        self.tblAddress.setObjectName("tblAddress")
        self.tblAddress.horizontalHeader().setCascadingSectionResizes(False)
        self.tblAddress.horizontalHeader().setDefaultSectionSize(150)
        self.tblAddress.horizontalHeader().setHighlightSections(False)
        self.tblAddress.horizontalHeader().setSortIndicatorShown(True)
        self.tblAddress.horizontalHeader().setStretchLastSection(True)
        self.tblAddress.verticalHeader().setVisible(False)
        self.tblAddress.verticalHeader().setCascadingSectionResizes(False)
        self.tblAddress.verticalHeader().setSortIndicatorShown(False)
        self.tblAddress.verticalHeader().setStretchLastSection(False)
        self.frmService = QtWidgets.QFrame(self.centralwidget)
        self.frmService.setGeometry(QtCore.QRect(279, 0, 1001, 768))
        self.frmService.setAutoFillBackground(False)
        self.frmService.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmService.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmService.setObjectName("frmService")
        self.txtServiceSearch = QtWidgets.QTextEdit(self.frmService)
        self.txtServiceSearch.setGeometry(QtCore.QRect(10, 99, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.txtServiceSearch.setFont(font)
        self.txtServiceSearch.setTabChangesFocus(True)
        self.txtServiceSearch.setObjectName("txtServiceSearch")
        self.lblTitleService = QtWidgets.QLabel(self.frmService)
        self.lblTitleService.setGeometry(QtCore.QRect(60, 25, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleService.setFont(font)
        self.lblTitleService.setObjectName("lblTitleService")
        self.btnServiceAdd = QtWidgets.QPushButton(self.frmService)
        self.btnServiceAdd.setGeometry(QtCore.QRect(460, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnServiceAdd.setFont(font)
        self.btnServiceAdd.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnServiceAdd.setMouseTracking(False)
        self.btnServiceAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnServiceAdd.setObjectName("btnServiceAdd")
        self.btnServiceUpdate = QtWidgets.QPushButton(self.frmService)
        self.btnServiceUpdate.setEnabled(False)
        self.btnServiceUpdate.setGeometry(QtCore.QRect(580, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnServiceUpdate.setFont(font)
        self.btnServiceUpdate.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnServiceUpdate.setMouseTracking(False)
        self.btnServiceUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnServiceUpdate.setObjectName("btnServiceUpdate")
        self.btnServiceDelete = QtWidgets.QPushButton(self.frmService)
        self.btnServiceDelete.setEnabled(False)
        self.btnServiceDelete.setGeometry(QtCore.QRect(700, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnServiceDelete.setFont(font)
        self.btnServiceDelete.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnServiceDelete.setMouseTracking(False)
        self.btnServiceDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnServiceDelete.setObjectName("btnServiceDelete")
        self.tblService = QtWidgets.QTableWidget(self.frmService)
        self.tblService.setGeometry(QtCore.QRect(0, 150, 1001, 621))
        self.tblService.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblService.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblService.setAutoScrollMargin(20)
        self.tblService.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblService.setProperty("showDropIndicator", False)
        self.tblService.setDragDropOverwriteMode(False)
        self.tblService.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblService.setAlternatingRowColors(False)
        self.tblService.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblService.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblService.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblService.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tblService.setShowGrid(True)
        self.tblService.setGridStyle(QtCore.Qt.SolidLine)
        self.tblService.setWordWrap(True)
        self.tblService.setCornerButtonEnabled(False)
        self.tblService.setRowCount(20)
        self.tblService.setColumnCount(0)
        self.tblService.setObjectName("tblService")
        self.tblService.horizontalHeader().setCascadingSectionResizes(False)
        self.tblService.horizontalHeader().setDefaultSectionSize(150)
        self.tblService.horizontalHeader().setHighlightSections(False)
        self.tblService.horizontalHeader().setSortIndicatorShown(True)
        self.tblService.horizontalHeader().setStretchLastSection(True)
        self.tblService.verticalHeader().setVisible(False)
        self.tblService.verticalHeader().setCascadingSectionResizes(False)
        self.tblService.verticalHeader().setSortIndicatorShown(False)
        self.tblService.verticalHeader().setStretchLastSection(False)
        self.frmStudent = QtWidgets.QFrame(self.centralwidget)
        self.frmStudent.setGeometry(QtCore.QRect(279, 0, 1001, 768))
        self.frmStudent.setAutoFillBackground(False)
        self.frmStudent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmStudent.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmStudent.setObjectName("frmStudent")
        self.txtStudentSearch = QtWidgets.QTextEdit(self.frmStudent)
        self.txtStudentSearch.setGeometry(QtCore.QRect(10, 99, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.txtStudentSearch.setFont(font)
        self.txtStudentSearch.setTabChangesFocus(True)
        self.txtStudentSearch.setObjectName("txtStudentSearch")
        self.lblTitleStudent = QtWidgets.QLabel(self.frmStudent)
        self.lblTitleStudent.setGeometry(QtCore.QRect(60, 25, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleStudent.setFont(font)
        self.lblTitleStudent.setObjectName("lblTitleStudent")
        self.btnStudentAdd = QtWidgets.QPushButton(self.frmStudent)
        self.btnStudentAdd.setGeometry(QtCore.QRect(460, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnStudentAdd.setFont(font)
        self.btnStudentAdd.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStudentAdd.setMouseTracking(False)
        self.btnStudentAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnStudentAdd.setObjectName("btnStudentAdd")
        self.btnStudentUpdate = QtWidgets.QPushButton(self.frmStudent)
        self.btnStudentUpdate.setEnabled(False)
        self.btnStudentUpdate.setGeometry(QtCore.QRect(580, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnStudentUpdate.setFont(font)
        self.btnStudentUpdate.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStudentUpdate.setMouseTracking(False)
        self.btnStudentUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnStudentUpdate.setObjectName("btnStudentUpdate")
        self.btnStudentDelete = QtWidgets.QPushButton(self.frmStudent)
        self.btnStudentDelete.setEnabled(False)
        self.btnStudentDelete.setGeometry(QtCore.QRect(700, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnStudentDelete.setFont(font)
        self.btnStudentDelete.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStudentDelete.setMouseTracking(False)
        self.btnStudentDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnStudentDelete.setObjectName("btnStudentDelete")
        self.tblStudent = QtWidgets.QTableWidget(self.frmStudent)
        self.tblStudent.setGeometry(QtCore.QRect(0, 150, 1001, 621))
        self.tblStudent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblStudent.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblStudent.setAutoScrollMargin(20)
        self.tblStudent.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblStudent.setProperty("showDropIndicator", False)
        self.tblStudent.setDragDropOverwriteMode(False)
        self.tblStudent.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblStudent.setAlternatingRowColors(False)
        self.tblStudent.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblStudent.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblStudent.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblStudent.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tblStudent.setShowGrid(True)
        self.tblStudent.setGridStyle(QtCore.Qt.SolidLine)
        self.tblStudent.setWordWrap(True)
        self.tblStudent.setCornerButtonEnabled(False)
        self.tblStudent.setRowCount(20)
        self.tblStudent.setColumnCount(0)
        self.tblStudent.setObjectName("tblStudent")
        self.tblStudent.horizontalHeader().setCascadingSectionResizes(False)
        self.tblStudent.horizontalHeader().setDefaultSectionSize(150)
        self.tblStudent.horizontalHeader().setHighlightSections(False)
        self.tblStudent.horizontalHeader().setSortIndicatorShown(True)
        self.tblStudent.horizontalHeader().setStretchLastSection(True)
        self.tblStudent.verticalHeader().setVisible(False)
        self.tblStudent.verticalHeader().setCascadingSectionResizes(False)
        self.tblStudent.verticalHeader().setSortIndicatorShown(False)
        self.tblStudent.verticalHeader().setStretchLastSection(False)
        self.frmSanction = QtWidgets.QFrame(self.centralwidget)
        self.frmSanction.setGeometry(QtCore.QRect(279, 0, 1001, 768))
        self.frmSanction.setAutoFillBackground(False)
        self.frmSanction.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmSanction.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmSanction.setObjectName("frmSanction")
        self.txtSanctionSearch = QtWidgets.QTextEdit(self.frmSanction)
        self.txtSanctionSearch.setGeometry(QtCore.QRect(10, 99, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.txtSanctionSearch.setFont(font)
        self.txtSanctionSearch.setTabChangesFocus(True)
        self.txtSanctionSearch.setObjectName("txtSanctionSearch")
        self.lblTitleSanction = QtWidgets.QLabel(self.frmSanction)
        self.lblTitleSanction.setGeometry(QtCore.QRect(60, 25, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleSanction.setFont(font)
        self.lblTitleSanction.setObjectName("lblTitleSanction")
        self.btnSanctionAdd = QtWidgets.QPushButton(self.frmSanction)
        self.btnSanctionAdd.setGeometry(QtCore.QRect(460, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnSanctionAdd.setFont(font)
        self.btnSanctionAdd.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSanctionAdd.setMouseTracking(False)
        self.btnSanctionAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSanctionAdd.setObjectName("btnSanctionAdd")
        self.btnSanctionUpdate = QtWidgets.QPushButton(self.frmSanction)
        self.btnSanctionUpdate.setEnabled(False)
        self.btnSanctionUpdate.setGeometry(QtCore.QRect(580, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnSanctionUpdate.setFont(font)
        self.btnSanctionUpdate.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSanctionUpdate.setMouseTracking(False)
        self.btnSanctionUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSanctionUpdate.setObjectName("btnSanctionUpdate")
        self.btnSanctionDelete = QtWidgets.QPushButton(self.frmSanction)
        self.btnSanctionDelete.setEnabled(False)
        self.btnSanctionDelete.setGeometry(QtCore.QRect(700, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnSanctionDelete.setFont(font)
        self.btnSanctionDelete.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSanctionDelete.setMouseTracking(False)
        self.btnSanctionDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSanctionDelete.setObjectName("btnSanctionDelete")
        self.tblSanction = QtWidgets.QTableWidget(self.frmSanction)
        self.tblSanction.setGeometry(QtCore.QRect(0, 150, 1001, 621))
        self.tblSanction.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblSanction.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblSanction.setAutoScrollMargin(20)
        self.tblSanction.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblSanction.setProperty("showDropIndicator", False)
        self.tblSanction.setDragDropOverwriteMode(False)
        self.tblSanction.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblSanction.setAlternatingRowColors(False)
        self.tblSanction.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblSanction.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblSanction.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblSanction.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tblSanction.setShowGrid(True)
        self.tblSanction.setGridStyle(QtCore.Qt.SolidLine)
        self.tblSanction.setWordWrap(True)
        self.tblSanction.setCornerButtonEnabled(False)
        self.tblSanction.setRowCount(20)
        self.tblSanction.setColumnCount(0)
        self.tblSanction.setObjectName("tblSanction")
        self.tblSanction.horizontalHeader().setCascadingSectionResizes(False)
        self.tblSanction.horizontalHeader().setDefaultSectionSize(150)
        self.tblSanction.horizontalHeader().setHighlightSections(False)
        self.tblSanction.horizontalHeader().setSortIndicatorShown(True)
        self.tblSanction.horizontalHeader().setStretchLastSection(True)
        self.tblSanction.verticalHeader().setVisible(False)
        self.tblSanction.verticalHeader().setCascadingSectionResizes(False)
        self.tblSanction.verticalHeader().setSortIndicatorShown(False)
        self.tblSanction.verticalHeader().setStretchLastSection(False)
        self.frmSanctionLog = QtWidgets.QFrame(self.centralwidget)
        self.frmSanctionLog.setGeometry(QtCore.QRect(279, 0, 1001, 768))
        self.frmSanctionLog.setAutoFillBackground(False)
        self.frmSanctionLog.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmSanctionLog.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmSanctionLog.setObjectName("frmSanctionLog")
        self.txtLogSearch = QtWidgets.QTextEdit(self.frmSanctionLog)
        self.txtLogSearch.setGeometry(QtCore.QRect(10, 99, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.txtLogSearch.setFont(font)
        self.txtLogSearch.setTabChangesFocus(True)
        self.txtLogSearch.setObjectName("txtLogSearch")
        self.lblTitleLog = QtWidgets.QLabel(self.frmSanctionLog)
        self.lblTitleLog.setGeometry(QtCore.QRect(60, 25, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleLog.setFont(font)
        self.lblTitleLog.setObjectName("lblTitleLog")
        self.btnLogAdd = QtWidgets.QPushButton(self.frmSanctionLog)
        self.btnLogAdd.setGeometry(QtCore.QRect(460, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnLogAdd.setFont(font)
        self.btnLogAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogAdd.setMouseTracking(False)
        self.btnLogAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnLogAdd.setObjectName("btnLogAdd")
        self.btnLogUpdate = QtWidgets.QPushButton(self.frmSanctionLog)
        self.btnLogUpdate.setEnabled(False)
        self.btnLogUpdate.setGeometry(QtCore.QRect(580, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnLogUpdate.setFont(font)
        self.btnLogUpdate.setCursor(QtGui.QCursor(
            QtCore.Qt.PointingHandCursor))
        self.btnLogUpdate.setMouseTracking(False)
        self.btnLogUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnLogUpdate.setObjectName("btnLogUpdate")
        self.btnLogDelete = QtWidgets.QPushButton(self.frmSanctionLog)
        self.btnLogDelete.setEnabled(False)
        self.btnLogDelete.setGeometry(QtCore.QRect(700, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnLogDelete.setFont(font)
        self.btnLogDelete.setCursor(QtGui.QCursor(
            QtCore.Qt.PointingHandCursor))
        self.btnLogDelete.setMouseTracking(False)
        self.btnLogDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnLogDelete.setObjectName("btnLogDelete")
        self.tblLog = QtWidgets.QTableWidget(self.frmSanctionLog)
        self.tblLog.setGeometry(QtCore.QRect(0, 150, 1001, 621))
        self.tblLog.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblLog.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblLog.setAutoScrollMargin(20)
        self.tblLog.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblLog.setProperty("showDropIndicator", False)
        self.tblLog.setDragDropOverwriteMode(False)
        self.tblLog.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblLog.setAlternatingRowColors(False)
        self.tblLog.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblLog.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblLog.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblLog.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tblLog.setShowGrid(True)
        self.tblLog.setGridStyle(QtCore.Qt.SolidLine)
        self.tblLog.setWordWrap(True)
        self.tblLog.setCornerButtonEnabled(False)
        self.tblLog.setRowCount(20)
        self.tblLog.setColumnCount(0)
        self.tblLog.setObjectName("tblLog")
        self.tblLog.horizontalHeader().setCascadingSectionResizes(False)
        self.tblLog.horizontalHeader().setDefaultSectionSize(150)
        self.tblLog.horizontalHeader().setHighlightSections(False)
        self.tblLog.horizontalHeader().setSortIndicatorShown(True)
        self.tblLog.horizontalHeader().setStretchLastSection(True)
        self.tblLog.verticalHeader().setVisible(False)
        self.tblLog.verticalHeader().setCascadingSectionResizes(False)
        self.tblLog.verticalHeader().setSortIndicatorShown(False)
        self.tblLog.verticalHeader().setStretchLastSection(False)
        self.frmSanctionType = QtWidgets.QFrame(self.centralwidget)
        self.frmSanctionType.setGeometry(QtCore.QRect(279, 0, 1001, 768))
        self.frmSanctionType.setAutoFillBackground(False)
        self.frmSanctionType.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmSanctionType.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmSanctionType.setObjectName("frmSanctionType")
        self.txtTypeSearch = QtWidgets.QTextEdit(self.frmSanctionType)
        self.txtTypeSearch.setGeometry(QtCore.QRect(10, 99, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.txtTypeSearch.setFont(font)
        self.txtTypeSearch.setTabChangesFocus(True)
        self.txtTypeSearch.setObjectName("txtTypeSearch")
        self.lblTitleType = QtWidgets.QLabel(self.frmSanctionType)
        self.lblTitleType.setGeometry(QtCore.QRect(60, 25, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleType.setFont(font)
        self.lblTitleType.setObjectName("lblTitleType")
        self.btnTypeAdd = QtWidgets.QPushButton(self.frmSanctionType)
        self.btnTypeAdd.setGeometry(QtCore.QRect(460, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnTypeAdd.setFont(font)
        self.btnTypeAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTypeAdd.setMouseTracking(False)
        self.btnTypeAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnTypeAdd.setObjectName("btnTypeAdd")
        self.btnTypeUpdate = QtWidgets.QPushButton(self.frmSanctionType)
        self.btnTypeUpdate.setEnabled(False)
        self.btnTypeUpdate.setGeometry(QtCore.QRect(580, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnTypeUpdate.setFont(font)
        self.btnTypeUpdate.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTypeUpdate.setMouseTracking(False)
        self.btnTypeUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnTypeUpdate.setObjectName("btnTypeUpdate")
        self.btnTypeDelete = QtWidgets.QPushButton(self.frmSanctionType)
        self.btnTypeDelete.setEnabled(False)
        self.btnTypeDelete.setGeometry(QtCore.QRect(700, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnTypeDelete.setFont(font)
        self.btnTypeDelete.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTypeDelete.setMouseTracking(False)
        self.btnTypeDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnTypeDelete.setObjectName("btnTypeDelete")
        self.tblType = QtWidgets.QTableWidget(self.frmSanctionType)
        self.tblType.setGeometry(QtCore.QRect(0, 150, 1001, 621))
        self.tblType.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblType.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblType.setAutoScrollMargin(20)
        self.tblType.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblType.setProperty("showDropIndicator", False)
        self.tblType.setDragDropOverwriteMode(False)
        self.tblType.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblType.setAlternatingRowColors(False)
        self.tblType.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblType.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblType.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblType.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tblType.setShowGrid(True)
        self.tblType.setGridStyle(QtCore.Qt.SolidLine)
        self.tblType.setWordWrap(True)
        self.tblType.setCornerButtonEnabled(False)
        self.tblType.setRowCount(20)
        self.tblType.setColumnCount(0)
        self.tblType.setObjectName("tblType")
        self.tblType.horizontalHeader().setCascadingSectionResizes(False)
        self.tblType.horizontalHeader().setDefaultSectionSize(150)
        self.tblType.horizontalHeader().setHighlightSections(False)
        self.tblType.horizontalHeader().setSortIndicatorShown(True)
        self.tblType.horizontalHeader().setStretchLastSection(True)
        self.tblType.verticalHeader().setVisible(False)
        self.tblType.verticalHeader().setCascadingSectionResizes(False)
        self.tblType.verticalHeader().setSortIndicatorShown(False)
        self.tblType.verticalHeader().setStretchLastSection(False)
        self.frmUser = QtWidgets.QFrame(self.centralwidget)
        self.frmUser.setGeometry(QtCore.QRect(279, 0, 1001, 768))
        self.frmUser.setAutoFillBackground(False)
        self.frmUser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmUser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmUser.setObjectName("frmUser")
        self.txtUserSearch = QtWidgets.QTextEdit(self.frmUser)
        self.txtUserSearch.setGeometry(QtCore.QRect(10, 99, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.txtUserSearch.setFont(font)
        self.txtUserSearch.setTabChangesFocus(True)
        self.txtUserSearch.setObjectName("txtUserSearch")
        self.lblTitleUser = QtWidgets.QLabel(self.frmUser)
        self.lblTitleUser.setGeometry(QtCore.QRect(60, 25, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleUser.setFont(font)
        self.lblTitleUser.setObjectName("lblTitleUser")
        self.btnUserAdd = QtWidgets.QPushButton(self.frmUser)
        self.btnUserAdd.setGeometry(QtCore.QRect(460, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnUserAdd.setFont(font)
        self.btnUserAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUserAdd.setMouseTracking(False)
        self.btnUserAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnUserAdd.setObjectName("btnUserAdd")
        self.btnUserUpdate = QtWidgets.QPushButton(self.frmUser)
        self.btnUserUpdate.setEnabled(False)
        self.btnUserUpdate.setGeometry(QtCore.QRect(580, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnUserUpdate.setFont(font)
        self.btnUserUpdate.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUserUpdate.setMouseTracking(False)
        self.btnUserUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnUserUpdate.setObjectName("btnUserUpdate")
        self.btnUserDelete = QtWidgets.QPushButton(self.frmUser)
        self.btnUserDelete.setEnabled(False)
        self.btnUserDelete.setGeometry(QtCore.QRect(700, 60, 125, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnUserDelete.setFont(font)
        self.btnUserDelete.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUserDelete.setMouseTracking(False)
        self.btnUserDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnUserDelete.setObjectName("btnUserDelete")
        self.tblUser = QtWidgets.QTableWidget(self.frmUser)
        self.tblUser.setGeometry(QtCore.QRect(0, 150, 1001, 621))
        self.tblUser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblUser.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblUser.setAutoScrollMargin(20)
        self.tblUser.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblUser.setProperty("showDropIndicator", False)
        self.tblUser.setDragDropOverwriteMode(False)
        self.tblUser.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblUser.setAlternatingRowColors(False)
        self.tblUser.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblUser.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblUser.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tblUser.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tblUser.setShowGrid(True)
        self.tblUser.setGridStyle(QtCore.Qt.SolidLine)
        self.tblUser.setWordWrap(True)
        self.tblUser.setCornerButtonEnabled(False)
        self.tblUser.setRowCount(20)
        self.tblUser.setColumnCount(0)
        self.tblUser.setObjectName("tblUser")
        self.tblUser.horizontalHeader().setCascadingSectionResizes(False)
        self.tblUser.horizontalHeader().setDefaultSectionSize(150)
        self.tblUser.horizontalHeader().setHighlightSections(False)
        self.tblUser.horizontalHeader().setSortIndicatorShown(True)
        self.tblUser.horizontalHeader().setStretchLastSection(True)
        self.tblUser.verticalHeader().setVisible(False)
        self.tblUser.verticalHeader().setCascadingSectionResizes(False)
        self.tblUser.verticalHeader().setSortIndicatorShown(False)
        self.tblUser.verticalHeader().setStretchLastSection(False)
        self.frmService.raise_()
        self.frmStudent.raise_()
        self.frmSanctionLog.raise_()
        self.frmSanctionType.raise_()
        self.frmSanction.raise_()
        self.frmAddress.raise_()
        self.frmLeft.raise_()
        self.frmUser.raise_()
        wndwAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(wndwAdmin)
        QtCore.QMetaObject.connectSlotsByName(wndwAdmin)

    def retranslateUi(self, wndwAdmin):
        _translate = QtCore.QCoreApplication.translate
        wndwAdmin.setWindowTitle(
            _translate("wndwAdmin", "Sanction Management System - ADMIN"))
        self.btnUser.setText(_translate("wndwAdmin", "USER"))
        self.btnService.setText(_translate("wndwAdmin", "SERVICE"))
        self.btnSanctionLog.setText(_translate("wndwAdmin", "SANCTION LOG"))
        self.btnSanctionType.setText(_translate("wndwAdmin", "SANCTION TYPE"))
        self.btnSanction.setText(_translate("wndwAdmin", "SANCTION"))
        self.btnStudent.setText(_translate("wndwAdmin", "STUDENT"))
        self.btnAddress.setText(_translate("wndwAdmin", "ADDRESS"))
        self.btnLogout.setText(_translate("wndwAdmin", "LOGOUT"))
        self.lblTitleMain.setText(_translate("wndwAdmin", "PUP - SMS"))
        self.lblCurrentUser.setText(_translate("wndwAdmin", "ADMIN"))
        self.lblCurrent.setText(_translate("wndwAdmin", "Logged in as"))
        self.txtAddressSearch.setPlaceholderText(
            _translate("wndwAdmin", "Search by AddressID"))
        self.lblTitleAddress.setText(_translate("wndwAdmin", "ADDRESS"))
        self.btnAddressAdd.setText(_translate("wndwAdmin", "ADD"))
        self.btnAddressUpdate.setText(_translate("wndwAdmin", "UPDATE"))
        self.btnAddressDelete.setText(_translate("wndwAdmin", "DELETE"))
        self.tblAddress.setSortingEnabled(True)
        self.txtServiceSearch.setPlaceholderText(
            _translate("wndwAdmin", "Search by ServiceID"))
        self.lblTitleService.setText(_translate("wndwAdmin", "SERVICE"))
        self.btnServiceAdd.setText(_translate("wndwAdmin", "ADD"))
        self.btnServiceUpdate.setText(_translate("wndwAdmin", "UPDATE"))
        self.btnServiceDelete.setText(_translate("wndwAdmin", "DELETE"))
        self.tblService.setSortingEnabled(True)
        self.txtStudentSearch.setPlaceholderText(
            _translate("wndwAdmin", "Search by StudentNo"))
        self.lblTitleStudent.setText(_translate("wndwAdmin", "STUDENT"))
        self.btnStudentAdd.setText(_translate("wndwAdmin", "ADD"))
        self.btnStudentUpdate.setText(_translate("wndwAdmin", "UPDATE"))
        self.btnStudentDelete.setText(_translate("wndwAdmin", "DELETE"))
        self.tblStudent.setSortingEnabled(True)
        self.txtSanctionSearch.setPlaceholderText(
            _translate("wndwAdmin", "Search by SanctionCode"))
        self.lblTitleSanction.setText(_translate("wndwAdmin", "SANCTION"))
        self.btnSanctionAdd.setText(_translate("wndwAdmin", "ADD"))
        self.btnSanctionUpdate.setText(_translate("wndwAdmin", "UPDATE"))
        self.btnSanctionDelete.setText(_translate("wndwAdmin", "DELETE"))
        self.tblSanction.setSortingEnabled(True)
        self.txtLogSearch.setPlaceholderText(
            _translate("wndwAdmin", "Search by LogID"))
        self.lblTitleLog.setText(_translate("wndwAdmin", "SANCTION LOG"))
        self.btnLogAdd.setText(_translate("wndwAdmin", "ADD"))
        self.btnLogUpdate.setText(_translate("wndwAdmin", "UPDATE"))
        self.btnLogDelete.setText(_translate("wndwAdmin", "DELETE"))
        self.tblLog.setSortingEnabled(True)
        self.txtTypeSearch.setPlaceholderText(
            _translate("wndwAdmin", "Search by TypeID"))
        self.lblTitleType.setText(_translate("wndwAdmin", "SANCTION TYPE"))
        self.btnTypeAdd.setText(_translate("wndwAdmin", "ADD"))
        self.btnTypeUpdate.setText(_translate("wndwAdmin", "UPDATE"))
        self.btnTypeDelete.setText(_translate("wndwAdmin", "DELETE"))
        self.tblType.setSortingEnabled(True)
        self.txtUserSearch.setPlaceholderText(
            _translate("wndwAdmin", "Search by Username"))
        self.lblTitleUser.setText(_translate("wndwAdmin", "USER"))
        self.btnUserAdd.setText(_translate("wndwAdmin", "ADD"))
        self.btnUserUpdate.setText(_translate("wndwAdmin", "UPDATE"))
        self.btnUserDelete.setText(_translate("wndwAdmin", "DELETE"))
        self.tblUser.setSortingEnabled(True)

        # CUSTOM CODE

        self.userClicked()

        self.tblUser.cellClicked.connect(self.tblUserClicked)
        self.btnUser.clicked.connect(self.userClicked)
        self.btnUserAdd.clicked.connect(self.userAdd)
        self.btnUserUpdate.clicked.connect(self.userUpdate)
        self.btnUserDelete.clicked.connect(self.userDelete)

        self.btnAddress.clicked.connect(self.addressClicked)
        self.btnSanction.clicked.connect(self.sanctionClicked)
        self.btnSanctionType.clicked.connect(self.typeClicked)
        self.btnSanctionLog.clicked.connect(self.logClicked)

        self.tblStudent.cellClicked.connect(self.tblStudentClicked)
        self.btnStudent.clicked.connect(self.studentClicked)
        self.btnStudentAdd.clicked.connect(self.studentAdd)
        self.btnStudentUpdate.clicked.connect(self.studentUpdate)
        self.btnStudentDelete.clicked.connect(self.studentDelete)

        self.btnService.clicked.connect(self.serviceClicked)
        self.btnLogout.clicked.connect(self.confirmationLogout)

##############   USER   #######################

    def tblUserClicked(self):
        self.r = self.tblUser.currentRow()
        if (self.tblUser.item(self.r, 0) != None):
            self.btnUserUpdate.setEnabled(True)
            self.btnUserDelete.setEnabled(True)
        else:
            self.btnUserUpdate.setEnabled(False)
            self.btnUserDelete.setEnabled(False)

    def userClicked(self):
        currentUser = dbUser.getUserByID(self._currentUserID)
        self._currentUsername = currentUser[1]
        self.lblCurrentUser.setText("<html><b>" + self._currentUsername +
                                    "</b></html>")
        self.resetFormState()
        self.frmUser.setVisible(True)
        self.btnUser.setEnabled(False)
        users = dbUser.getAllUser()
        if users != None:
            self.tblUser.setColumnCount(4)
            self.tblUser.setHorizontalHeaderLabels(
                ['userID', 'Username', 'Password', 'Role'])
            row = 0

            for user in users:
                _userID = user[0]
                _username = user[1]
                _password = user[2]
                _role = user[3]

                self.tblUser.insertRow(row)
                self.tblUser.setItem(row, 0, QTableWidgetItem(str(_userID)))
                self.tblUser.setItem(row, 1, QTableWidgetItem(_username))
                self.tblUser.setItem(row, 2, QTableWidgetItem(_password))
                self.tblUser.setItem(row, 3, QTableWidgetItem(str(_role)))
                row = row + 1

        else:
            msg = self.msgBox()
            msg.setText("NO USER FOUND")
            msg.exec_()

    def userAdd(self):
        self._userID = ''
        self._username = ''
        self._password = ''
        self._role = 0
        self.dgUser = QtWidgets.QDialog()
        self.dg = Ui_dgUser(self._userID, self._username, self._password,
                            self._role)
        self.dg.setupUi(self.dgUser)
        self.dg.txtUsername.setEnabled(True)
        self.dgUser.show()
        x = self.dgUser.exec_()
        if x == 0:
            self.userClicked()

    def userUpdate(self):
        self._userID = self.tblUser.item(self.r, 0).text()
        self._username = self.tblUser.item(self.r, 1).text()
        self._password = self.tblUser.item(self.r, 2).text()
        self._role = self.tblUser.item(self.r, 3).text()
        self.dgUser = QtWidgets.QDialog()
        self.dg = Ui_dgUser(self._userID, self._username, self._password,
                            self._role)
        self.dg.setupUi(self.dgUser)
        self.dg.txtUsername.setEnabled(False)
        self.dgUser.show()
        x = self.dgUser.exec_()
        if x == 0:
            self.userClicked()

    def userDelete(self):
        self._userID = self.tblUser.item(self.r, 0).text()
        msg = self.confirmationBox()
        msg.setText(
            f"Are you sure you want to Delete User with userID='{self._userID}'?"
        )
        ans = msg.exec_()
        if (ans == 16384):
            dbUser.deleteUser(self._userID)
            info = self.infoBox()
            info.setText(
                f"User with userID='{self._userID}' successfully deleted!")
            info.exec_()
            self.userClicked()

##############   ADDRESS   #######################

    def addressClicked(self):
        self.resetFormState()
        self.frmAddress.setVisible(True)
        self.btnAddress.setEnabled(False)

##############   SANCTION   #######################

    def sanctionClicked(self):
        self.resetFormState()
        self.frmSanction.setVisible(True)
        self.btnSanction.setEnabled(False)

##############   SANCTION TYPE   #######################

    def typeClicked(self):
        self.resetFormState()
        self.frmSanctionType.setVisible(True)
        self.btnSanctionType.setEnabled(False)

##############   SANCTION LOG   #######################

    def logClicked(self):
        self.resetFormState()
        self.frmSanctionLog.setVisible(True)
        self.btnSanctionLog.setEnabled(False)

##############   STUDENT   #######################

    def studentClicked(self):
        self.resetFormState()
        self.frmStudent.setVisible(True)
        self.btnStudent.setEnabled(False)
        students = dbStudent.getAllStudent()
        if students != None:
            self.tblStudent.setColumnCount(12)
            self.tblStudent.setHorizontalHeaderLabels([
                'StudentNo', 'FName', 'MName', 'LName', 'XTName', 'ContactNo',
                'AddressID', 'Email', 'DateOfBirth', 'Course', 'Section',
                'SchoolYear'
            ])
            row = 0

            for student in students:
                self._StudentNo = student[0]
                self._FName = student[1]
                self._MName = student[2]
                self._LName = student[3]
                self._XTName = student[4]
                self._ContactNo = student[5]
                self._Email = student[6]
                self._AddressID = student[7]
                self._DateOfBirth = student[8]
                self._Course = student[9]
                self._Section = student[10]
                self._SchoolYear = student[11]

                self.tblStudent.insertRow(row)
                self.tblStudent.setItem(row, 0,
                                        QTableWidgetItem(str(self._StudentNo)))
                self.tblStudent.setItem(row, 1, QTableWidgetItem(self._FName))
                self.tblStudent.setItem(row, 2, QTableWidgetItem(self._MName))
                self.tblStudent.setItem(row, 3, QTableWidgetItem(self._LName))
                self.tblStudent.setItem(row, 4, QTableWidgetItem(self._XTName))
                self.tblStudent.setItem(row, 5,
                                        QTableWidgetItem(str(self._ContactNo)))
                self.tblStudent.setItem(row, 6,
                                        QTableWidgetItem(self._AddressID))
                self.tblStudent.setItem(row, 7, QTableWidgetItem(self._Email))
                self.tblStudent.setItem(
                    row, 8, QTableWidgetItem(str(self._DateOfBirth)))
                self.tblStudent.setItem(row, 9, QTableWidgetItem(self._Course))
                self.tblStudent.setItem(row, 10,
                                        QTableWidgetItem(str(self._Section)))
                self.tblStudent.setItem(
                    row, 11, QTableWidgetItem(str(self._SchoolYear)))

                row = row + 1
                self.tblStudent.setVisible(True)

        else:
            msg = self.msgBox()
            msg.setText("NO STUDENT FOUND")
            msg.exec_()

    def tblStudentClicked(self):
        self.r = self.tblStudent.currentRow()
        if (self.tblStudent.item(self.r, 0) != None):
            self.btnStudentUpdate.setEnabled(True)
            self.btnStudentDelete.setEnabled(True)
        else:
            self.btnStudentUpdate.setEnabled(False)
            self.btnStudentDelete.setEnabled(False)

    def studentInit(self):
        self._StudentNo = ''
        self._FName = ''
        self._MName = ''
        self._LName = ''
        self._XTName = ''
        self._ContactNo = 0
        self._Email = ''
        self._AddressID = 0
        self._DateOfBirth = ''
        self._Course = ''
        self._Section = ''
        self._SchoolYear = 0
        self._student = [
            self._StudentNo, self._FName, self._MName, self._LName,
            self._XTName, self._ContactNo, self._Email, self._AddressID,
            self._DateOfBirth, self._Course, self._Section, self._SchoolYear
        ]

    def studentAdd(self):
        self.dgStudent = QtWidgets.QDialog()
        self.dgstud = Ui_dgStud([])
        self.dgstud.setupUi(self.dgStudent)
        # self.dgstud.txtUsername.setEnabled(True)
        self.dgStudent.show()
        x = self.dgStudent.exec_()
        if x == 0:
            self.studentClicked()

    def studentUpdate(self):
        self._StudentNo = self.tblStudent.item(self.r, 0).text()

        self.dgStudent = QtWidgets.QDialog()
        self.dgstud = Ui_dgStud([self._StudentNo])
        self.dgstud.setupUi(self.dgStudent)
        self.dgStudent.show()
        x = self.dgStudent.exec_()
        if x == 0:
            self.studentClicked()

    def studentDelete(self):
        self._StudentNo = self.tblStudent.item(self.r, 0).text()
        msg = self.confirmationBox()
        msg.setText(
            f"Are you sure you want to Delete Student with StudentNo='{self._StudentNo}'?"
        )
        ans = msg.exec_()
        if (ans == 16384):
            dbStudent.deleteStudent(self._StudentNo)
            info = self.infoBox()
            info.setText(
                f"Student with StudetNo='{self._StudentNo}' successfully deleted!"
            )
            info.exec_()
            self.userClicked()

##############   SERVICE   #######################

    def serviceClicked(self):
        self.resetFormState()
        self.frmService.setVisible(True)
        self.btnService.setEnabled(False)


##############   OTHER FUNCTIONS   #######################

    def confirmationLogout(self):
        msg = self.confirmationBox()
        msg.setDefaultButton(QMessageBox.No)
        ans = msg.exec_()
        if (ans == 16384):
            self.wndwAdmin.hide()
            self.wndwLogin.show()

    def infoBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sanction Management System - Information")
        msg.setText("SOME INFO HERE!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        return msg

    def confirmationBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sanction Management System - Confirmation")
        msg.setText("Are you sure you want to Logout?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        return msg

    def resetFormState(self):
        self.frmUser.setVisible(False)
        self.frmAddress.setVisible(False)
        self.frmSanction.setVisible(False)
        self.frmSanctionType.setVisible(False)
        self.frmSanctionLog.setVisible(False)
        self.frmStudent.setVisible(False)
        self.frmService.setVisible(False)
        self.btnUser.setEnabled(True)
        self.btnAddress.setEnabled(True)
        self.btnSanction.setEnabled(True)
        self.btnSanctionType.setEnabled(True)
        self.btnSanctionLog.setEnabled(True)
        self.btnStudent.setEnabled(True)
        self.btnService.setEnabled(True)
        self.btnUserUpdate.setEnabled(False)
        self.btnUserDelete.setEnabled(False)

        self.tblUser.clear()
        self.tblAddress.clear()
        self.tblSanction.clear()
        self.tblType.clear()
        self.tblLog.clear()
        self.tblStudent.clear()
        self.tblService.clear()
