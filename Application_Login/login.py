import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_Login.UI.login_window import Ui_w_login

class LoginForm(qtw.QWidget, Ui_w_login):

    login_success = qtc.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.process_login)

    @qtc.Slot()
    def process_login(self):
        if self.le_userid.text() == 'Me' and self.le_password.text() == 'silly':
            self.login_success.emit()
            self.close()
        else:
            self.lbl_message.setText("Login incorrect")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec_())
