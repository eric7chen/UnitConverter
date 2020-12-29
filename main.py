import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        with open('conversions.json', 'r') as c:
            self.conversions = json.load(c)
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Unit Converter")

        self.setMinimumHeight(100)
        self.setMinimumWidth(500)

        self.layout = QGridLayout()

        self.bar = self.menuBar()

        self.createActions()
        # File Menu
        self.fileMenu = self.bar.addMenu('File')
        self.fileMenu.addAction('New')
        self.fileMenu.addAction(self.closeAction)

        #Edit Menu
        self.editMenu = self.bar.addMenu('Edit')
        self.editMenu.addAction(self.unitAction)
        #View Menu
        self.viewMenu = self.bar.addMenu('View')

        #Help Menu
        self.viewMenu = self.bar.addMenu('Help')

        #Choosing Units
        self.unitType = QComboBox(self)
        self.unitType.addItems(self.conversions.keys())

        self.length_list = list(self.conversions.keys())

        self.comboBoxOne = QComboBox(self)
        # self.comboBoxOne.addItems(self.length_list)
        self.comboBoxTwo = QComboBox(self)
        # self.comboBoxTwo.addItems(self.length_list)

        self.set_units()

        #Text Input/Output
        self.textBoxOne = QLineEdit(self)
        self.textBoxOne.setText('0.0')
        self.textBoxTwo = QLineEdit(self)
        self.textBoxTwo.setReadOnly(True)

        #Convert Button
        self.convertButton = QPushButton(text = 'Convert!')
        self.convertButton.clicked.connect(lambda *args: self.convert())

        #Functionality
        self.textBoxOne.textChanged[str].connect(lambda *args: self.convert())
        self.comboBoxOne.currentTextChanged.connect(lambda *args: self.convert())
        self.comboBoxTwo.currentTextChanged.connect(lambda *args: self.convert())
        self.unitType.currentTextChanged.connect(lambda *args: self.set_units())

        self.layout.addWidget(self.unitType, 0, 0, 1, 2)
        self.layout.addWidget(self.textBoxTwo, 1, 1)
        self.layout.addWidget(self.textBoxOne, 1, 0)
        self.layout.addWidget(self.comboBoxOne, 2, 0)
        self.layout.addWidget(self.comboBoxTwo, 2, 1)
        self.layout.addWidget(self.convertButton, 3, 0, 1, 2)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def createActions(self):
        # FILE MENU

        #Change unit type
        self.unitAction = QAction('Unit')
        self.unitAction.triggered.connect(lambda *args: self.conversion_menu())

        #Close Action
        self.closeAction = QAction('Close')
        self.closeAction.triggered.connect(self.close)

        # EDIT MENU

        #Add conversion
        self.addConversion = QAction('Add')

    def set_units(self):
        self.comboBoxOne.clear()
        self.comboBoxTwo.clear()
        self.comboBoxOne.addItems(self.conversions[self.unitType.currentText()])
        self.comboBoxTwo.addItems(self.conversions[self.unitType.currentText()])

    def convert(self):
        try:
            newVal = float(self.textBoxOne.text()) * self.conversions[self.unitType.currentText()][self.comboBoxOne.currentText()] / self.conversions[self.unitType.currentText()][self.comboBoxTwo.currentText()]
            self.textBoxTwo.setText(str(newVal))
        except ValueError:
            self.textBoxTwo.setText('Value Error!')
        except KeyError:
            self.textBoxTwo.setText('Key Error!')
    
    # def chooseUnit(self):

    # def editConversions(self):

    def conversion_menu(self):
        self.set = QDialog(self)
        self.set.resize(500, 500)
        self.set.setWindowTitle('Unit Conversions')

        self.menuLayout = QHBoxLayout()

        self.unit_type_list = QListWidget()
        self.unit_type_list.addItems(self.conversions.keys())

        self.available_units = QListWidget()

        self.menuLayout.addWidget(self.unit_type_list)
        self.menuLayout.addWidget(self.available_units)

        self.menuLayout.addStretch()

        self.conversionFactor = QLineEdit()
        self.conversionFactor.setReadOnly(True)
        self.menuLayout.addWidget(self.conversionFactor)

        self.unit_type_list.itemSelectionChanged.connect(lambda *args: self.updateAvailableUnits())
        self.available_units.itemSelectionChanged.connect(lambda *args: self.conversionFactor.setText(str(self.conversions[self.unit_type_list.currentItem().text()][self.available_units.currentItem().text()])))

        self.set.setLayout(self.menuLayout)
        self.set.exec_()
    
    def updateAvailableUnits(self):
        self.available_units.clear()
        self.available_units.addItems(self.conversions[self.unit_type_list.currentItem().text()].keys())
        self.conversionFactor.clear()

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()