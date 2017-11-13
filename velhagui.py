import sys
import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title ='Velha Master'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.moves={n+1:{(a,b):" " for a in range(3) for b in range(3) } for n in range(9)}
        pprint.pprint(self.moves)
        self.initUI()
        self.Show()
    def Show(self):
        self.show()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 
        self.prinlayout = QHBoxLayout()
        n=1
        for a in range(1,4):
            self.windowLayout = QVBoxLayout()
            print(self.moves[n])
            [self.createGridLayout(n) for n in range(n,n+3)]
            self.prinlayout.addLayout(self.windowLayout)
            n=n+3
        self.setLayout(self.prinlayout)
    def move(self,n,x,y,player):
        self.moves[n][(x,y)]=player

    def createGridLayout(self,nome):
        self.horizontalGroupBox = QGroupBox(str(nome))
        layout = QGridLayout()
        layout.setColumnStretch(1, 6)
        n=0
        for x,y in ((x,y) for x in range(3) for y in range(3)):
            n=n+1
            layout.addWidget(QPushButton(self.moves[nome][(x,y)]),x,y)
        self.horizontalGroupBox.setLayout(layout)
        self.windowLayout.addWidget(self.horizontalGroupBox)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
