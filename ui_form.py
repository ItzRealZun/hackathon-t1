# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 253)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QSize(0, -1))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.openPathButton = QPushButton(self.centralwidget)
        self.openPathButton.setObjectName(u"openPathButton")
        self.openPathButton.setGeometry(QRect(180, 30, 121, 25))
        self.createGoldenRecordButton = QPushButton(self.centralwidget)
        self.createGoldenRecordButton.setObjectName(u"createGoldenRecordButton")
        self.createGoldenRecordButton.setGeometry(QRect(150, 160, 201, 25))
        self.pathLine = QLineEdit(self.centralwidget)
        self.pathLine.setObjectName(u"pathLine")
        self.pathLine.setGeometry(QRect(60, 90, 361, 25))
        self.pathLine.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 476, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openPathButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.createGoldenRecordButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u043e\u043b\u043e\u0442\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u044c", None))
    # retranslateUi

