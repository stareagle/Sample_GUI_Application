# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import icons_rc

class Ui_w_login(object):
    def setupUi(self, w_login):
        if not w_login.objectName():
            w_login.setObjectName(u"w_login")
        w_login.resize(393, 261)
        font = QFont()
        font.setPointSize(12)
        w_login.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/icons8-dollar-bills-94.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        w_login.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_cancel = QPushButton(w_login)
        self.pb_cancel.setObjectName(u"pb_cancel")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/icons8-cancel-94.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_cancel.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_cancel, 2, 1, 1, 1)

        self.groupBox = QGroupBox(w_login)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_userid = QLineEdit(self.groupBox)
        self.le_userid.setObjectName(u"le_userid")
        self.le_userid.setEchoMode(QLineEdit.EchoMode.Normal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_userid)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_password = QLineEdit(self.groupBox)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_password)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.pb_ok = QPushButton(w_login)
        self.pb_ok.setObjectName(u"pb_ok")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/icons8-tick-mark-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_ok.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_ok, 2, 0, 1, 1)

        self.lbl_message = QLabel(w_login)
        self.lbl_message.setObjectName(u"lbl_message")

        self.gridLayout.addWidget(self.lbl_message, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        QWidget.setTabOrder(self.le_userid, self.le_password)
        QWidget.setTabOrder(self.le_password, self.pb_ok)
        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)

        self.retranslateUi(w_login)

        QMetaObject.connectSlotsByName(w_login)
    # setupUi

    def retranslateUi(self, w_login):
        w_login.setWindowTitle(QCoreApplication.translate("w_login", u"Sample GUI", None))
        self.pb_cancel.setText(QCoreApplication.translate("w_login", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_login", u"Welcome Please Login", None))
        self.label.setText(QCoreApplication.translate("w_login", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("w_login", u"Password", None))
        self.pb_ok.setText(QCoreApplication.translate("w_login", u"OK", None))
        self.lbl_message.setText(QCoreApplication.translate("w_login", u"Message", None))
    # retranslateUi

