# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIbwxMol.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, QRect,
                            QSize)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QComboBox, QDateEdit, QHBoxLayout,
                               QLabel, QLineEdit, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(539, 542)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color : whitergb(231, 231, 231)")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 521, 111))
        self.widget.setStyleSheet(u"background-color : white;\n"
"border-radius : 20px;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 100))
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u":/icons/email.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(25)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color : rgb(0, 81, 255)")

        self.horizontalLayout.addWidget(self.label)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QRect(10, 140, 521, 361))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"background-color : white;\n"
"border-radius : 20px;\n"
"}\n"
"\n"
"QComboBox{\n"
"border-radius : 10px;\n"
"padding-left : 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: white;\n"
"border :2px solid green;\n"
"color : green;\n"
"padding : 10px 5px;\n"
"font-size : 15px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color : rgb(202, 255, 233)\n"
"}")
        self.selected_option = QComboBox(self.widget_2)
        self.selected_option.addItem("")
        self.selected_option.addItem("")
        self.selected_option.addItem("")
        self.selected_option.setObjectName(u"selected_option")
        self.selected_option.setGeometry(QRect(130, 90, 221, 41))
        self.selected_option.setStyleSheet(u"font-family : serif;\n"
"font-size : 16px;\n"
"font-weight : 600;\n"
"background-color : rgb(16, 151, 255);\n"
"color : white;\n"
"border : none;")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 80, 60, 60))
        self.label_3.setMinimumSize(QSize(60, 60))
        self.label_3.setMaximumSize(QSize(60, 60))
        self.label_3.setPixmap(QPixmap(u":/icons/date.png"))
        self.label_3.setScaledContents(True)
        self.save_button = QPushButton(self.widget_2)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(140, 250, 111, 41))
        self.save_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../icons/true.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon)
        self.save_button.setIconSize(QSize(25, 25))
        self.save_button.setCheckable(True)
        self.save_button.setChecked(False)
        self.save_button.setAutoExclusive(True)
        self.date_column = QWidget(self.widget_2)
        self.date_column.setObjectName(u"date_column")
        self.date_column.setEnabled(True)
        self.date_column.setGeometry(QRect(130, 150, 244, 76))
        self.date_column.setAutoFillBackground(False)
        self.date_column.setStyleSheet(u"font-size : 17px;")
        self.verticalLayout = QVBoxLayout(self.date_column)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.date_column)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(28, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.dateEdit = QDateEdit(self.date_column)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2000, 2, 1))

        self.horizontalLayout_2.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.date_column)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(28, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.dateEdit_2 = QDateEdit(self.date_column)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dateEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 40, 371, 31))
        self.lineEdit.setStyleSheet(u"font-family : serif;\n"
"font-size : 16px;\n"
"font-weight : 600;\n"
"background-color : rgb(16, 151, 255);\n"
"color : white;\n"
"border : none;")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 51, 41))
        self.label_6.setPixmap(QPixmap(u":/icons/path.png"))
        self.label_6.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 539, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Email Saver app v1", None))
        self.selected_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Today", None))
        self.selected_option.setItemText(1, QCoreApplication.translate("MainWindow", u"Yesterday", None))
        self.selected_option.setItemText(2, QCoreApplication.translate("MainWindow", u"Date Range", None))

        self.label_3.setText("")
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/dd/yyyy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/dd/yyyy", None))
        self.label_6.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

