import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

MATR = [[1 for i in range(8)] if j % 2 == 0 else [0 for i in range(8)] for j in range(11)]


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        i = 0
        self.n = [chr(i) for i in range(100)]
        for x in range(len(MATR)):
            for y in range(len(MATR[x])):
                if MATR[x][y] == 1:
                    self.n[i] = QPushButton('*', self)
                    self.n[i].resize(40, 40)
                    self.n[i].move(32 * x, y * 32)
                    i += 1
                    self.setGeometry(300, 300, 38 * x, 38 * y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
