import sys

from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QFileDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        self.current = Image.open(self.fname)
        self.new_img = 'new.png'
        self.initUI()
        self.alpha.valueChanged.connect(self.change_alpha)

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Изменение прозрачности')

        # Изображение
        self.pixmap = QPixmap(self.fname)
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)

        self.alpha = QSlider(self)
        self.alpha.move(20, 30)
        self.alpha.resize(20, 300)
        self.alpha.setMinimum(0)
        self.alpha.setMaximum(255)
        self.alpha.setValue(255)

    def change_alpha(self):
        img = self.current
        img.putalpha(int(self.alpha.value()))
        img.save(self.new_img)
        self.image.setPixmap(QPixmap(self.new_img))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
