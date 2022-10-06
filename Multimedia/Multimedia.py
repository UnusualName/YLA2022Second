import sys

from player import Ui_Form
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.notes = []
        self.load_mp3(
            '/Users/viacheslav/Downloads/24-piano-keys/key01.mp3')
        self.playBtn.clicked.connect(self.notes[-1].play)
        self.pauseBtn.clicked.connect(self.notes[-1].play)
        self.stopBtn.clicked.connect(self.notes[-1].stop)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.notes.append(QtMultimedia.QMediaPlayer())
        self.notes[-1].setMedia(content)
        self.notes[-1].setDuration(100)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
