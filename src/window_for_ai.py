import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore
from classy import *



class Window(QWidget):
    def __init__(self):
        super().__init__()
        # f = open('resources/stylesheet', 'r') # это для стилей потом все скину
        # self.styleData = f.read()
        # f.close()
        self.title = 'Генератор заголовков'
        # self.setStyleSheet(self.styleData) # это для стилей потом все скину
        self.initUI()

    # задал по сути оптимальные размеры для элементов
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(400, 100, 500, 400)
        self.button = QPushButton('Генерировать', self)
        self.button.move(195, 210)
        self.button.clicked.connect(self.one)
        self.lbl = QLabel(self)
        self.lbl.setFont(QFont("Times", 50, QFont.Bold))  # тут изменяется шрифт
        self.lbl.move(10, 230)
        self.qle = QPlainTextEdit(self)
        self.qle.resize(490, 200)
        self.qle.move(5, 5)

        self.show()

    def one(self):
        text = self.qle.toPlainText()  # тут заберается текст из формы
        self.lbl.setText(newdoc(text))  # тут присваеватся значение лейблу
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
