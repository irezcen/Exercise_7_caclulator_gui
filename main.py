import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import numpy as np
import math

class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.top = 300
        self.left = 300
        self.height = 500
        self.width = 400
        self.przyciski = np.full(16, QPushButton(parent=self))
        self.okno = QLineEdit(self)
        self.okno.setReadOnly(True)
        self.title = 'Kalkulator'
        self.setWindowTitle(self.title)
        for i in range(0, 15, 1):
            self.przyciski[i] = QPushButton(parent=self)
            self.przyciski[i].move(125 + i%3 * 50, 100 +  math.floor(i/3)* 50)
            self.przyciski[i].resize(50, 50)
        self.przyciski[15].move(125, 350)
        self.przyciski[15].resize(150, 50)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.okno.move(125, 75)
        self.okno.resize(150, 20)
        self.przyciski[0].setText('1')
        self.przyciski[1].setText('2')
        self.przyciski[2].setText('3')
        self.przyciski[3].setText('4')
        self.przyciski[4].setText('5')
        self.przyciski[5].setText('6')
        self.przyciski[6].setText('7')
        self.przyciski[7].setText('8')
        self.przyciski[8].setText('9')
        self.przyciski[9].setText('0')
        self.przyciski[10].setText('+')
        self.przyciski[11].setText('-')
        self.przyciski[12].setText('*')
        self.przyciski[13].setText('/')
        self.przyciski[14].setText('C')
        self.przyciski[15].setText('=')
        
        self.przyciski[0].clicked.connect(lambda: self.click_liczby(0))
        self.przyciski[1].clicked.connect(lambda: self.click_liczby(1))
        self.przyciski[2].clicked.connect(lambda: self.click_liczby(2))
        self.przyciski[3].clicked.connect(lambda: self.click_liczby(3))
        self.przyciski[4].clicked.connect(lambda: self.click_liczby(4))
        self.przyciski[5].clicked.connect(lambda: self.click_liczby(5))
        self.przyciski[6].clicked.connect(lambda: self.click_liczby(6))
        self.przyciski[7].clicked.connect(lambda: self.click_liczby(7))
        self.przyciski[8].clicked.connect(lambda: self.click_liczby(8))
        self.przyciski[9].clicked.connect(lambda: self.click_liczby(9))
        self.przyciski[10].clicked.connect(self.dodaj)
        self.przyciski[11].clicked.connect(self.odejmij)
        self.przyciski[12].clicked.connect(self.pomnoz)
        self.przyciski[13].clicked.connect(self.podziel)
        self.przyciski[14].clicked.connect(self.wyczysc)
        self.przyciski[15].clicked.connect(self.rownanie)

        self.show()

    def click_liczby(self, liczba):
        cyfra = liczba + 1
        if cyfra == 10:
            cyfra = 0
        nowy_tekst = self.okno.text() + str(cyfra)
        self.okno.setText(nowy_tekst)
    
    def dodaj(self):
        nowy_tekst = self.okno.text() + "+"
        self.okno.setText(nowy_tekst)

    def odejmij(self):
        nowy_tekst = self.okno.text() + "-"
        self.okno.setText(nowy_tekst)

    def pomnoz(self):
        nowy_tekst = self.okno.text() + "*"
        self.okno.setText(nowy_tekst)
    
    def podziel(self):
        nowy_tekst = self.okno.text() + "/"
        self.okno.setText(nowy_tekst)

    def rownanie(self):
        wynik = self.okno.text()
        wynik = eval(wynik)
        self.okno.setText(str(eval(self.okno.text())))

    def wyczysc(self):
        self.okno.clear()


    
        

app = QApplication(sys.argv)
ex = Kalkulator()
app.exec_()
