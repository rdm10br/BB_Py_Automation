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
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(670, 470)
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
        self.icon_widget.setGeometry(QRect(130, 0, 55, 451))
        self.icon_widget.setStyleSheet(u"QWidget{\n"
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
"}\n"
"QPushButton:on{\n"
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
        self.pushButton_16.setGeometry(QRect(15, 70, 20, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QSize(20, 20))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	padding-left: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: none;\n"
"}\n"
"QPushButton:on{\n"
"	background-color: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QSize(20, 20))
        self.pushButton_16.setCheckable(True)
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
        self.layoutWidget = QWidget(self.icon_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(5, 110, 46, 336))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.layoutWidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.pushButton_24 = QPushButton(self.splitter_2)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon2)
        self.pushButton_24.setIconSize(QSize(20, 20))
        self.pushButton_24.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_24)
        self.pushButton_23 = QPushButton(self.splitter_2)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/double-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_23.setIcon(icon3)
        self.pushButton_23.setIconSize(QSize(20, 20))
        self.pushButton_23.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_23)
        self.pushButton_22 = QPushButton(self.splitter_2)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_22.setIcon(icon4)
        self.pushButton_22.setIconSize(QSize(20, 20))
        self.pushButton_22.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_22)
        self.pushButton_21 = QPushButton(self.splitter_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon5)
        self.pushButton_21.setIconSize(QSize(20, 20))
        self.pushButton_21.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_21)
        self.pushButton_20 = QPushButton(self.splitter_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/detective.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon6)
        self.pushButton_20.setIconSize(QSize(20, 20))
        self.pushButton_20.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_20)
        self.pushButton_25 = QPushButton(self.splitter_2)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/experiment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_25.setIcon(icon7)
        self.pushButton_25.setIconSize(QSize(20, 20))
        self.pushButton_25.setCheckable(True)
        self.splitter_2.addWidget(self.pushButton_25)

        self.verticalLayout_6.addWidget(self.splitter_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(38, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.pushButton_18 = QPushButton(self.layoutWidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy1)
        self.pushButton_18.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icon/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon8)
        self.pushButton_18.setIconSize(QSize(16, 16))
        self.pushButton_18.setCheckable(True)

        self.verticalLayout_5.addWidget(self.pushButton_18)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.layoutWidget1.raise_()
        self.label_3.raise_()
        self.line_2.raise_()
        self.pushButton_16.raise_()
        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setEnabled(True)
        self.icon_text_widget.setGeometry(QRect(0, 0, 131, 451))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgba(15, 23, 42, 1);\n"
"}\n"
"QPushButton{\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	text-align: left;\n"
"	padding-left: 1,5px;\n"
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
"}\n"
"QPushButton:on{\n"
"	background-color: #393D5C;\n"
"}")
        self.layoutWidget1 = QWidget(self.icon_text_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(5, 105, 126, 271))
        self.MainButtons = QVBoxLayout(self.layoutWidget1)
        self.MainButtons.setObjectName(u"MainButtons")
        self.MainButtons.setContentsMargins(0, 0, 0, 6)
        self.Home_pushButton = QPushButton(self.layoutWidget1)
        self.Home_pushButton.setObjectName(u"Home_pushButton")
        self.Home_pushButton.setMaximumSize(QSize(118, 16777215))
        self.Home_pushButton.setToolTipDuration(5)
        self.Home_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.Home_pushButton.setStyleSheet(u"")
        self.Home_pushButton.setIcon(icon2)
        self.Home_pushButton.setIconSize(QSize(20, 20))
        self.Home_pushButton.setCheckable(True)
        self.Home_pushButton.setAutoDefault(True)

        self.MainButtons.addWidget(self.Home_pushButton)

        self.DoubleCheck = QFrame(self.layoutWidget1)
        self.DoubleCheck.setObjectName(u"DoubleCheck")
        self.DoubleCheck.setStyleSheet(u"")
        self.DoubleCheck.setFrameShape(QFrame.StyledPanel)
        self.DoubleCheck.setFrameShadow(QFrame.Raised)
        self.splitter_4 = QSplitter(self.DoubleCheck)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(2, 5, 122, 199))
        self.splitter_4.setOrientation(Qt.Vertical)
        self.pushButton_11 = QPushButton(self.splitter_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy2)
        self.pushButton_11.setMaximumSize(QSize(118, 16777215))
        self.pushButton_11.setStyleSheet(u"")
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setIconSize(QSize(20, 20))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.splitter_4.addWidget(self.pushButton_11)
        self.DoubleCheck_DropDown = QFrame(self.splitter_4)
        self.DoubleCheck_DropDown.setObjectName(u"DoubleCheck_DropDown")
        self.DoubleCheck_DropDown.setAutoFillBackground(False)
        self.DoubleCheck_DropDown.setStyleSheet(u"")
        self.DoubleCheck_DropDown.setFrameShape(QFrame.StyledPanel)
        self.DoubleCheck_DropDown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.DoubleCheck_DropDown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.DoubleCheck_DropDown)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #393D5C;\n"
"}")
        self.splitter.setOrientation(Qt.Vertical)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)
        self.splitter.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.splitter.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.splitter)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.splitter.addWidget(self.pushButton_3)
        self.pushButton_4 = QPushButton(self.splitter)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)
        self.splitter.addWidget(self.pushButton_4)

        self.verticalLayout_2.addWidget(self.splitter)

        self.splitter_4.addWidget(self.DoubleCheck_DropDown)

        self.MainButtons.addWidget(self.DoubleCheck)

        self.Copia = QFrame(self.layoutWidget1)
        self.Copia.setObjectName(u"Copia")
        self.Copia.setStyleSheet(u"")
        self.Copia.setFrameShape(QFrame.StyledPanel)
        self.Copia.setFrameShadow(QFrame.Raised)
        self.splitter_6 = QSplitter(self.Copia)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(2, 5, 118, 111))
        self.splitter_6.setOrientation(Qt.Vertical)
        self.pushButton_13 = QPushButton(self.splitter_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy2.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy2)
        self.pushButton_13.setMaximumSize(QSize(118, 16777215))
        self.pushButton_13.setStyleSheet(u"")
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QSize(20, 20))
        self.pushButton_13.setCheckable(True)
        self.splitter_6.addWidget(self.pushButton_13)
        self.Copy_DropDown = QFrame(self.splitter_6)
        self.Copy_DropDown.setObjectName(u"Copy_DropDown")
        self.Copy_DropDown.setAutoFillBackground(False)
        self.Copy_DropDown.setStyleSheet(u"")
        self.Copy_DropDown.setFrameShape(QFrame.StyledPanel)
        self.Copy_DropDown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Copy_DropDown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_3 = QSplitter(self.Copy_DropDown)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #393D5C;\n"
"}")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.pushButton_7 = QPushButton(self.splitter_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCheckable(True)
        self.splitter_3.addWidget(self.pushButton_7)
        self.pushButton_10 = QPushButton(self.splitter_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCheckable(True)
        self.splitter_3.addWidget(self.pushButton_10)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter_6.addWidget(self.Copy_DropDown)

        self.MainButtons.addWidget(self.Copia)

        self.Data = QFrame(self.layoutWidget1)
        self.Data.setObjectName(u"Data")
        self.Data.setStyleSheet(u"")
        self.Data.setFrameShape(QFrame.StyledPanel)
        self.Data.setFrameShadow(QFrame.Raised)
        self.splitter_7 = QSplitter(self.Data)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setGeometry(QRect(0, 0, 118, 86))
        self.splitter_7.setOrientation(Qt.Vertical)
        self.pushButton_14 = QPushButton(self.splitter_7)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy2.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy2)
        self.pushButton_14.setMaximumSize(QSize(118, 16777215))
        self.pushButton_14.setStyleSheet(u"padding-left: 6px;")
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setIconSize(QSize(20, 20))
        self.pushButton_14.setCheckable(True)
        self.splitter_7.addWidget(self.pushButton_14)
        self.Date_DropDown = QFrame(self.splitter_7)
        self.Date_DropDown.setObjectName(u"Date_DropDown")
        self.Date_DropDown.setAutoFillBackground(False)
        self.Date_DropDown.setStyleSheet(u"")
        self.Date_DropDown.setFrameShape(QFrame.StyledPanel)
        self.Date_DropDown.setFrameShadow(QFrame.Raised)
        self.pushButton_19 = QPushButton(self.Date_DropDown)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(20, 5, 96, 26))
        self.pushButton_19.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #393D5C;\n"
"}")
        self.pushButton_19.setCheckable(True)
        self.splitter_7.addWidget(self.Date_DropDown)

        self.MainButtons.addWidget(self.Data)

        self.X9 = QFrame(self.layoutWidget1)
        self.X9.setObjectName(u"X9")
        self.X9.setStyleSheet(u"")
        self.X9.setFrameShape(QFrame.StyledPanel)
        self.X9.setFrameShadow(QFrame.Raised)
        self.splitter_5 = QSplitter(self.X9)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(2, 5, 118, 91))
        self.splitter_5.setOrientation(Qt.Vertical)
        self.pushButton_9 = QPushButton(self.splitter_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(118, 16777215))
        self.pushButton_9.setStyleSheet(u"padding-left: 3px;")
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QSize(20, 20))
        self.pushButton_9.setCheckable(True)
        self.splitter_5.addWidget(self.pushButton_9)
        self.X9_DropDown = QFrame(self.splitter_5)
        self.X9_DropDown.setObjectName(u"X9_DropDown")
        self.X9_DropDown.setAutoFillBackground(False)
        self.X9_DropDown.setStyleSheet(u"")
        self.X9_DropDown.setFrameShape(QFrame.StyledPanel)
        self.X9_DropDown.setFrameShadow(QFrame.Raised)
        self.pushButton_26 = QPushButton(self.X9_DropDown)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(5, 5, 91, 46))
        self.pushButton_26.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #393D5C;\n"
"}")
        self.pushButton_26.setCheckable(True)
        self.splitter_5.addWidget(self.X9_DropDown)

        self.MainButtons.addWidget(self.X9)

        self.Test_pushButton = QPushButton(self.layoutWidget1)
        self.Test_pushButton.setObjectName(u"Test_pushButton")
        self.Test_pushButton.setMaximumSize(QSize(118, 16777215))
        self.Test_pushButton.setStyleSheet(u"")
        self.Test_pushButton.setIcon(icon7)
        self.Test_pushButton.setIconSize(QSize(20, 20))
        self.Test_pushButton.setCheckable(True)

        self.MainButtons.addWidget(self.Test_pushButton)

        self.pushButton_15 = QPushButton(self.icon_text_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(5, 426, 113, 24))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setBold(True)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(u"")
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.pushButton_15.setCheckable(True)
        self.widget = QWidget(self.icon_text_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(5, 5, 126, 101))
        self.header = QVBoxLayout(self.widget)
        self.header.setObjectName(u"header")
        self.header.setContentsMargins(4, 0, 4, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMaximumSize(QSize(32, 32))
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u":/icon/automated-process.png"))
        self.label_4.setScaledContents(True)

        self.header.addWidget(self.label_4)

        self.pushButton_17 = QPushButton(self.widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy3.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy3)
        self.pushButton_17.setMinimumSize(QSize(20, 20))
        self.pushButton_17.setMaximumSize(QSize(20, 20))
        self.pushButton_17.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: none;\n"
"}\n"
"QPushButton:on{\n"
"	background-color: none;\n"
"}")
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QSize(20, 20))
        self.pushButton_17.setCheckable(True)

        self.header.addWidget(self.pushButton_17)

        self.verticalSpacer_5 = QSpacerItem(20, 7, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.header.addItem(self.verticalSpacer_5)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setLayoutDirection(Qt.LeftToRight)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"Line{\n"
"	color: rgb(22, 35, 63);\n"
"}")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.header.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.header.addItem(self.verticalSpacer_3)

        self.Main_Screen_Widget = QWidget(self.centralwidget)
        self.Main_Screen_Widget.setObjectName(u"Main_Screen_Widget")
        self.Main_Screen_Widget.setEnabled(True)
        self.Main_Screen_Widget.setGeometry(QRect(185, 40, 491, 411))
        self.Main_Screen_Widget.setAutoFillBackground(False)
        self.Main_Screen_Widget.setStyleSheet(u"background-color:#393D5C;")
        self.Header_widget = QWidget(self.centralwidget)
        self.Header_widget.setObjectName(u"Header_widget")
        self.Header_widget.setGeometry(QRect(185, 0, 491, 41))
        self.Header_widget.setStyleSheet(u"background-color: rgb(33, 41, 66);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.icon_widget.raise_()
        self.Main_Screen_Widget.raise_()
        self.Header_widget.raise_()
        self.icon_text_widget.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_11.toggled.connect(self.DoubleCheck_DropDown.setHidden)
        self.pushButton_9.toggled.connect(self.X9_DropDown.setHidden)
        self.pushButton_13.toggled.connect(self.Copy_DropDown.setHidden)
        self.pushButton_14.toggled.connect(self.Date_DropDown.setHidden)

        self.Home_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label_3.setText("")
        self.pushButton_16.setText("")
        self.pushButton_24.setText("")
        self.pushButton_23.setText("")
        self.pushButton_22.setText("")
        self.pushButton_21.setText("")
        self.pushButton_20.setText("")
        self.pushButton_25.setText("")
        self.pushButton_18.setText("")
        self.Home_pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Double\n"
"Check", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Atividades\n"
"Pr\u00e1ticas", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Master", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Mescla Digital", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Mescla\n"
"Veteranos", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"C\u00f3pia", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Nova Sala", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Ajuste de Data", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"X9", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Double Check\n"
"Configura\u00e7\u00f5es", None))
        self.Test_pushButton.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.label_4.setText("")
        self.pushButton_17.setText("")
#if QT_CONFIG(tooltip)
        self.Main_Screen_Widget.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

