import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtCore
from classy import *



class Window(QWidget):
    def __init__(self):
        super().__init__()
        f = open('stylesheet', 'r')  # это для стилей потом все скину
        self.styleData = f.read()
        f.close()
        self.title = 'Генератор заголовков'
        self.setStyleSheet(self.styleData)  # это для стилей потом все скину
        self.initUI()

    # задал по сути оптимальные размеры для элементов
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(400, 100, 800, 500)
        self.button = QPushButton('Генерировать', self)
        self.button.move(310, 260)
        self.button.clicked.connect(self.one)
        '''
        self.qle2 = QPlainTextEdit(self)
        self.qle2.setFont(QFont("Times", 10, QFont.Bold))  # тут изменяется шрифт
        self.qle2.move(5, 351)
        '''
        self.qle = QPlainTextEdit(self)
        self.qle.resize(790, 200)
        #self.qle2.resize(790, 145)
        self.qle.move(5, 50)
        self.lbl_title_1 = QLabel(self)
        self.lbl_title_2 = QLabel(self)
        self.lbl = QLabel(self)
        self.lbl_title_1.move(5, 2)
        self.lbl_title_1.setFont(QFont("Times", 30, QFont.Bold))
        self.lbl_title_1.setText("Статья")
        self.lbl_title_2.move(5, 301)
        self.lbl_title_2.setFont(QFont("Times", 30, QFont.Bold))
        self.lbl_title_2.setText("Заголовок")
        self.lbl.move(10, 401)
        self.lbl.setFont(QFont("Arial", 30, QFont.Bold))
        self.show()

    def one(self):
        text = self.qle.toPlainText()  # тут заберается текст из формы
        self.lbl.setText(newdoc(text))  # тут присваеватся значение лейблу
        self.lbl.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())