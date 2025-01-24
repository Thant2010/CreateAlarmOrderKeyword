from PyQt5.QtWidgets import QLineEdit, QButtonGroup, QRadioButton

from UtilityClasses.DataManager import DataManager
from elementsGui.elementRows.BaseHBoxRow import BaseHBoxRow


class InstructionRow(BaseHBoxRow):

    def __init__(self):
        super().__init__()
        self.__instructionLineEdit = QLineEdit()
        self.__instructionLineEdit.setMinimumHeight(40)
        self.__instructionLineEdit.setProperty("fontsize", "medium")
        self.__instructionRadioGroup = QButtonGroup()
        self.__radioMustButton = QRadioButton("Pflicht")
        self.__radioCanButton = QRadioButton("Kann")
        self.__radioCanButton.setChecked(True)
        self.__instructionRadioGroup.addButton(self.__radioMustButton)
        self.__instructionRadioGroup.addButton(self.__radioCanButton)
        self.addWidget(self.__instructionLineEdit)
        self.addWidget(self.__radioMustButton)
        self.addWidget(self.__radioCanButton)

    def getRowData(self):
        if self.__instructionLineEdit.text() != "":
            return self.__instructionLineEdit.text(), self.__instructionRadioGroup.checkedButton().text()
        else:
            return None

    def setDefault(self):
        self.__radioCanButton.setChecked(True)
        self.__instructionLineEdit.setText("")

    def setRowData(self, text, radioText):

        self.__instructionLineEdit.setText(text)
        for button in self.__instructionRadioGroup.buttons():
            if button.text() == radioText:
                button.setChecked(True)
                break