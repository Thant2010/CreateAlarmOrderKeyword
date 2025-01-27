from PyQt6.QtWidgets import QVBoxLayout, QGroupBox

from utilityClasses.DataManager import DataManager
from utilityClasses.SignalManager import signalManager
from elementsGui.elementRows.instructionRow import InstructionRow



class InstructionGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        signalManager.onSelectKeyword.connect(self.__setKeywordData)
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

    def __setKeywordData(self, category: str, keyword: str):
        instructionData = DataManager.getKeywordData(category, keyword, "instructions")
        for i in range(len(instructionData)):
            if instructionData[i] is not None:
                self.__instructionRows[i].setRowData(instructionData[i][0],
                                                     instructionData[i][1])

