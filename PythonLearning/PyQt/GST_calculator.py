import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QGridLayout, QMessageBox


class Calculate(QWidget):
    def __init__(self):
        super(Calculate, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(40,40, 400,400)
        self.setWindowTitle("GST Calculator")

        self.gridlayout = QGridLayout()

        self.category ="Mobile Phone"

        self.label1 = QLabel("Product Name: ", self)
        self.lineedit1 = QLineEdit(self)

        self.label2 = QLabel("Category: ")
        self.combobox = QComboBox(self)
        self.combobox.addItem("Mobile Phone")
        self.combobox.addItem("AC")
        self.combobox.addItem("Radio")
        self.combobox.activated[str].connect(self.combo)


        self.label3 = QLabel("Price: ")
        self.lineedit2 = QLineEdit(self)

        self.submit = QPushButton("Calculate GST", self)
        self.submit.clicked.connect(self.on_submit)

        self.gridlayout.addWidget(self.label1, 0,0)
        self.gridlayout.addWidget(self.lineedit1, 0,1,1,2)

        self.gridlayout.addWidget(self.label2, 1,0)
        self.gridlayout.addWidget(self.combobox, 1, 1)

        self.gridlayout.addWidget(self.label3, 2, 0)
        self.gridlayout.addWidget(self.lineedit2, 2, 1, 1, 2)

        self.gridlayout.addWidget(self.submit, 3, 1)

        self.setLayout(self.gridlayout)

    def combo(self, text):
        self.category = text

    def on_submit(self, text):
        product = self.lineedit1.text()
        price = int(self.lineedit2.text())
        gst = 0

        print(self.category, type(self.category))

        if self.category == "Mobile Phone":
            gst = 0.18*price
        elif self.category == "AC":
            gst = 0.28*price
        else:
            gst = 0.12*price

        QMessageBox.information(self, "GST", f"Price and GST for {product}:\n\n"
                                             f"Price without GST: {price}\n"
                                             f"GST: {gst}\n"
                                             f"Price with GST: {price+gst}", QMessageBox.Ok)


app = QApplication(sys.argv)
gui = Calculate()
gui.show()
sys.exit(app.exec_())
