# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(596, 507)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vrtLO_main = QVBoxLayout()
        self.vrtLO_main.setSpacing(5)
        self.vrtLO_main.setObjectName(u"vrtLO_main")
        self.vrtLO_main.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vrtLO_main.setContentsMargins(10, 10, 10, 10)
        self.hrzLO_input = QHBoxLayout()
        self.hrzLO_input.setObjectName(u"hrzLO_input")
        self.LnEd_userInput = QLineEdit(self.centralwidget)
        self.LnEd_userInput.setObjectName(u"LnEd_userInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LnEd_userInput.sizePolicy().hasHeightForWidth())
        self.LnEd_userInput.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LnEd_userInput.setFont(font)
        self.LnEd_userInput.setAlignment(Qt.AlignCenter)

        self.hrzLO_input.addWidget(self.LnEd_userInput)

        self.Lb_userInput = QLabel(self.centralwidget)
        self.Lb_userInput.setObjectName(u"Lb_userInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Lb_userInput.sizePolicy().hasHeightForWidth())
        self.Lb_userInput.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(16)
        self.Lb_userInput.setFont(font1)
        self.Lb_userInput.setAlignment(Qt.AlignCenter)

        self.hrzLO_input.addWidget(self.Lb_userInput)

        self.LnEd_baseInput = QLineEdit(self.centralwidget)
        self.LnEd_baseInput.setObjectName(u"LnEd_baseInput")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LnEd_baseInput.sizePolicy().hasHeightForWidth())
        self.LnEd_baseInput.setSizePolicy(sizePolicy4)
        self.LnEd_baseInput.setFont(font)
        self.LnEd_baseInput.setAlignment(Qt.AlignCenter)

        self.hrzLO_input.addWidget(self.LnEd_baseInput)


        self.vrtLO_main.addLayout(self.hrzLO_input)

        self.Lb_errorMessage = QLabel(self.centralwidget)
        self.Lb_errorMessage.setObjectName(u"Lb_errorMessage")
        self.Lb_errorMessage.setEnabled(True)
        self.Lb_errorMessage.setWordWrap(True)

        self.vrtLO_main.addWidget(self.Lb_errorMessage)

        self.vrtLO_roundingMeth = QVBoxLayout()
        self.vrtLO_roundingMeth.setObjectName(u"vrtLO_roundingMeth")
        self.vrtLO_roundingMeth.setContentsMargins(5, 5, 5, 5)
        self.Lb_roundingMeth = QLabel(self.centralwidget)
        self.Lb_roundingMeth.setObjectName(u"Lb_roundingMeth")

        self.vrtLO_roundingMeth.addWidget(self.Lb_roundingMeth)

        self.vrtLO_roundingOpt = QVBoxLayout()
        self.vrtLO_roundingOpt.setObjectName(u"vrtLO_roundingOpt")
        self.vrtLO_roundingOpt.setContentsMargins(5, 5, 5, 5)
        self.rdBtn_nearEven = QRadioButton(self.centralwidget)
        self.btnGrp_roundMeth = QButtonGroup(MainWindow)
        self.btnGrp_roundMeth.setObjectName(u"btnGrp_roundMeth")
        self.btnGrp_roundMeth.addButton(self.rdBtn_nearEven)
        self.rdBtn_nearEven.setObjectName(u"rdBtn_nearEven")
        self.rdBtn_nearEven.setChecked(True)

        self.vrtLO_roundingOpt.addWidget(self.rdBtn_nearEven)

        self.rdBtn_floor = QRadioButton(self.centralwidget)
        self.btnGrp_roundMeth.addButton(self.rdBtn_floor)
        self.rdBtn_floor.setObjectName(u"rdBtn_floor")

        self.vrtLO_roundingOpt.addWidget(self.rdBtn_floor)

        self.rdBtn_ceil = QRadioButton(self.centralwidget)
        self.btnGrp_roundMeth.addButton(self.rdBtn_ceil)
        self.rdBtn_ceil.setObjectName(u"rdBtn_ceil")

        self.vrtLO_roundingOpt.addWidget(self.rdBtn_ceil)

        self.rdBtn_nearZero = QRadioButton(self.centralwidget)
        self.btnGrp_roundMeth.addButton(self.rdBtn_nearZero)
        self.rdBtn_nearZero.setObjectName(u"rdBtn_nearZero")

        self.vrtLO_roundingOpt.addWidget(self.rdBtn_nearZero)


        self.vrtLO_roundingMeth.addLayout(self.vrtLO_roundingOpt)


        self.vrtLO_main.addLayout(self.vrtLO_roundingMeth)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.Btn_convert = QPushButton(self.centralwidget)
        self.Btn_convert.setObjectName(u"Btn_convert")
        self.Btn_convert.setMinimumSize(QSize(150, 0))
        self.Btn_convert.setFont(font1)

        self.horizontalLayout_4.addWidget(self.Btn_convert)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.vrtLO_main.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vrtLO_main.addItem(self.verticalSpacer_2)

        self.frmLO_output = QFormLayout()
        self.frmLO_output.setObjectName(u"frmLO_output")
        self.Lb_binary = QLabel(self.centralwidget)
        self.Lb_binary.setObjectName(u"Lb_binary")
        self.Lb_binary.setFont(font1)
        self.Lb_binary.setAlignment(Qt.AlignCenter)

        self.frmLO_output.setWidget(0, QFormLayout.LabelRole, self.Lb_binary)

        self.Lb_hexadecimal = QLabel(self.centralwidget)
        self.Lb_hexadecimal.setObjectName(u"Lb_hexadecimal")
        self.Lb_hexadecimal.setFont(font1)
        self.Lb_hexadecimal.setAlignment(Qt.AlignCenter)

        self.frmLO_output.setWidget(1, QFormLayout.LabelRole, self.Lb_hexadecimal)

        self.LnEd_hexadecimal = QLineEdit(self.centralwidget)
        self.LnEd_hexadecimal.setObjectName(u"LnEd_hexadecimal")
        self.LnEd_hexadecimal.setFont(font1)
        self.LnEd_hexadecimal.setReadOnly(True)

        self.frmLO_output.setWidget(1, QFormLayout.FieldRole, self.LnEd_hexadecimal)

        self.LnEd_binary = QLineEdit(self.centralwidget)
        self.LnEd_binary.setObjectName(u"LnEd_binary")
        self.LnEd_binary.setFont(font1)
        self.LnEd_binary.setReadOnly(True)

        self.frmLO_output.setWidget(0, QFormLayout.FieldRole, self.LnEd_binary)


        self.vrtLO_main.addLayout(self.frmLO_output)

        self.hrzLO_printText = QHBoxLayout()
        self.hrzLO_printText.setSpacing(0)
        self.hrzLO_printText.setObjectName(u"hrzLO_printText")
        self.PshBtn_printText = QPushButton(self.centralwidget)
        self.PshBtn_printText.setObjectName(u"PshBtn_printText")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.PshBtn_printText.sizePolicy().hasHeightForWidth())
        self.PshBtn_printText.setSizePolicy(sizePolicy5)
        self.PshBtn_printText.setMaximumSize(QSize(200, 16777215))
        self.PshBtn_printText.setFont(font1)

        self.hrzLO_printText.addWidget(self.PshBtn_printText)


        self.vrtLO_main.addLayout(self.hrzLO_printText)

        self.vrtLO_main.setStretch(0, 1)
        self.vrtLO_main.setStretch(2, 1)
        self.vrtLO_main.setStretch(5, 1)
        self.vrtLO_main.setStretch(6, 1)

        self.gridLayout.addLayout(self.vrtLO_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LnEd_userInput.setText(QCoreApplication.translate("MainWindow", u"69", None))
        self.Lb_userInput.setText(QCoreApplication.translate("MainWindow", u"x 10 ^", None))
        self.LnEd_baseInput.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Lb_errorMessage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">ERROR: Sample Error</span></p></body></html>", None))
        self.Lb_roundingMeth.setText(QCoreApplication.translate("MainWindow", u"Rounding methods:", None))
        self.rdBtn_nearEven.setText(QCoreApplication.translate("MainWindow", u"Round to Nearest Zero Ties to Nearest Even", None))
        self.rdBtn_floor.setText(QCoreApplication.translate("MainWindow", u"Floor", None))
        self.rdBtn_ceil.setText(QCoreApplication.translate("MainWindow", u"Ceiling", None))
        self.rdBtn_nearZero.setText(QCoreApplication.translate("MainWindow", u"Round to Nearest Zero", None))
        self.Btn_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.Lb_binary.setText(QCoreApplication.translate("MainWindow", u"Binary", None))
        self.Lb_hexadecimal.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal", None))
        self.LnEd_hexadecimal.setText(QCoreApplication.translate("MainWindow", u"0x45", None))
        self.LnEd_binary.setText(QCoreApplication.translate("MainWindow", u"0b0b1000101", None))
        self.PshBtn_printText.setText(QCoreApplication.translate("MainWindow", u"Print into text file", None))
    # retranslateUi

