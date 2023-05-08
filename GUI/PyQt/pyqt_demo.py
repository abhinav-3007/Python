import sys
from PyQt5.QtCore import QSize, Qt, QDateTime
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QAction, QMessageBox, \
    QCheckBox, QProgressBar, QComboBox, QFontDialog, QColorDialog, QDateEdit, QLineEdit, QSlider, QRadioButton, \
    QSpinBox


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initgui()


    def initgui(self):
        self.setGeometry(0, 30, 750, 750)
        self.setWindowTitle('My App')
        self.count = 0

        self.color = QColor(0,0,0)
        self.bgcolor = QColor(255,255,255)

        self.label = QLabel(self)
        self.label.setText("Clicked 0")
        self.label.setStatusTip("Number of times clicked")
        self.label.move(40,85)

        self.button1 = QPushButton(self)
        self.button1.setText("Click Me")
        self.button1.move(0, 50)
        self.button1.setStatusTip("Click the button to increase value")
        self.button1.setShortcut("Shift+C")
        self.button1.clicked.connect(self.on_button_click)

        self.button2 = QPushButton(self)
        self.button2.setText("Quit")
        self.button2.move(0, 120)
        self.button2.setStatusTip("Click to quit")
        self.button2.setShortcut("Ctrl+Q")
        self.button2.clicked.connect(self.closeEvent)

        self.checkbox = QCheckBox('Enlarge Window', self)
        self.checkbox.move(0,155)
        self.checkbox.stateChanged.connect(self.enlarge_window)

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(0,190,150,20)

        self.pbtn = QPushButton("Transfer", self)
        self.pbtn.move(175, 190)
        self.pbtn.clicked.connect(self.start_transfer)

        self.label2 = QLabel("Games", self)
        self.label2.move(0, 230)
        self.label2.setStyleSheet('QWidget{color:red; background-color:blue;}')

        self.combobox = QComboBox(self)
        self.combobox.addItem("Minecraft")
        self.combobox.addItem("Roblox")
        self.combobox.addItem("Fortnite")
        self.combobox.addItem("FIFA20")
        self.combobox.addItem("Call of Duty")
        self.combobox.move(200, 230)
        self.combobox.activated[str].connect(self.name_the_game)

        self.dateEdit = QDateEdit(self, calendarPopup=True)
        self.dateEdit.move(300, 430)
        self.dateEdit.setDateTime(QDateTime.currentDateTime())

        self.nameLabel = QLabel("name:",self)
        self.nameLabel.move(100, 470)

        self.LineEdit = QLineEdit(self)
        self.LineEdit.move(200,470)

        self.nameButton = QPushButton("Enter",self)
        self.nameButton.move(300,470)
        self.nameButton.clicked.connect(self.show_name)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(500, 500, 30, 200)
        self.slider.setRange(0,10)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.valueChanged[int].connect(self.slider_value)

        self.radiobutton1 = QRadioButton("Radio1", self)
        self.radiobutton1.move(50, 600)
        self.radiobutton1.toggled.connect(lambda: self.radio_clicked(self.radiobutton1))

        self.radiobutton2 = QRadioButton("Radio2", self)
        self.radiobutton2.move(50, 650)
        self.radiobutton2.toggled.connect(lambda: self.radio_clicked(self.radiobutton2))

        self.checklist = ["",""]

        self.checkbox1 = QCheckBox("check1", self)
        self.checkbox1.move(50, 675)
        self.checkbox1.stateChanged.connect(lambda: self.check_clicked(self.checkbox1))

        self.checkbox2 = QCheckBox("check2", self)
        self.checkbox2.move(50, 700)
        self.checkbox2.stateChanged.connect(lambda: self.check_clicked(self.checkbox2))

        self.spinbox = QSpinBox(self)
        self.spinbox.setGeometry(50, 750, 200, 30)
        self.spinbox.valueChanged.connect(self.spinbox_value)
        self.spinbox.setRange(-100, 100)

        self.createMenu()
        self.statusBar()
        self.createToolbar()

    def createToolbar(self):
        self.toolItem1 = QAction(QIcon("save.png"), "Save", self)
        self.toolItem1.setStatusTip("Save...")
        self.toolItem1.triggered.connect(lambda : self.print_action("Save"))

        self.toolItem2 = QAction(QIcon("create_new.png"), "create new", self)
        self.toolItem2.setStatusTip("Create...")
        self.toolItem2.triggered.connect(lambda: self.print_action("Create new"))

        self.toolItem3 = QAction(QIcon("home.png"), "home", self)
        self.toolItem3.setStatusTip("Home...")
        self.toolItem3.triggered.connect(lambda: self.print_action("Home"))

        self.toolItem4 = QAction(QIcon("copy.png"), "copy", self)
        self.toolItem4.setStatusTip("Copy...")
        self.toolItem4.triggered.connect(lambda: self.print_action("Copy"))

        self.toolItem5 = QAction(QIcon("font.png"), "font", self)
        self.toolItem5.setStatusTip("Change the font...")
        self.toolItem5.triggered.connect(self.select_font)

        self.toolItem6 = QAction(QIcon("colour.png"), "colour", self)
        self.toolItem6.setStatusTip("Change the colour...")
        self.toolItem6.triggered.connect(self.select_bg_colour)

        self.toolItem7 = QAction(QIcon("colour.png"), "colour", self)
        self.toolItem7.setStatusTip("Change the text colour...")
        self.toolItem7.triggered.connect(self.select_text_colour)

        self.toolItem8 = QAction(QIcon("colour.png"), "colour", self)
        self.toolItem8.setStatusTip("Clear colour...")
        self.toolItem8.triggered.connect(self.select_default_colour)

        self.toolbar = self.addToolBar("Tools")

        self.toolbar.addAction(self.toolItem1)
        self.toolbar.addAction(self.toolItem2)
        self.toolbar.addAction(self.toolItem3)
        self.toolbar.addAction(self.toolItem4)
        self.toolbar.addAction(self.toolItem5)
        self.toolbar.addAction(self.toolItem6)
        self.toolbar.addAction(self.toolItem7)
        self.toolbar.addAction(self.toolItem8)

        self.toolbar.setIconSize(QSize(18,18))

    def createMenu(self):
        self.menuItem1 = QAction("&New", self)
        self.menuItem1.setShortcut("Ctrl+N")
        self.menuItem1.setStatusTip("Creating a new file....")
        self.menuItem1.triggered.connect(self.print_action)

        self.menuItem2 = QAction("&Exit", self)
        self.menuItem2.setShortcut("Ctrl+W")
        self.menuItem2.setStatusTip("Exit the application....")
        self.menuItem2.triggered.connect(self.closeEvent)

        self.menuItem3 = QAction("&Copy", self)
        self.menuItem3.setShortcut("Ctrl+C")
        self.menuItem3.setStatusTip("Copy the data....")
        self.menuItem3.triggered.connect(self.print_action)

        self.menuItem4 = QAction("&Paste", self)
        self.menuItem4.setShortcut("Ctrl+V")
        self.menuItem4.setStatusTip("Paste the data....")
        self.menuItem4.triggered.connect(self.print_action)

        self.mainMenu = self.menuBar()

        self.fileMenu1 = self.mainMenu.addMenu("&File")
        self.fileMenu1.addAction(self.menuItem1)
        self.fileMenu1.addAction(self.menuItem2)

        self.fileMenu2 = self.mainMenu.addMenu("&Edit")
        self.fileMenu2.addAction(self.menuItem3)
        self.fileMenu2.addAction(self.menuItem4)

    def on_button_click(self):
        self.count+=1
        self.label.setText(f"Clicked {self.count}")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(0,30,1000,1000)
        else:
            self.setGeometry(0,30,500,500)

    def start_transfer(self):
        self.value = 0
        while self.value<100:
            self.value+=0.0001
            self.progressbar.setValue(self.value)

    def name_the_game(self, text):
        self.label2.setText(text)
        self.label2.adjustSize()

    def select_font(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.label2.setFont(font)
            self.label2.adjustSize()

    def select_bg_colour(self):
        self.bgcolor = QColorDialog.getColor()
        self.set_colours()

    def select_text_colour(self):
        self.color = QColorDialog.getColor()
        self.set_colours()

    def set_colours(self):
        self.label2.setStyleSheet("QWidget{color:%s;background-color:%s;}" % (self.color.name(), self.bgcolor.name()))

    def select_default_colour(self):
        self.label2.setStyleSheet('QWidget{color:black; background-color:transparent;}')

    def closeEvent(self, event):
        confirm = QMessageBox.question(self, "Confirmation",
                                       "Are you sure you want to exit?", QMessageBox.No | QMessageBox.Yes,
                                       QMessageBox.No)

        if confirm == QMessageBox.Yes:
            if event:
                event.accept()
            sys.exit()
        else:
            if event:
                event.ignore()
            print("No")

    def print_action(self, value):
        print(value)

    def show_name(self):
        textvalue= self.LineEdit.text()
        QMessageBox.information(self, "Name", f"Your name: {textvalue}", QMessageBox.Ok)
        self.LineEdit.setText("")

    def slider_value(self, value):
        self.label.setText(f"Slider: {value}")

    def radio_clicked(self, radio):
        self.label.setText(radio.text())

    def check_clicked(self, check):
        if check.text() == "check1" and check.isChecked():
            self.checklist[0] = check.text()
        elif check.text() == "check1" and not check.isChecked():
            self.checklist[0] = ""

        if check.text() == "check2" and check.isChecked():
            self.checklist[1] = check.text()
        elif check.text() == "check2" and not check.isChecked():
            self.checklist[1] = ""

        self.label.setText(" ".join(self.checklist))

    def spinbox_value(self):
        self.label.setText(str(self.spinbox.value()))


app = QApplication(sys.argv)
gui = MyWindow()
gui.show()
sys.exit(app.exec_())
