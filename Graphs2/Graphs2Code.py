import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Graphs2 import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.lineEdit.text()[0] == 'x':
            a = '1'
        else:
            a = ''
        self.graphicsView.plot([x for x in range(int(self.lineEdit_2.text().split()[0]),
                                                 int(self.lineEdit_2.text().split()[1]))],
                               [eval(a + self.lineEdit.text().replace('x', '*x')) for x in
                                range(int(self.lineEdit_2.text().split()[0]),
                                      int(self.lineEdit_2.text().split()[1]))], pen='b')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
