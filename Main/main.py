import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Main.UI.main_window import Ui_w_main
from Persons.UI.add_person_dialog import Ui_d_person

class MainWindow(qtw.QMainWindow, Ui_w_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.act_quit.triggered.connect(self.close)
        self.act_add_person.triggered.connect(self.open_person_dialog)

    def open_person_dialog(self):
        print("Dialog Opened")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
