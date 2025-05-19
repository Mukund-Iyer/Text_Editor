from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class ImageMaskWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Load image
        pixmap = QPixmap("Futuristic_UI.png")
        scaled_pixmap = pixmap.scaled(800, 600, Qt.KeepAspectRatio,Qt.SmoothTransformation)  # Adjust to your preferred size
        self.resize(scaled_pixmap.size())

        if pixmap.isNull():
            print("Failed to load image.")
            return

        # Set up QLabel to show the image
        label = QLabel(self)
        label.setPixmap(scaled_pixmap)
        label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        self.resize(pixmap.size())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageMaskWindow()
    window.show()
    sys.exit(app.exec_())