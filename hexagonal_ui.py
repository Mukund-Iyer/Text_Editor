from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtGui import QPolygon, QRegion
import sys
import math

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        uic.loadUi("untitled.ui", self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Text Editor")

        # Delay hexagon shape until window is shown
        QTimer.singleShot(0, self.set_hexagon_shape)

        self.ExitMenuItem.triggered.connect(self.exit_application)
        self.Save_AsMenuItem.triggered.connect(self.save_as)
        self.NewMenuItem.triggered.connect(self.new_file)

    def set_hexagon_shape(self):
        w, h = self.width(), self.height()
        r = min(w, h) // 2 - 10
        cx, cy = w // 2, h // 2 + 20  # Shift center down to make room for toolbar

        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            x = cx + r * math.cos(angle_rad)
            y = cy + r * math.sin(angle_rad)
            points.append(QPoint(int(x), int(y)))

        hexagon = QPolygon(points)
        self.setMask(QRegion(hexagon))

    def resizeEvent(self, event):
        self.set_hexagon_shape()
        super().resizeEvent(event)

    def exit_application(self):
        QtWidgets.QApplication.quit()

    def save_as(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save As", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            text = self.plainTextEdit.toPlainText()
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(text)

    def new_file(self):
        self.plainTextEdit.clear()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
