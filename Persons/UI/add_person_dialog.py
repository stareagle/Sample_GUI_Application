# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import icons_rc

class Ui_d_person(object):
    def setupUi(self, d_person):
        if not d_person.objectName():
            d_person.setObjectName(u"d_person")
        d_person.setWindowModality(Qt.WindowModality.ApplicationModal)
        d_person.resize(487, 232)
        icon = QIcon()
        icon.addFile(u":/Main/icons8-dollar-bills-94.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        d_person.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_person)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_close = QPushButton(d_person)
        self.pb_close.setObjectName(u"pb_close")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/icons8-cancel-94.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_close.setIcon(icon1)
        self.pb_close.setAutoDefault(False)

        self.gridLayout.addWidget(self.pb_close, 2, 2, 1, 1)

        self.pb_submit = QPushButton(d_person)
        self.pb_submit.setObjectName(u"pb_submit")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/icons8-tick-mark-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_submit.setIcon(icon2)
        self.pb_submit.setAutoDefault(False)

        self.gridLayout.addWidget(self.pb_submit, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.gbx_person = QGroupBox(d_person)
        self.gbx_person.setObjectName(u"gbx_person")
        self.gbx_person.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.gbx_person)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gbx_person)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_firstname = QLineEdit(self.gbx_person)
        self.le_firstname.setObjectName(u"le_firstname")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_firstname)

        self.label_2 = QLabel(self.gbx_person)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_lastname = QLineEdit(self.gbx_person)
        self.le_lastname.setObjectName(u"le_lastname")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_lastname)


        self.gridLayout.addWidget(self.gbx_person, 0, 0, 1, 3)

        self.lbl_message = QLabel(d_person)
        self.lbl_message.setObjectName(u"lbl_message")

        self.gridLayout.addWidget(self.lbl_message, 3, 0, 1, 2)


        self.retranslateUi(d_person)

        self.pb_submit.setDefault(True)


        QMetaObject.connectSlotsByName(d_person)
    # setupUi

    def retranslateUi(self, d_person):
        d_person.setWindowTitle(QCoreApplication.translate("d_person", u"Sample Application", None))
        self.pb_close.setText(QCoreApplication.translate("d_person", u"Close", None))
        self.pb_submit.setText(QCoreApplication.translate("d_person", u"Submit", None))
        self.gbx_person.setTitle(QCoreApplication.translate("d_person", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("d_person", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("d_person", u"Last Name", None))
        self.lbl_message.setText(QCoreApplication.translate("d_person", u"Message", None))
    # retranslateUi

