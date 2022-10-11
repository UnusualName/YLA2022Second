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
        self.player = QtMultimedia.QMediaPlayer()
        self.done = QPushButton('done', self)
        self.done.move(150, 200)
        self.done.clicked.connect(self.make)

        self.uu = QPushButton('uu', self)
        self.uu.move(200, 200)
        self.uu.clicked.connect(self.player.play)

        self.textEdit = QTextEdit(self)
        self.textEdit.move(70, 100)
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 200, 31))
        self.textEdit.setObjectName("textEdit")

        self.tone = Note('C')
        self.s = QSound('24-piano-keys/key01.wav')
        self.playlist = QtMultimedia.QMediaPlaylist(self.player)

    def choose_ton(self):
        tone, ok_pressed = QInputDialog.getItem(
            self, "Выберите тональность", "Выберите тональность?",
            ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'), 0, False)
        self.tone = Note(tone)

    def make(self):
        for i in Harmony(self.tone).harm:
            self.playlist.addMedia(Note(i).lower_file())
            print(Note(i).lower_file())
        self.player.setPlaylist(self.playlist)
        self.player.play()
        print(self.playlist.media(1))

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
