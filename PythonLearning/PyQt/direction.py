import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initgui()


    def initgui(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('My App')

        self.label = QLabel(self)
        self.label.move(120,35)

        self.up = QPushButton(self)
        self.up.setText("up")
        self.up.move(80,0)
        self.up.clicked.connect(self.up_click)

        self.down = QPushButton(self)
        self.down.setText("down")
        self.down.move(80, 70)
        self.down.clicked.connect(self.down_click)

        self.left = QPushButton(self)
        self.left.setText("left")
        self.left.move(0, 35)
        self.left.clicked.connect(self.left_click)

        self.right = QPushButton(self)
        self.right.setText("right")
        self.right.move(150, 35)
        self.right.clicked.connect(self.right_click)

    def up_click(self):
        self.label.setText("up")

    def down_click(self):
        self.label.setText("down")

    def left_click(self):
        self.label.setText("left")

    def right_click(self):
        self.label.setText("right")


app = QApplication(sys.argv)
gui = MyWindow()
gui.show()
sys.exit(app.exec_())

