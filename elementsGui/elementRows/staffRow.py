from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QCheckBox
from elementsGui.elementRows.BaseHBoxRow import BaseHBoxRow
from utilityClasses.SignalManager import signalManager

class StaffRow(BaseHBoxRow):

    def __init__(self, staff):
        super().__init__()
        signalManager.onEntryIsSaved.connect(self.__setDefault)
        self.__staffLabel = QLabel(staff)
        self.__staffLabel.setMinimumWidth(170)
        self.__staffLabel.setProperty("weight", "bold")
        self.__staffLabel.setProperty("fontsize", "medium")
        self.__staffLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__checkStaff = QCheckBox()

        self.addWidget(self.__staffLabel)
        self.addWidget(self.__checkStaff)


    def setRowData(self, staffText: str, value: bool):
        if staffText == self.__staffLabel.text():
            self.__checkStaff.setChecked(value)

    def __setDefault(self, isSaved):
        if isSaved:
            self.__checkStaff.setChecked(False)

    def getRowData(self):
        return self.__staffLabel.text(), self.__checkStaff.isChecked()
