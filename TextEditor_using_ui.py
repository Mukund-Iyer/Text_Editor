from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("untitled.ui", self)  # Load the .ui file
        self.setWindowTitle("Text Editor")
        self.ExitMenuItem.triggered.connect(self.exit_application)
        self.Save_AsMenuItem.triggered.connect(self.save_as)
        self.NewMenuItem.triggered.connect(self.new_file)

    def exit_application(self):
        # Define what happens when ExitMenuItem is triggered
        sys.exit()

    def save_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)

        if file_name:
            # Get the text from plainTextEdit
            text = self.ui.plainTextEdit.toPlainText()
            # Write the text to the chosen file
            with open(file_name, 'w') as file:
                file.write(text)

    def new_file(self):
        self.ui.plainTextEdit.clear()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
