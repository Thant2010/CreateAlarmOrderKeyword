from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QCheckBox
from UtilityClasses.LayoutSpacer import LayoutSpacer
from elementsGui.elementRows.BaseHBoxRow import BaseHBoxRow


class StaffRow(BaseHBoxRow):

    def __init__(self, staff):
        super().__init__()
        self.__staffLabel = QLabel(staff)
        self.__staffLabel.setMinimumWidth(170)
        self.__staffLabel.setProperty("weight", "bold")
        self.__staffLabel.setProperty("fontsize", "medium")
        self.__staffLabel.setAlignment(Qt.AlignCenter)
        self.__checkStaff = QCheckBox()

        self.addWidget(self.__staffLabel)
        self.addWidget(self.__checkStaff)


    def setRowData(self, staffText: str, value: bool):
        if staffText == self.__staffLabel.text():
            self.__checkStaff.setChecked(value)

    def setDefault(self):
        self.__checkStaff.setChecked(False)

    def getRowData(self):
        return self.__staffLabel.text(), self.__checkStaff.isChecked()
