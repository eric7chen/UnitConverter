import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from convert import Convert
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Unit Converter")

        self.setMinimumHeight(100)
        self.setMinimumWidth(500)

        self.layout = QGridLayout()

        self.bar = self.menuBar()
        self.fileMenu = self.bar.addMenu('File')
        self.editMenu = self.bar.addMenu('Edit')

        self.length_list = ['Kilometers', 'Meters', 'Centimeters', 'Millimeters', 'Micrometers', 'Nanometers']

        self.comboBoxOne = QComboBox(self)
        self.comboBoxOne.addItems(self.length_list)
        self.comboBoxTwo = QComboBox(self)
        self.comboBoxTwo.addItems(self.length_list)

        self.textBoxOne = QLineEdit(self)
        self.textBoxOne.setText('0.0')
        self.textBoxTwo = QLineEdit(self)
        self.textBoxTwo.setReadOnly(True)

        self.convertButton = QPushButton(text = 'Convert!')
        self.convertButton.clicked.connect(lambda *args: self.convert())

        self.textBoxOne.textChanged[str].connect(lambda *args: self.convert())

        self.layout.addWidget(self.textBoxTwo, 0, 1)
        self.layout.addWidget(self.textBoxOne, 0, 0)
        self.layout.addWidget(self.comboBoxOne, 1, 0)
        self.layout.addWidget(self.comboBoxTwo, 1, 1)
        self.layout.addWidget(self.convertButton, 2, 0, 1, 2)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def convert(self):
        try:
            newVal = float(self.textBoxOne.text()) * Convert.factor_dictionary[self.comboBoxOne.currentText()] / Convert.factor_dictionary[self.comboBoxTwo.currentText()]
            self.textBoxTwo.setText(str(newVal))
        except ValueError:
            self.textBoxTwo.setText('Value Error!')

def main():
    app = QApplication(sys.argv)
    app.setStyle('windowsvista')
    window = MainWindow()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()