# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'labOneQt.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(516, 363)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(350, 10, 151, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 5, 15, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, -1, -1)
        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_3.addWidget(self.radioButton_3)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.radioButton_4 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_4.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_4.addWidget(self.radioButton_5)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 200, 481, 51))

        # layout for chekbox
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)

        #revers
        self.checkBox_4 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_4)


        # sound
        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_2)

        # backlight
        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        # auto
        self.checkBox_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 180, 81, 16))
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 331, 161))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Eras Bold ITC")
        font.setPointSize(14)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.lcdNumber = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMouseTracking(False)

        self.horizontalLayout_3.addWidget(self.lcdNumber)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 270, 55, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 270, 91, 16))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 290, 111, 31))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(392, 290, 111, 31))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 330, 481, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):

        # Добавляем название окну
        # tr() = переводимая строка с помошью лингвист
        self.setWindowTitle(self.tr("SETTING MENU"))
        # добавляем иконку окну
        icon = QIcon("img/settings.png")
        self.setWindowIcon(icon)

        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Button one", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Button two", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Button three", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"MENU", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"OPTION", None))

        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"REVERSE", None))

        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"SOUND", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"BACKLIGHT", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"AUTO", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SETTINGS", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"COUNTER", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"EXIT", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"ADD", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"COLOR", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"BRIGHTNESS", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"INSTALL", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"INSTALL", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"FIRST", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"SECOND", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"THIRD", None))

    # retranslateUi

