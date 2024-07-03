# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'threads_test.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(595, 412)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background: qlineargradient(x1:0 y1:1,x2:0 y2:0,stop:0 rgba(30, 41, 59, 1),stop:1 rgba(15, 23, 42, 1));\n"
"font-family: 'Poppins';\n"
"color: rgb(241, 245, 249);")
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self.action12 = QAction(MainWindow)
        self.action12.setObjectName(u"action12")
        self.action13 = QAction(MainWindow)
        self.action13.setObjectName(u"action13")
        self.action21 = QAction(MainWindow)
        self.action21.setObjectName(u"action21")
        self.action22 = QAction(MainWindow)
        self.action22.setObjectName(u"action22")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 30, 141, 41))
        self.pushButton.setStyleSheet(u"background-color: #393D5C;\n"
"font-family: 'Poppins';\n"
"color: rgb(241, 245, 249);\n"
"border: 1px solid #1E293B;\n"
"border-radius: 12px;\n"
"padding: 10px;\n"
"font-size: 14px;")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(290, 30, 251, 31))
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"    border: 2px solid #99abeb;\n"
"    background-color: #5e73c0;\n"
"    border-radius: 12px;\n"
"    text-align: center;\n"
"    color: rgb(241, 245, 249);\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: #3C519E;\n"
"    border-radius: 12px;\n"
"    margin: 1px;\n"
"	border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"    border-top-left-radius: 10px;\n"
"}\n"
"QProgressBar::chunk[8>=value] {\n"
"	border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 8px;\n"
"	border-top-right-radius: 10px;\n"
"    border-top-left-radius: 8px;\n"
"}")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(9)
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 101, 381))
        self.listWidget.setStyleSheet(u"QListWidget:item:hover{\n"
" background-color: #5e73c0;\n"
" padding: 3px;\n"
"}\n"
"QListWidget:item{\n"
" padding: 3px;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 595, 20))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.action1)
        self.menuMenu.addAction(self.action2)
        self.menuConfig.addAction(self.action12)
        self.menuConfig.addAction(self.action13)
        self.menuEdit.addAction(self.action21)
        self.menuEdit.addAction(self.action22)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.action12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.action13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.action21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.action22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Double Check", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Copia", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"BQ", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Teste", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

