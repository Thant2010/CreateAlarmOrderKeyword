from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QButtonGroup, QRadioButton

from elementsGui.elementRows.BaseHBoxRow import BaseHBoxRow
from utilityClasses.SignalManager import signalManager

class LeaderRow(BaseHBoxRow):

    def __init__(self, leader):
        signalManager.onEntryIsSaved.connect(self.__setDefault)
        super().__init__()
        self.__leaderLabel = QLabel(leader)
        self.__leaderLabel.setProperty("weight", "bold")
        self.__leaderLabel.setProperty("fontsize", "medium")
        self.__leaderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__radioButtonGroup = QButtonGroup()
        self.__radioButtonAlarm = QRadioButton("Alarm")
        self.__radioButtonInfo = QRadioButton("Info")
        self.__radioButtonDefault = QRadioButton("Nichts")
        self.__radioButtonDefault.setChecked(True)
        self.__radioButtonGroup.addButton(self.__radioButtonAlarm)
        self.__radioButtonGroup.addButton(self.__radioButtonInfo)
        self.__radioButtonGroup.addButton(self.__radioButtonDefault)
        self.addWidget(self.__leaderLabel)
        self.addWidget(self.__radioButtonAlarm)
        self.addWidget(self.__radioButtonInfo)
        self.addWidget(self.__radioButtonDefault)

    def getRowData(self):
        return self.__leaderLabel.text(), self.__radioButtonGroup.checkedButton().text()

    def __setDefault(self, isSaved):
        if isSaved:
            self.__radioButtonDefault.setChecked(True)

    def setRowData(self, leader, value):
        if self.__leaderLabel.text() == leader:
            for button in self.__radioButtonGroup.buttons():
                if button.text() == value:
                    button.setChecked(True)
                    break
