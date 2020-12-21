import os
import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QStyleFactory, QWidget, QLabel, QComboBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Unit Converter")

        self.setFixedHeight(500)
        self.setFixedWidth(1000)

        widget = QWidget()
        layout = QGridLayout()
        widget.setLayout(layout)

        #comboBox = QComboBox(self)
        #layout.addWidget(comboBox, 0, 0)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
app.setStyle('windowsvista')

window = MainWindow()
window.show()

app.exec_()