from PySide6.QtWidgets import QVBoxLayout

from elementsGui.groupBoxes.baseGroupBox import BaseGroupBox
from globals import staffs
from elementsGui.elementRows.staffRow import StaffRow
from UtilityClasses.DataManager import DataManager


class StaffGroupBox(BaseGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle("Mannschaft")
        self.setMinimumHeight(300)
        __layout = QVBoxLayout()
        self.__staffRows = []
        for staff in staffs:
            self.__staffRows.append(StaffRow(staff))

        for row in self.__staffRows:
            __layout.addItem(row)

        self.setLayout(__layout)

    def getStaffValues(self):
        staffData = dict()
        for row in self.__staffRows:
            rowData = row.getRowData()
            staffData[rowData[0]] = rowData[1]

        return staffData

    def setKeywordData(self, category: str, keyword: str):
        staffData = DataManager.getKeywordData(category, keyword, "staff")

        for key in staffData.keys():
            for row in self.__staffRows:
                row.setRowData(key, staffData[key])

    def setDefault(self):
        for row in self.__staffRows:
            row.setDefault()
