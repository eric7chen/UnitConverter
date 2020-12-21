import os
import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow, QSizePolicy, QStyleFactory, QWidget, QLabel, QComboBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Unit Converter")

        self.setFixedHeight(500)
        self.setFixedWidth(1000)

        layout = QGridLayout()

        comboBoxOne = QComboBox(self)
        comboBoxOne.size()
        list_one = ['a', 'b', 'c']
        comboBoxOne.addItems(list_one)

        comboBoxTwo = QComboBox(self)
        comboBoxTwo.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        list_two = ['d', 'e', 'f']
        comboBoxTwo.addItems(list_two)

        textBoxOne = QLineEdit(self)
        textBoxTwo = QLineEdit(self)
        textBoxTwo.setReadOnly(True)

        layout.addWidget(comboBoxOne, 0, 0)
        layout.addWidget(textBoxOne, 0, 1)
        layout.addWidget(QLabel(''), 1, 0)
        layout.addWidget(QLabel(''), 2, 0)
        layout.addWidget(comboBoxTwo, 3, 0)
        layout.addWidget(textBoxTwo, 3, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
app.setStyle('windowsvista')

window = MainWindow()
window.show()

app.exec_()