from PySide6.QtWidgets import QVBoxLayout, QTextEdit

from UtilityClasses.DataManager import DataManager
from elementsGui.groupBoxes.baseGroupBox import BaseGroupBox


class AlarmScenarioBox(BaseGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle("Szenarios")
        __layout = QVBoxLayout()
        self.__alarmScenarioTextEdit = QTextEdit()
        self.__alarmScenarioTextEdit.setProperty("fontsize", "medium")
        __layout.addWidget(self.__alarmScenarioTextEdit)
        self.setLayout(__layout)

    def setKeywordData(self, category: str, keyword: str):
        scenarioData = DataManager.getKeywordData(category, keyword, "scenarios")
        value = str()
        for scenrario in scenarioData:
            value += f'{scenrario}\n'
        self.__alarmScenarioTextEdit.setText(value)



    def setDefault(self):
        self.__alarmScenarioTextEdit.setText("")

    def getAlarmScenariosData(self):
        value = self.__alarmScenarioTextEdit.toPlainText()
        data = value.splitlines()
        return tuple(data)