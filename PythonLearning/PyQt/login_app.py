import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QMessageBox


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(20,20,200,200)
        self.setWindowTitle("Login")

        self.gridlayout = QGridLayout()

        self.label1 = QLabel("Email", self)
        self.lineedit1 = QLineEdit(self)

        self.label2 = QLabel("Password", self)
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setEchoMode(QLineEdit.Password)

        self.button1 = QPushButton("Login", self)
        self.button1.clicked.connect(self.on_login_click)

        self.button2 = QPushButton("Clear", self)
        self.button2.clicked.connect(self.on_clear_click)

        self.gridlayout.addWidget(self.label1,0,0)
        self.gridlayout.addWidget(self.lineedit1, 0, 1, 1, 2)
        self.gridlayout.addWidget(self.label2,1,0)
        self.gridlayout.addWidget(self.lineedit2,1,1,1,2)
        self.gridlayout.addWidget(self.button1, 2,1)
        self.gridlayout.addWidget(self.button2, 2,2)

        self.setLayout(self.gridlayout)

    def on_login_click(self):
        email = self.lineedit1.text()
        password = self.lineedit2.text()

        if not email or not password:
            QMessageBox.warning(self, "Alert", "Please fill both the email and password", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Information", f"Login Successful!\nEmail: {email}\nPassword: {password}",
                                    QMessageBox.Ok)
            self.lineedit1.setText("")
            self.lineedit2.setText("")


    def on_clear_click(self):
        self.lineedit1.setText("")
        self.lineedit2.setText("")


app = QApplication(sys.argv)
gui = Login()
gui.show()
sys.exit(app.exec_())