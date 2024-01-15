import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class MyCalculator(QWidget):
    def __init__(self):
        super(MyCalculator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(260,410)
        self.setWindowTitle("Calculator")

        self.display_value = "0"
        self.first_number = "0"
        self.second_number = "0"
        self.operator = "+"

        self.label_cal_entry = QLabel(self.display_value, self)
        self.label_cal_entry.setGeometry(0,0, 260, 90)
        self.label_cal_entry.setContentsMargins(0,0,0,0)
        self.label_cal_entry.setFont(QFont("Helvetica", 30))
        self.label_cal_entry.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.label_cal_entry.setStyleSheet("QWidget{color:white; background-color:#212121; padding:10px}")

        self.button_ac = self.create_button("AC", 0, 90, "#505050")
        self.button_pm = self.create_button(chr(177), 65, 90, "#505050")
        self.button_per = self.create_button("%", 130, 90, "#505050")
        self.button_div = self.create_button(chr(247), 195, 90, "#ff9800")

        self.button_7 = self.create_button("7", 0, 155, "#757575")
        self.button_8 = self.create_button("8", 65, 155, "#757575")
        self.button_9 = self.create_button("9", 130, 155, "#757575")
        self.button_mul = self.create_button("x", 195, 155, "#ff9800")

        self.button_6 = self.create_button("6", 0, 220, "#757575")
        self.button_5 = self.create_button("5", 65, 220, "#757575")
        self.button_4 = self.create_button("4", 130, 220, "#757575")
        self.button_min = self.create_button("-", 195, 220, "#ff9800")

        self.button_3 = self.create_button("3", 0, 285, "#757575")
        self.button_2 = self.create_button("2", 65, 285, "#757575")
        self.button_1 = self.create_button("1", 130, 285, "#757575")
        self.button_pl = self.create_button("+", 195, 285, "#ff9800")

        self.button_0 = self.create_button("0", 0, 350, "#757575", 130)
        self.button_dec = self.create_button(".", 130, 350, "#757575")
        self.button_eq = self.create_button("=", 195, 350, "#ff9800")

        self.button_0.clicked.connect(self.button_pressed)
        self.button_1.clicked.connect(self.button_pressed)
        self.button_2.clicked.connect(self.button_pressed)
        self.button_3.clicked.connect(self.button_pressed)
        self.button_4.clicked.connect(self.button_pressed)
        self.button_5.clicked.connect(self.button_pressed)
        self.button_6.clicked.connect(self.button_pressed)
        self.button_7.clicked.connect(self.button_pressed)
        self.button_8.clicked.connect(self.button_pressed)
        self.button_9.clicked.connect(self.button_pressed)
        self.button_dec.clicked.connect(self.button_pressed)
        self.button_pm.clicked.connect(self.button_pressed)
        self.button_per.clicked.connect(self.button_pressed)
        self.button_ac.clicked.connect(self.button_pressed)
        self.button_pl.clicked.connect(self.button_pressed)
        self.button_min.clicked.connect(self.button_pressed)
        self.button_mul.clicked.connect(self.button_pressed)
        self.button_div.clicked.connect(self.button_pressed)
        self.button_eq.clicked.connect(self.button_pressed)

    def create_button(self, text, x, y,bg_color, width=65):
        button = QPushButton(text, self)
        button.setGeometry(x, y, width, 65)
        button.setContentsMargins(0,0,0,0)
        button.setFont(QFont("Helvetica", 13))
        button.setStyleSheet("QWidget{color:white; background-color:%s; padding:10px}"%(bg_color))
        return button

    def button_pressed(self):
        sender_text = self.sender().text()
        try:
            if sender_text == '.' and not '.' in self.display_value and len(self.display_value) < 8:
                self.display_value +=sender_text
            elif sender_text == chr(177) and self.display_value != '0':
                self.display_value = format(float(self.display_value)*-1, '.12g')
            elif sender_text == '0' and '.' in self.display_value and len(self.display_value) < 8:
                self.display_value+=sender_text
            elif sender_text == '%':
                self.display_value = format(float(self.display_value)/100, '.8g')
            elif sender_text in "1234567890" and len(self.display_value) < 8:
                self.display_value = format(float(self.display_value + sender_text), '.8g')
            elif sender_text == "AC":
                self.display_value = "0"
                self.first_number = "0"
                self.second_number = "0"
                self.operator = "+"
            elif sender_text == "+":
                self.first_number = self.display_value
                self.operator = "+"
                self.display_value = "0"
            elif sender_text == "-":
                self.first_number = self.display_value
                self.operator = "-"
                self.display_value = "0"
            elif sender_text == "x":
                self.first_number = self.display_value
                self.operator = "*"
                self.display_value = "0"
            elif sender_text == chr(247):
                self.first_number = self.display_value
                self.operator = "/"
                self.display_value = "0"
            elif sender_text == "=":
                self.second_number = self.display_value
                self.display_value = format(eval(self.first_number+self.operator+self.second_number), ".8g")

            if sender_text not in ["+", "-", "x", chr(247)]:
                self.label_cal_entry.setText(self.display_value)
            else:
                self.label_cal_entry.setText(sender_text)
        except ZeroDivisionError as ze:
            self.label_cal_entry.setText("Error")
            print("ZeroDivisionError:", ze)
            self.display_value = "0"
            self.first_number = "0"
            self.second_number = "0"
            self.operator = "+"
        except Exception as e:
            self.label_cal_entry.setText("Error")
            print("Exception:", e)



app = QApplication(sys.argv)
gui = MyCalculator()
gui.show()
sys.exit(app.exec_())
