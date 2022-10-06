import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PIL_UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.imp)

        self.pushButton_2.clicked.connect(self.take)

        reg_ex = QRegExp("[1-3]{,1}")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]


    def imp(self):
        self.lcdNumber.display(self.lineEdit.text())
        self.lineEdit.setReadOnly(True)

    def take(self):
        self.lcdNumber.display(self.lcdNumber.value() - int(self.lineEdit_2.text()))
        self.listWidget.addItem(f'Игрок взял - {self.lineEdit_2.text()}')
        if self.lcdNumber.value() == 0:
            self.listWidget.addItem(f'Победа Игрока!')

        elif self.lcdNumber.value() % 4 == 0:
            self.listWidget.addItem(f'ИИ взял - 1')
            self.lcdNumber.display(self.lcdNumber.value() - 1)
        else:
            self.listWidget.addItem(f'ИИ взял - {int(self.lcdNumber.value() % 4)}')
            self.lcdNumber.display(self.lcdNumber.value() - self.lcdNumber.value() % 4)

        if self.lcdNumber.value() == 0:
            self.listWidget.addItem(f'Победа ИИ!')
            self.pushButton_2.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


