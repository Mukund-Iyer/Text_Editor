from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QFileDialog
import webbrowser

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.loaded_file = ""
        uic.loadUi("untitled.ui", self)  # Load the .ui file
        self.setWindowTitle("Text Editor")
        self.OpenMenuItem.triggered.connect(self.open_file)
        self.ExitMenuItem.triggered.connect(self.exit_application)
        self.Save_AsMenuItem.triggered.connect(self.save_as)
        self.NewMenuItem.triggered.connect(self.new_file)
        self.Help_MenuItem.triggered.connect(self.open_help)
        self.SaveMenuItem.triggered.connect(self.save)

    def exit_application(self):
        # Define what happens when ExitMenuItem is triggered
        sys.exit()

    def save_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)

        if file_name:
            # Get the text from plainTextEdit
            text = self.plainTextEdit.toPlainText()
            # Write the text to the chosen file
            with open(file_name, 'w') as file:
                file.write(text)
                self.loaded_file = file_name
                self.setWindowTitle("Text Editor - " + file_name)

    def save(self):
        if self.loaded_file != "" and self.loaded_file:
            text = self.plainTextEdit.toPlainText()
            with open(self.loaded_file,'w') as file:
                file.write(text)
        else:
            self.save_as()

    def new_file(self):
        self.plainTextEdit.clear()
        self.setWindowTitle("Text Editor")
        self.loaded_file = ""

    def open_file(self):
        option = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self,"Open...","","Text Files (*.txt);;All Files (*)",options=option)
        if file_name:
            with open(file_name, 'r') as file:
                text = file.read()
                self.plainTextEdit.setPlainText(text)
                self.setWindowTitle("Text Editor - " + file_name)
                self.loaded_file = file_name

    def open_help(self):
        site_url = "https://github.com/Mukund-Iyer/Text_Editor/tree/Text_Editor_Only"
        webbrowser.open(site_url)


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
