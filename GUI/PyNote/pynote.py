import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPlainTextEdit, QAction, \
    QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtPrintSupport import QPrintDialog


class MyNotepad(QMainWindow):
    def __init__(self):
        super(MyNotepad, self).__init__()
        self.initUI()

    def initUI(self):
        self.path = None
        self.filterFileTypes = "Text Document (*.txt);; Python (*.py)"

        self.update_title()
        self.setGeometry(10, 55, 500, 500)

        self.widget = QWidget()
        self.vboxlayout = QVBoxLayout()

        self.editor = QPlainTextEdit()

        self.vboxlayout.addWidget(self.editor)

        self.widget.setLayout(self.vboxlayout)
        self.setCentralWidget(self.widget)

        self.createMenu()
        self.createToolbar()
        self.statusBar()

    def createMenu(self):
        self.menuItem1 = QAction("&New", self)
        self.menuItem1.setShortcut("Ctrl+N")
        self.menuItem1.setStatusTip("Creating a new file....")
        self.menuItem1.triggered.connect(self.file_new)

        self.menuItem2 = QAction("&Open", self)
        self.menuItem2.setShortcut("Ctrl+O")
        self.menuItem2.setStatusTip("Open a file....")
        self.menuItem2.triggered.connect(self.file_open)

        self.menuItem3 = QAction("&Save", self)
        self.menuItem3.setShortcut("Ctrl+S")
        self.menuItem3.setStatusTip("Saving file....")
        self.menuItem3.triggered.connect(self.file_save)

        self.menuItem4 = QAction("&Save As", self)
        self.menuItem4.setShortcut("Ctrl+Shift+S")
        self.menuItem4.setStatusTip("Saving file as....")
        self.menuItem4.triggered.connect(self.file_save_as)

        self.menuItem5 = QAction("&Print", self)
        self.menuItem5.setShortcut("Ctrl+P")
        self.menuItem5.setStatusTip("Printing file....")
        self.menuItem5.triggered.connect(self.file_print)

        self.menuItem6 = QAction("&Exit", self)
        self.menuItem6.setShortcut("Ctrl+Q")
        self.menuItem6.setStatusTip("Exiting....")
        self.menuItem6.triggered.connect(self.closeEvent)

        self.menuItem7 = QAction("&Undo", self)
        self.menuItem7.setShortcut("Ctrl+Z")
        self.menuItem7.setStatusTip("Undo....")
        self.menuItem7.triggered.connect(self.editor.undo)

        self.menuItem8 = QAction("&Redo", self)
        self.menuItem8.setShortcut("Ctrl+Y")
        self.menuItem8.setStatusTip("Redo....")
        self.menuItem8.triggered.connect(self.editor.redo)

        self.menuItem9 = QAction("&Cut", self)
        self.menuItem9.setShortcut("Ctrl+X")
        self.menuItem9.setStatusTip("Cut....")
        self.menuItem9.triggered.connect(self.editor.cut)

        self.menuItem10 = QAction("&Copy", self)
        self.menuItem10.setShortcut("Ctrl+C")
        self.menuItem10.setStatusTip("Copy....")
        self.menuItem10.triggered.connect(self.editor.copy)

        self.menuItem11 = QAction("&Paste", self)
        self.menuItem11.setShortcut("Ctrl+V")
        self.menuItem11.setStatusTip("Paste....")
        self.menuItem11.triggered.connect(self.editor.paste)

        self.menuItem12 = QAction("&Select All", self)
        self.menuItem12.setShortcut("Ctrl+A")
        self.menuItem12.setStatusTip("Select All....")
        self.menuItem12.triggered.connect(self.editor.selectAll)

        self.menuItem13 = QAction("&Clear", self)
        self.menuItem13.setShortcut("Ctrl+L")
        self.menuItem13.setStatusTip("Clear....")
        self.menuItem13.triggered.connect(self.clear_text)

        self.mainMenu = self.menuBar()

        self.fileMenu1 = self.mainMenu.addMenu("&File")
        self.fileMenu1.addAction(self.menuItem1)
        self.fileMenu1.addAction(self.menuItem2)
        self.fileMenu1.addSeparator()
        self.fileMenu1.addAction(self.menuItem3)
        self.fileMenu1.addAction(self.menuItem4)
        self.fileMenu1.addSeparator()
        self.fileMenu1.addAction(self.menuItem5)
        self.fileMenu1.addSeparator()
        self.fileMenu1.addAction(self.menuItem6)

        self.fileMenu2 = self.mainMenu.addMenu("&Edit")
        self.fileMenu2.addAction(self.menuItem7)
        self.fileMenu2.addAction(self.menuItem8)
        self.fileMenu2.addSeparator()
        self.fileMenu2.addAction(self.menuItem9)
        self.fileMenu2.addAction(self.menuItem10)
        self.fileMenu2.addAction(self.menuItem11)
        self.fileMenu2.addSeparator()
        self.fileMenu2.addAction(self.menuItem12)
        self.fileMenu2.addAction(self.menuItem13)

    def createToolbar(self):
        self.toolItem1 = QAction(QIcon("Icons/new.png"), "New File", self)
        self.toolItem1.setStatusTip("New file...")
        self.toolItem1.triggered.connect(self.file_new)

        self.toolItem2 = QAction(QIcon("Icons/open.png"), "Open File", self)
        self.toolItem2.setStatusTip("Open file...")
        self.toolItem2.triggered.connect(self.file_open)

        self.toolItem3 = QAction(QIcon("Icons/save.png"), "Save", self)
        self.toolItem3.setStatusTip("Save...")
        self.toolItem3.triggered.connect(self.file_save)

        self.toolItem4 = QAction(QIcon("Icons/save_as.png"), "Save As", self)
        self.toolItem4.setStatusTip("Save As...")
        self.toolItem4.triggered.connect(self.file_save_as)

        self.toolItem5 = QAction(QIcon("Icons/print.png"), "Print", self)
        self.toolItem5.setStatusTip("Print...")
        self.toolItem5.triggered.connect(self.file_print)

        self.toolItem6 = QAction(QIcon("Icons/undo.png"), "Undo", self)
        self.toolItem6.setStatusTip("Undo...")
        self.toolItem6.triggered.connect(self.editor.undo)

        self.toolItem7 = QAction(QIcon("Icons/redo.png"), "Redo", self)
        self.toolItem7.setStatusTip("Redo...")
        self.toolItem7.triggered.connect(self.editor.redo)


        self.toolItem8 = QAction(QIcon("Icons/cut.png"), "Cut", self)
        self.toolItem8.setStatusTip("Cut...")
        self.toolItem8.triggered.connect(self.editor.cut)


        self.toolItem9 = QAction(QIcon("Icons/copy.png"), "Copy", self)
        self.toolItem9.setStatusTip("Copy...")
        self.toolItem9.triggered.connect(self.editor.copy)


        self.toolItem10 = QAction(QIcon("Icons/paste.png"), "Paste", self)
        self.toolItem10.setStatusTip("Paste...")
        self.toolItem10.triggered.connect(self.editor.paste)

        self.toolItem11 = QAction(QIcon("Icons/select_all.png"), "Select All", self)
        self.toolItem11.setStatusTip("Select All...")
        self.toolItem11.triggered.connect(self.editor.selectAll)

        self.toolItem12 = QAction(QIcon("Icons/clear.png"), "Clear", self)
        self.toolItem12.setStatusTip("Clear...")
        self.toolItem12.triggered.connect(self.clear_text)

        self.toolbar1 = self.addToolBar("Tools1")
        self.toolbar2 = self.addToolBar("Tools2")

        self.toolbar1.addAction(self.toolItem1)
        self.toolbar1.addAction(self.toolItem2)
        self.toolbar1.addSeparator()
        self.toolbar1.addAction(self.toolItem3)
        self.toolbar1.addAction(self.toolItem4)
        self.toolbar1.addSeparator()
        self.toolbar1.addAction(self.toolItem5)

        self.toolbar2.addAction(self.toolItem6)
        self.toolbar2.addAction(self.toolItem7)
        self.toolbar2.addSeparator()
        self.toolbar2.addAction(self.toolItem8)
        self.toolbar2.addAction(self.toolItem9)
        self.toolbar2.addAction(self.toolItem10)
        self.toolbar2.addSeparator()
        self.toolbar2.addAction(self.toolItem11)
        self.toolbar2.addAction(self.toolItem12)

        self.toolbar1.setIconSize(QSize(26, 26))
        self.toolbar2.setIconSize(QSize(26, 26))

    def file_new(self):
        confirm = QMessageBox.No
        if self.editor.toPlainText():
            confirm = QMessageBox.question(self, "Confirmation",
                                           "Do you want to save this file?", QMessageBox.No | QMessageBox.Yes,
                                           QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            self.file_save()

        self.clear_text()
        self.path = None
        self.update_title()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", self.filterFileTypes)
        if path:
            try:
                with open(path, "r") as file:
                    text = file.read()
            except Exception as ex:
                print("Exception", ex)
            self.path = path
            self.editor.setPlainText(text)
            self.update_title()

    def file_save(self):
        if self.path is None:
            self.file_save_as()
        else:
            text = self.editor.toPlainText()
            try:
                with open(self.path, "w") as file:
                    file.write(text)
            except Exception as ex:
                print("Exception", ex)

    def file_save_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File As", "", self.filterFileTypes)
        text = self.editor.toPlainText()

        if path:
            try:
                with open(path, 'w') as file:
                    file.write(text)
            except Exception as ex:
                print("Exception", ex)
            self.path = path
            self.update_title()

    def file_print(self):
        printdialog = QPrintDialog()
        if printdialog.exec_():
            self.editor.print_(printdialog.printer())

    def update_title(self):
        self.setWindowTitle(f'{os.path.basename(self.path)} - PyNote' if self.path else 'Untitled - PyNote')

    def clear_text(self):
        if self.editor.toPlainText() != "":
            confirm = QMessageBox.question(self, "Confirmation", "Are you sure you want to clear all text in this document? "
                                                                 "Once cleared the text cannot be recovered.",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.editor.setPlainText("")

    def closeEvent(self, event):
        text = ""
        if self.path:
            try:
                with open(self.path, "r") as file:
                    text = file.read()
            except Exception as ex:
                print("Exception", ex)
        confirm = QMessageBox.No
        if self.editor.toPlainText() != text and self.editor.toPlainText() != "":
            confirm = QMessageBox.question(self, "Confirmation",
                                           "Do you want to save changes?", QMessageBox.No | QMessageBox.Yes,
                                           QMessageBox.Yes)
        if confirm == QMessageBox.Yes:
            self.file_save()
        sys.exit()


app = QApplication(sys.argv)
notepad = MyNotepad()
notepad.show()
sys.exit(app.exec_())
