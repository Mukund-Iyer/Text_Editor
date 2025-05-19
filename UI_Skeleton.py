import sys
from PyQt5 import QtWidgets
from TextEditor import Ui_MainWindow # Replace 'untitled' with the name of your generated Python file
from PyQt5.QtWidgets import QFileDialog

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_triggers()
        self.show()# Ensure the main window is shown

    def connect_triggers(self):
        self.ui.ExitMenuItem.triggered.connect(self.exit_application)
        self.ui.Save_AsMenuItem.triggered.connect(self.save_as)
        self.ui.NewMenuItem.triggered.connect(self.new_file)
    
    def exit_application(self):
        # Define what happens when ExitMenuItem is triggered
        sys.exit()

    def save_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self,"Save As","","Text Files (*.txt);;All Files (*)", options=options)
        
        if file_name:
            # Get the text from plainTextEdit
            text = self.ui.plainTextEdit.toPlainText()
            # Write the text to the chosen file
            with open(file_name, 'w') as file:
                file.write(text)

    def new_file(self):
        self.ui.plainTextEdit.clear()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
