import sys

from PIL import Image
from PIL.ImageQt import ImageQt, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PILUI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        self.orig = Image.open(self.fname)
        self.now = Image.open(self.fname)
        self.a = ImageQt(self.now)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)
        self.pushButton_1.clicked.connect(self.set)
        self.pushButton_2.clicked.connect(self.set)
        self.pushButton_3.clicked.connect(self.set)
        self.pushButton_4.clicked.connect(self.set)
        self.pushButton_5.clicked.connect(self.rotate)
        self.pushButton_6.clicked.connect(self.rotate)

    def set(self):
        self.now = self.orig.copy()
        pixels = self.now.load()
        x, y = self.now.size
        if self.sender().objectName()[-1] != '4':
            for i in range(x):
                for j in range(y):
                    rgb = [0, 0, 0]
                    rgb[int(self.sender().objectName()[-1]) - 1] = pixels[i, j][
                        int(self.sender().objectName()[-1]) - 1]
                    pixels[i, j] = tuple(rgb)

        self.a = ImageQt(self.now)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def rotate(self):
        self.orig = self.orig.rotate(90 - 180 * (int(self.sender().objectName()[-1]) - 5),
                                     expand=True)
        self.now = self.now.rotate(90 - 180 * (int(self.sender().objectName()[-1]) - 5), expand=True)
        self.a = ImageQt(self.now)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
