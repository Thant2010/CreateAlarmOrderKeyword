from PyQt6.QtWidgets import QVBoxLayout, QTextEdit, QGroupBox

from utilityClasses.DataManager import DataManager
from utilityClasses.SignalManager import signalManager



class AlarmScenarioBox(QGroupBox):

    def __init__(self):
        super().__init__()

        signalManager.onEntryIsSaved.connect(self.__setDefault)
        signalManager.onSelectKeyword.connect(self.__setKeywordData)

        self.setTitle("Meldebild")
        __layout = QVBoxLayout()
        self.__alarmScenarioTextEdit = QTextEdit()
        self.__alarmScenarioTextEdit.setProperty("fontsize", "medium")
        __layout.addWidget(self.__alarmScenarioTextEdit)
        self.setLayout(__layout)

    def __setKeywordData(self, category: str, keyword: str):
        scenarioData = DataManager.getKeywordData(category, keyword, "scenarios")
        value = str()
        for scenrario in scenarioData:
            value += f'{scenrario}\n'
        self.__alarmScenarioTextEdit.setText(value)

    def __setDefault(self, isSaved):
        if isSaved:
            self.__alarmScenarioTextEdit.setText("")

    def getAlarmScenariosData(self):
        value = self.__alarmScenarioTextEdit.toPlainText()
        data = value.splitlines()
        return tuple(data)