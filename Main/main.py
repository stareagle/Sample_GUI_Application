import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Main.UI.main_window import Ui_w_main
from Application_Login.login import LoginForm
from Persons.add_person import AddPerson

class MainWindow(qtw.QMainWindow, Ui_w_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.act_quit.triggered.connect(self.close)
        self.act_add_person.triggered.connect(self.open_person_dialog)

        self.form = LoginForm()
        self.form.login_success.connect(self.show)
        self.form.show()


    @qtc.Slot()
    def open_person_dialog(self):
        self.form = AddPerson()
        self.form.exec()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
