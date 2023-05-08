import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.grid()

    def hbox(self):
        self.setGeometry(20,20,500,500)
        self.setWindowTitle("HBox Application")

        self.hboxlayout = QHBoxLayout()

        self.button1 = QPushButton("Click 1",self)
        self.button2 = QPushButton("Click 2", self)
        self.button3 = QPushButton("Click 3", self)
        self.button4 = QPushButton("Click 4", self)

        self.hboxlayout.addWidget(self.button1)
        self.hboxlayout.addStretch(1)
        self.hboxlayout.addWidget(self.button2)
        self.hboxlayout.addStretch(2)
        self.hboxlayout.addWidget(self.button3)
        self.hboxlayout.addStretch(5)
        self.hboxlayout.addWidget(self.button4)

        self.setLayout(self.hboxlayout)
        
    def vbox(self):
        self.setGeometry(20,20,500,500)
        self.setWindowTitle("VBox Application")

        self.vboxlayout = QVBoxLayout()

        self.button1 = QPushButton("Click 1",self)
        self.button2 = QPushButton("Click 2", self)
        self.button3 = QPushButton("Click 3", self)
        self.button4 = QPushButton("Click 4", self)

        self.vboxlayout.addWidget(self.button1)
        self.vboxlayout.addStretch(1)
        self.vboxlayout.addWidget(self.button2)
        self.vboxlayout.addStretch(2)
        self.vboxlayout.addWidget(self.button3)
        self.vboxlayout.addStretch(5)
        self.vboxlayout.addWidget(self.button4)

        self.setLayout(self.vboxlayout)

    def combo(self):
        self.setGeometry(20,20,500,500)
        self.setWindowTitle("VBox Application")

        self.hboxlayout = QHBoxLayout()
        self.vboxlayout = QVBoxLayout()

        self.button1 = QPushButton("Click 1",self)
        self.button2 = QPushButton("Click 2", self)
        self.button3 = QPushButton("Click 3", self)
        self.button4 = QPushButton("Click 4", self)

        self.hboxlayout.addWidget(self.button1)
        self.hboxlayout.addWidget(self.button2)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.vboxlayout.addWidget(self.button3)
        self.vboxlayout.addWidget(self.button4)

        self.setLayout(self.vboxlayout)

    def combo2(self):
        self.setGeometry(20,20,500,500)
        self.setWindowTitle("VBox Application")

        self.hboxlayout = QHBoxLayout()
        self.vboxlayout = QVBoxLayout()

        self.button1 = QPushButton("Click 1",self)
        self.button2 = QPushButton("Click 2", self)

        self.hboxlayout.addWidget(self.button1)
        self.hboxlayout.addWidget(self.button2)
        self.hboxlayout.addStretch(1)
        self.vboxlayout.addStretch(1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.setLayout(self.vboxlayout)

    def grid(self):
        self.setGeometry(20, 20, 500, 500)
        self.setWindowTitle("VBox Application")

        self.gridlayout = QGridLayout()

        self.button1 = QPushButton("Click 1", self)
        self.button2 = QPushButton("Click 2", self)
        self.button3 = QPushButton("Click 3", self)
        self.button4 = QPushButton("Click 4", self)

        self.gridlayout.addWidget(self.button1, 1, 0)
        self.gridlayout.addWidget(self.button2, 2, 5)
        self.gridlayout.addWidget(self.button3, 4, 5)
        self.gridlayout.addWidget(self.button4, 7, 1)

        self.setLayout(self.gridlayout)



app = QApplication(sys.argv)
gui = MyWindow()
gui.show()
sys.exit(app.exec_())