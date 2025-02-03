# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import icons_rc

class Ui_w_main(object):
    def setupUi(self, w_main):
        if not w_main.objectName():
            w_main.setObjectName(u"w_main")
        w_main.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/Main/icons8-dollar-bills-94.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_main.setWindowIcon(icon)
        self.act_quit = QAction(w_main)
        self.act_quit.setObjectName(u"act_quit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/icons8-cancel-94.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_quit.setIcon(icon1)
        self.act_add_person = QAction(w_main)
        self.act_add_person.setObjectName(u"act_add_person")
        self.centralwidget = QWidget(w_main)
        self.centralwidget.setObjectName(u"centralwidget")
        w_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPerson = QMenu(self.menubar)
        self.menuPerson.setObjectName(u"menuPerson")
        w_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_main)
        self.statusbar.setObjectName(u"statusbar")
        w_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPerson.menuAction())
        self.menuFile.addAction(self.act_quit)
        self.menuPerson.addAction(self.act_add_person)

        self.retranslateUi(w_main)

        QMetaObject.connectSlotsByName(w_main)
    # setupUi

    def retranslateUi(self, w_main):
        w_main.setWindowTitle(QCoreApplication.translate("w_main", u"Sample Application", None))
        self.act_quit.setText(QCoreApplication.translate("w_main", u"Quit", None))
        self.act_add_person.setText(QCoreApplication.translate("w_main", u"Add Person", None))
        self.menuFile.setTitle(QCoreApplication.translate("w_main", u"File", None))
        self.menuPerson.setTitle(QCoreApplication.translate("w_main", u"Person", None))
    # retranslateUi

