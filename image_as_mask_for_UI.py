from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QRegion
from PyQt5.QtCore import Qt
import sys

class ImageMaskWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Load image
        pixmap = QPixmap("Futuristic_UI.png")
        if pixmap.isNull():
            print("Failed to load image.")
            return

        self.resize(pixmap.size())

        # Create a mask from the alpha channel (transparency)
        mask = pixmap.createMaskFromColor(Qt.transparent, Qt.MaskOutColor)
        self.setMask(QRegion(mask))

        # Set the image as the background
        self.setStyleSheet("background-image: url(Futuristic_UI.png);")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageMaskWindow()
    window.show()
    sys.exit(app.exec_())
