from PyQt5.QtWidgets import QVBoxLayout
from elementsGui.elementRows.leaderRow import LeaderRow
from elementsGui.groupBoxes.baseGroupBox import BaseGroupBox
from UtilityClasses.DataManager import DataManager


class LeadersLevelGroupBox(BaseGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle("Führungsstufe")
        self.setMinimumWidth(450)
        __layout = QVBoxLayout()

        __leaderARow = LeaderRow("A-Dienst")
        __leaderBRow = LeaderRow("B-Dienst")
        __leaderCRow = LeaderRow("C-Dienst")

        __layout.addItem(__leaderARow)
        __layout.addItem(__leaderBRow)
        __layout.addItem(__leaderCRow)

        self.__rows = [__leaderARow,
                       __leaderBRow,
                       __leaderCRow]

        self.setLayout(__layout)

    def getLeadersLevels(self) -> dict:
        leaderData = dict()

        for row in self.__rows:
            rowDatas = row.getRowData()
            leaderData[rowDatas[0]] = rowDatas[1]

        return leaderData

    def setDefault(self):
        for row in self.__rows:
            row.setDefault()

    def setKeywordData(self, category: str, keyword: str):
        keywordData = DataManager.getKeywordData(category, keyword, "leader")
        for key in keywordData.keys():
            for row in self.__rows:
                row.setRowData(key, keywordData[key])
