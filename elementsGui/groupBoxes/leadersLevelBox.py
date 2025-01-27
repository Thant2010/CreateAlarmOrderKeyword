from PyQt6.QtWidgets import QVBoxLayout, QGroupBox

from utilityClasses.SignalManager import signalManager
from elementsGui.elementRows.leaderRow import LeaderRow
from utilityClasses.DataManager import DataManager


class LeadersLevelGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        signalManager.onSelectKeyword.connect(self.__setKeywordData)
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


    def __setKeywordData(self, category: str, keyword: str):
        keywordData = DataManager.getKeywordData(category, keyword, "leader")
        for key in keywordData.keys():
            for row in self.__rows:
                row.setRowData(key, keywordData[key])
