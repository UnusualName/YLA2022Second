import sys
from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QInputDialog, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(70, 200)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        n, ok_pressed = QInputDialog.getInt(
            self, "Введите количество...", "Сколько цветов?",
            3, 1, 6, 1)
        self.n = n
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(self.n):
            qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            qp.drawRect(30, 30 + 30 * i, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
