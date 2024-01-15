import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initgui()


    def initgui(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('My App')
        self.count = 0

        self.label = QLabel(self)
        self.label.setText(str(self.count))
        self.label.move(40, 35)

        self.increase = QPushButton(self)
        self.increase.setText("Increase")
        self.increase.move(0, 0)
        self.increase.clicked.connect(self.increase_click)

        self.decrease = QPushButton(self)
        self.decrease.setText("Decrease")
        self.decrease.move(0, 70)
        self.decrease.clicked.connect(self.decrease_click)


    def increase_click(self):
        self.count+=1
        self.label.setText(str(self.count))

    def decrease_click(self):
        self.count-=1
        self.label.setText(str(self.count))


app = QApplication(sys.argv)
gui = MyWindow()
gui.show()
sys.exit(app.exec_())

