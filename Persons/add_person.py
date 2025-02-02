import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Persons.UI.add_person_dialog import Ui_d_person

class AddPerson(qtw.QDialog, Ui_d_person):
    def __init__(self, parent=None):
        qtw.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.le_firstname.setFocus()
        self.gbx_person.setTitle("Add Person")
        self.lbl_message.clear()
        self.pb_close.clicked.connect(self.reject)

        self.pb_submit.clicked.connect(self.process_entry)

    @qtc.Slot()
    def process_entry(self):
        self.lbl_message.setText(self.le_firstname.text() + " " +
                                 self.le_lastname.text() + " "
                                 'has been added')
        self.le_lastname.clear()
        self.le_firstname.clear()

        self.le_firstname.setFocus()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = AddPerson()
    window.open()

    sys.exit(app.exec_())