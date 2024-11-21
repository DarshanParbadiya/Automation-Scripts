# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emailappEoZcOa.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
import emailapp_rc
import emailapp_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(521, 522)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color : whitergb(231, 231, 231)")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 521, 511))
        self.tabWidget.setStyleSheet(u"background-color :  rgb(227, 227, 227);")
        self.Main = QWidget()
        self.Main.setObjectName(u"Main")
        self.widget = QWidget(self.Main)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 481, 111))
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

        self.widget_2 = QWidget(self.Main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QRect(10, 130, 481, 341))
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
        icon.addFile(u"../icons/true.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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

        self.horizontalSpacer_3 = QSpacerItem(28, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        self.horizontalSpacer_2 = QSpacerItem(28, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.dateEdit_2 = QDateEdit(self.date_column)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.dateEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.Main, "")
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.widget_3 = QWidget(self.config)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 491, 451))
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 140, 51, 41))
        self.label_6.setPixmap(QPixmap(u":/icons/path.png"))
        self.label_6.setScaledContents(True)
        self.path = QLineEdit(self.widget_3)
        self.path.setObjectName(u"path")
        self.path.setGeometry(QRect(90, 150, 371, 31))
        self.path.setStyleSheet(u"font-family : serif;\n"
"font-size : 16px;\n"
"font-weight : 600;\n"
"background-color : rgb(16, 151, 255);\n"
"color : white;\n"
"border : none;")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 481, 111))
        self.widget_4.setStyleSheet(u"background-color : white;\n"
"border-radius : 20px;\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 100))
        self.label_7.setMaximumSize(QSize(100, 100))
        self.label_7.setPixmap(QPixmap(u":/icons/email.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color : rgb(0, 81, 255)")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 190, 41, 41))
        self.label_9.setPixmap(QPixmap(u":/icons/searching.png"))
        self.label_9.setScaledContents(True)
        self.url = QLineEdit(self.widget_3)
        self.url.setObjectName(u"url")
        self.url.setGeometry(QRect(90, 200, 371, 31))
        self.url.setStyleSheet(u"font-family : serif;\n"
"font-size : 16px;\n"
"font-weight : 600;\n"
"background-color : rgb(16, 151, 255);\n"
"color : white;\n"
"border : none;")
        self.tabWidget.addTab(self.config, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), QCoreApplication.translate("MainWindow", u"Main", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Email Saver app v1", None))
        self.label_9.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), QCoreApplication.translate("MainWindow", u"config", None))
    # retranslateUi

