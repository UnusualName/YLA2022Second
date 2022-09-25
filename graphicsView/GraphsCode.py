import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from Graphs_UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.radioButton.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)], [i for i in range(10)], pen='r')
        elif self.radioButton_2.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)], [i ** 2 for i in range(10)], pen='g')
        elif self.radioButton_3.isChecked():
            self.graphicsView.clear()
            self.graphicsView.plot([i for i in range(10)], [i ** 3 for i in range(10)], pen='b')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())