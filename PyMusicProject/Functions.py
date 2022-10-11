from PyQt5 import QtMultimedia
from PyQt5 import QtCore


class Note:
    def __init__(self, pitch):
        self.pitch = pitch
        self.STAN = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __int__(self):
        return self.STAN.index(self.pitch)

    def __add__(self, other):
        return self.STAN[(int(self) + other) % len(self.STAN)]

    def lower_file(self):
        filenum = str((int(self) + 7) + 1)
        filename = '/Users/viacheslav/PycharmProjects/YLA2022Second/PyMusicProject/24-piano-keys/key' + filenum.rjust(2, '0') + '.mp3'
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        return content


class Harmony:
    def __init__(self, tone, lad=1):
        self.C_MAJ_LAD = (2, 2, 1, 2, 2, 2, 1)
        self.tone = tone
        self.lad = lad
        self.harm = [tone + sum(self.C_MAJ_LAD[:i]) for i in range(7)]
