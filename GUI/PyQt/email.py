import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QMessageBox


class Email(QWidget):
    def __init__(self):
        super(Email, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0, 300,300)
        self.setWindowTitle("Email Parts")
        self.gridlayout = QGridLayout()

        self.label = QLabel("Email: ", self)
        self.lineedit = QLineEdit(self)

        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.submit_click)

        self.gridlayout.addWidget(self.label, 0,0)
        self.gridlayout.addWidget(self.lineedit, 0, 1, 1, 2)
        self.gridlayout.addWidget(self.button, 1,1)

        self.setLayout(self.gridlayout)

    def submit_click(self):
        print("hello")
        email = self.lineedit.text()
        print("1")
        username = email.split("@")[0]
        print("2")
        domain = email.split(".")[1]
        print("3")
        server = email.split("@")[1].split(".")[0]
        print("4")

        QMessageBox.information(self, "Message", f"email: {email}\nUsername: {username}\nDomain: {domain}\nServer: {server}", QMessageBox.Ok)


app = QApplication(sys.argv)
gui = Email()
gui.show()
sys.exit(app.exec_())
