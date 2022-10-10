import sys
import time

from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtMultimedia import QSound

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QTextEdit

from Functions import Note, Harmony


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(70, 200)
        self.btn.clicked.connect(self.choose_ton)

        self.done = QPushButton('done', self)

        self.done.move(150, 200)
        self.done.clicked.connect(self.make)
        self.textEdit = QTextEdit(self)
        self.textEdit.move(70, 100)
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 200, 31))
        self.textEdit.setObjectName("textEdit")
        self.load_mp3('/Users/viacheslav/PycharmProjects/PyMusicProject/24-piano-keys/key14.mp3')
        self.tone = Note('C')
        self.s = QSound('24-piano-keys/key01.wav')

    def choose_ton(self):
        tone, ok_pressed = QInputDialog.getItem(
            self, "Выберите тональность", "Выберите тональность?",
            ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'), 0, False)
        self.tone = Note(tone)

    def make(self):
        filename = '24-piano-keys/key01.wav'
        self.s = QSound(filename)
        self.textEdit.setText(' '.join(Harmony(self.tone).harm))
        self.s.play()
        start_time = time.time()
        print(time.time() - start_time, self.player.duration())
        while time.time() - start_time < 0.5:
            continue
        self.player = QtMultimedia.QMediaPlayer()
        print(time.time() - start_time)


    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
