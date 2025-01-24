from PySide6.QtWidgets import QVBoxLayout

from UtilityClasses.DataManager import DataManager
from elementsGui.elementRows.instructionRow import InstructionRow
from elementsGui.groupBoxes.baseGroupBox import BaseGroupBox


class InstructionGroupBox(BaseGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle("Anweisungen")
        self.setMinimumHeight(300)

        __layout = QVBoxLayout()

        self.__instructionRows = []

        for i in range(7):
            self.__instructionRows.append(InstructionRow())

        for row in self.__instructionRows:
            __layout.addItem(row)

        self.setLayout(__layout)

    def getInstructionValues(self):
        values = []

        for row in self.__instructionRows:
            values.append(row.getRowData())

        return tuple(values)

    def setKeywordData(self, category: str, keyword: str):
        instructionData = DataManager.getKeywordData(category, keyword, "instructions")
        for i in range(len(instructionData)):
            if instructionData[i] is not None:
                self.__instructionRows[i].setRowData(instructionData[i][0],
                                                     instructionData[i][1])


    def setDefault(self):
        for row in self.__instructionRows:
            row.setDefault()