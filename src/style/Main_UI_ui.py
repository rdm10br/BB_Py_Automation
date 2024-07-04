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
"    padding: 10px;\n"
"    font-size: 14px;\n"
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
"QPushButton:hover{\n"
"	background-color: #393D5C;\n"
"}")
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 25, 71, 21))
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
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"}")
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QSize(20, 20))
        self.splitter_6 = QSplitter(self.icon_text_widget)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(10, 410, 109, 36))
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.pushButton_15 = QPushButton(self.splitter_6)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border: none;")
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.splitter_6.addWidget(self.pushButton_15)
        self.label_11 = QLabel(self.splitter_6)
        self.label_11.setObjectName(u"label_11")
        self.splitter_6.addWidget(self.label_11)
        self.splitter_9 = QSplitter(self.icon_text_widget)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setGeometry(QRect(0, 110, 102, 240))
        self.splitter_9.setOrientation(Qt.Vertical)
        self.splitter_8 = QSplitter(self.splitter_9)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Horizontal)
        self.pushButton_8 = QPushButton(self.splitter_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"border: none;")
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(20, 20))
        self.splitter_8.addWidget(self.pushButton_8)
        self.label_5 = QLabel(self.splitter_8)
        self.label_5.setObjectName(u"label_5")
        self.splitter_8.addWidget(self.label_5)
        self.splitter_9.addWidget(self.splitter_8)
        self.splitter_7 = QSplitter(self.splitter_9)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.pushButton_11 = QPushButton(self.splitter_7)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"border: none;")
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QSize(20, 20))
        self.splitter_7.addWidget(self.pushButton_11)
        self.label_6 = QLabel(self.splitter_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 10px;")
        self.splitter_7.addWidget(self.label_6)
        self.splitter_9.addWidget(self.splitter_7)
        self.splitter_5 = QSplitter(self.splitter_9)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.pushButton_13 = QPushButton(self.splitter_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"border: none;")
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setIconSize(QSize(20, 20))
        self.splitter_5.addWidget(self.pushButton_13)
        self.label_7 = QLabel(self.splitter_5)
        self.label_7.setObjectName(u"label_7")
        self.splitter_5.addWidget(self.label_7)
        self.splitter_9.addWidget(self.splitter_5)
        self.splitter_4 = QSplitter(self.splitter_9)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.pushButton_14 = QPushButton(self.splitter_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"border: none;")
        self.pushButton_14.setIcon(icon6)
        self.pushButton_14.setIconSize(QSize(20, 20))
        self.splitter_4.addWidget(self.pushButton_14)
        self.label_9 = QLabel(self.splitter_4)
        self.label_9.setObjectName(u"label_9")
        self.splitter_4.addWidget(self.label_9)
        self.splitter_9.addWidget(self.splitter_4)
        self.splitter_3 = QSplitter(self.splitter_9)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.pushButton_9 = QPushButton(self.splitter_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"border: none;")
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(20, 20))
        self.splitter_3.addWidget(self.pushButton_9)
        self.label_8 = QLabel(self.splitter_3)
        self.label_8.setObjectName(u"label_8")
        self.splitter_3.addWidget(self.label_8)
        self.splitter_9.addWidget(self.splitter_3)
        self.splitter = QSplitter(self.splitter_9)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton_12 = QPushButton(self.splitter)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"border: none;")
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QSize(20, 20))
        self.splitter.addWidget(self.pushButton_12)
        self.label_10 = QLabel(self.splitter)
        self.label_10.setObjectName(u"label_10")
        self.splitter.addWidget(self.label_10)
        self.splitter_9.addWidget(self.splitter)
        self.Main_Screen_Widget = QWidget(self.centralwidget)
        self.Main_Screen_Widget.setObjectName(u"Main_Screen_Widget")
        self.Main_Screen_Widget.setGeometry(QRect(185, 40, 406, 411))
        self.Main_Screen_Widget.setAutoFillBackground(False)
        self.Main_Screen_Widget.setStyleSheet(u"background-color:#393D5C;")
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
        self.pushButton_15.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.pushButton_8.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Home  ", None))
        self.pushButton_11.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Double\n"
"Check", None))
        self.pushButton_13.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"C\u00f3pia ", None))
        self.pushButton_14.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Data   ", None))
        self.pushButton_9.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X9     ", None))
        self.pushButton_12.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Teste  ", None))
        pass
    # retranslateUi

