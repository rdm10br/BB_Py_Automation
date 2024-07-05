# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QWidget)
from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(591, 467)
        MainWindow.setMinimumSize(QSize(591, 467))
        MainWindow.setWindowTitle(u"BB Py Automation")
        icon = QIcon()
        icon.addFile(u":/icon/automation0.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/automation0.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"    background: qlineargradient(x1:0 y1:1,x2:0 y2:0,stop:0 rgba(30, 41, 59, 1),stop:1 rgba(15, 23, 42, 1));\n"
"    font-family: 'Poppins';\n"
"}\n"
"QWidget{\n"
"	font-family: 'Poppins';\n"
"}\n"
"QLabel{\n"
"    color: rgb(241, 245, 249);\n"
"	font-family: 'Poppins';\n"
"    font-size: 10px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #737BB9;\n"
"    font-family: 'Poppins';\n"
"    color: rgb(241, 245, 249);\n"
"    border: 1px solid #1E293B;\n"
"    border-radius: 12px;\n"
"    padding: 4px;\n"
"    font-size: 13px;\n"
"}\n"
"QMessageBox{\n"
"    background-color: #393D5C;\n"
"    font-family: 'Poppins';\n"
"    color: rgb(241, 245, 249);\n"
"}\n"
"QProgressBar{\n"
"    border: 2px solid #99abeb;\n"
"    background-color: #5e73c0;\n"
"    border-radius: 12px;\n"
"    text-align: center;\n"
"    color: rgb(241, 245, 249);\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: #3C519E;\n"
"    border-radius: 12px;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.icon_widget = QWidget(self.centralwidget)
        self.icon_widget.setObjectName(u"icon_widget")
        self.icon_widget.setGeometry(QRect(0, 0, 55, 451))
        self.icon_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgba(15, 23, 42, 1);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #393D5C;\n"
"}")
        self.label_3 = QLabel(self.icon_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 32, 32))
        self.label_3.setStyleSheet(u"")
        self.label_3.setPixmap(QPixmap(u":/icon/automated-process.png"))
        self.label_3.setScaledContents(True)
        self.pushButton_16 = QPushButton(self.icon_widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(15, 70, 16, 16))
        self.pushButton_16.setStyleSheet(u"background-color: none;\n"
"border: none")
        icon1 = QIcon()
        icon1.addFile(u":/icon/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QSize(20, 20))
        self.line_2 = QFrame(self.icon_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(5, 90, 41, 20))
        self.line_2.setLayoutDirection(Qt.LeftToRight)
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet(u"Line{\n"
"	color: rgb(22, 35, 63);\n"
"}")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.pushButton_18 = QPushButton(self.icon_widget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(5, 410, 40, 36))
        self.pushButton_18.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QSize(16, 16))
        self.splitter_2 = QSplitter(self.icon_widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(5, 110, 44, 240))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.pushButton_24 = QPushButton(self.splitter_2)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setStyleSheet(u"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon3)
        self.pushButton_24.setIconSize(QSize(20, 20))
        self.splitter_2.addWidget(self.pushButton_24)
        self.pushButton_23 = QPushButton(self.splitter_2)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u"border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/icon/double-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_23.setIcon(icon4)
        self.pushButton_23.setIconSize(QSize(20, 20))
        self.splitter_2.addWidget(self.pushButton_23)
        self.pushButton_22 = QPushButton(self.splitter_2)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/icon/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_22.setIcon(icon5)
        self.pushButton_22.setIconSize(QSize(20, 20))
        self.splitter_2.addWidget(self.pushButton_22)
        self.pushButton_21 = QPushButton(self.splitter_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/icon/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon6)
        self.pushButton_21.setIconSize(QSize(20, 20))
        self.splitter_2.addWidget(self.pushButton_21)
        self.pushButton_20 = QPushButton(self.splitter_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/icon/detective.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon7)
        self.pushButton_20.setIconSize(QSize(20, 20))
        self.splitter_2.addWidget(self.pushButton_20)
        self.pushButton_25 = QPushButton(self.splitter_2)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/icon/experiment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_25.setIcon(icon8)
        self.pushButton_25.setIconSize(QSize(20, 20))
        self.splitter_2.addWidget(self.pushButton_25)
        self.splitter_2.raise_()
        self.label_3.raise_()
        self.line_2.raise_()
        self.pushButton_16.raise_()
        self.pushButton_18.raise_()
        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setEnabled(True)
        self.icon_text_widget.setGeometry(QRect(55, 0, 131, 451))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgba(15, 23, 42, 1);\n"
"}\n"
"QPushButton{\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #393D5C;\n"
"}\n"
"QPushButton::icon{\n"
"	subcontrol-position: left center;\n"
"}\n"
"QPushButton::text{\n"
"	subcontrol-position: left center;\n"
"	left: 5px;\n"
"}")
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 25, 71, 21))
        self.label_2.setStyleSheet(u"font-weight: bold;")
        self.label_4 = QLabel(self.icon_text_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 32, 32))
        self.label_4.setStyleSheet(u"border: none;")
        self.label_4.setPixmap(QPixmap(u":/icon/automated-process.png"))
        self.label_4.setScaledContents(True)
        self.line = QFrame(self.icon_text_widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 90, 111, 20))
        self.line.setLayoutDirection(Qt.LeftToRight)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"Line{\n"
"	color: rgb(22, 35, 63);\n"
"}")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.pushButton_17 = QPushButton(self.icon_text_widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(20, 70, 16, 16))
        self.pushButton_17.setStyleSheet(u"padding-left: 0px;")
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QSize(20, 20))
        self.pushButton_15 = QPushButton(self.icon_text_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(0, 410, 128, 36))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setBold(True)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(u"")
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.pushButton_13 = QPushButton(self.icon_text_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(0, 192, 128, 36))
        self.pushButton_13.setStyleSheet(u"")
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setIconSize(QSize(20, 20))
        self.pushButton_8 = QPushButton(self.icon_text_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(0, 110, 128, 36))
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_8.setStyleSheet(u"")
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(20, 20))
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_9 = QPushButton(self.icon_text_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(0, 274, 128, 36))
        self.pushButton_9.setStyleSheet(u"")
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(20, 20))
        self.pushButton_14 = QPushButton(self.icon_text_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(0, 233, 128, 36))
        self.pushButton_14.setStyleSheet(u"")
        self.pushButton_14.setIcon(icon6)
        self.pushButton_14.setIconSize(QSize(20, 20))
        self.pushButton_11 = QPushButton(self.icon_text_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(0, 151, 128, 36))
        self.pushButton_11.setStyleSheet(u"")
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QSize(20, 20))
        self.pushButton_12 = QPushButton(self.icon_text_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(0, 314, 128, 36))
        self.pushButton_12.setStyleSheet(u"")
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QSize(20, 20))
        self.Main_Screen_Widget = QWidget(self.centralwidget)
        self.Main_Screen_Widget.setObjectName(u"Main_Screen_Widget")
        self.Main_Screen_Widget.setGeometry(QRect(185, 40, 406, 411))
        self.Main_Screen_Widget.setAutoFillBackground(False)
        self.Main_Screen_Widget.setStyleSheet(u"background-color:#393D5C;")
        self.frame_4 = QFrame(self.Main_Screen_Widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 45, 131, 136))
        self.frame_4.setStyleSheet(u"background-color: rgba(15, 23, 42, 1);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.Main_Screen_Widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(190, 200, 131, 136))
        self.frame_5.setStyleSheet(u"background-color: rgba(15, 23, 42, 1);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.Main_Screen_Widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(190, 45, 131, 136))
        self.frame_6.setStyleSheet(u"background-color: rgba(15, 23, 42, 1);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.Main_Screen_Widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(40, 200, 131, 136))
        self.frame_7.setStyleSheet(u"background-color: rgba(15, 23, 42, 1);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.Header_widget = QWidget(self.centralwidget)
        self.Header_widget.setObjectName(u"Header_widget")
        self.Header_widget.setGeometry(QRect(185, 0, 406, 41))
        self.Header_widget.setStyleSheet(u"background-color: rgb(33, 41, 66);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.icon_text_widget.raise_()
        self.icon_widget.raise_()
        self.Main_Screen_Widget.raise_()
        self.Header_widget.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label_3.setText("")
        self.pushButton_16.setText("")
        self.pushButton_18.setText("")
        self.pushButton_24.setText("")
        self.pushButton_23.setText("")
        self.pushButton_22.setText("")
        self.pushButton_21.setText("")
        self.pushButton_20.setText("")
        self.pushButton_25.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Automa\u00e7\u00e3o", None))
        self.label_4.setText("")
        self.pushButton_17.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"C\u00f3pia", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"X9", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Double Check", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        pass
    # retranslateUi

