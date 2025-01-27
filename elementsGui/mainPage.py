from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout

from utilityClasses.ShadowEffect import ShadowEffect
from utilityClasses.SignalManager import signalManager
from utilityClasses.DataManager import DataManager
from utilityFunctions.myMessageBox import MyMessageBox
from elementsGui.groupBoxes.alarmKeywordBox import AlarmKeywordGroupBox
from elementsGui.groupBoxes.alarmScenariosBox import AlarmScenarioBox
from elementsGui.groupBoxes.leadersLevelBox import LeadersLevelGroupBox
from elementsGui.groupBoxes.vehiclesBox import VehicleGroupBox
from elementsGui.groupBoxes.staffBox import StaffGroupBox
from elementsGui.groupBoxes.instructionBox import InstructionGroupBox
from elementsGui.elementRows.flatIconButtonRow import FlatIconButtonRow
from elementsGui.treeViewWindow import TreeViewWindow


class MainPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(1300, 800)
        self.setWindowIcon(QIcon("icons/windowIcon.ico"))
        self.setWindowTitle("Ford Werkfeuerwehr - AAO Bearbeitung")

        __titleLabel = QLabel("AAO Einträge bearbeiten")
        __titleLabel.setObjectName("mainTitle")
        __titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        __titleLabel.setGraphicsEffect(ShadowEffect().shadow)

        self.__alarmKeywordGroupBox = AlarmKeywordGroupBox()
        self.__leaderLevelGroupBox = LeadersLevelGroupBox()
        self.__vehicleGroupBox = VehicleGroupBox()
        self.__staffGroupBox = StaffGroupBox()
        self.__instructionGroupBox = InstructionGroupBox()
        self.__alarmScenarioBox = AlarmScenarioBox()

        self.__flatIconButtonRow = FlatIconButtonRow()
        self.__flatIconButtonRow.setFunctionToButton(0, self.__saveDataInFile)
        self.__flatIconButtonRow.setFunctionToButton(1, self.__openTreeView)
        self.__flatIconButtonRow.setFunctionToButton(2, lambda: signalManager.onEntryIsSaved.emit(True))
        self.__flatIconButtonRow.setFunctionToButton(-1, self.close)

        __gridLayout = QGridLayout()
        self.setLayout(__gridLayout)

        __gridLayout.addWidget(__titleLabel, 0, 0, 1, 6)
        __gridLayout.addWidget(self.__alarmKeywordGroupBox, 1, 0, 1, 2)
        __gridLayout.addWidget(self.__leaderLevelGroupBox, 2, 0, 2, 2)
        __gridLayout.addWidget(self.__staffGroupBox, 1, 2, 3, 1)
        __gridLayout.addWidget(self.__vehicleGroupBox, 1, 3, 3, 1)
        __gridLayout.addWidget(self.__alarmScenarioBox, 1, 4, 3, 1)
        __gridLayout.addWidget(self.__instructionGroupBox, 5, 0, 1, 5)
        __gridLayout.addLayout(self.__flatIconButtonRow, 1, 5, 7, 1)

        self.show()

    def __saveDataInFile(self):

        try:
            category, keyword = self.__alarmKeywordGroupBox.getKeywordValue()
        except TypeError:
            return

        if keyword != "":

            keywordDataSet = self.__getEntryValues()

            DataManager.saveData(category, keyword, keywordDataSet)
            MyMessageBox("Erfolgreich", "Datensatz erfolgreich gespeichert")
            signalManager.onEntryIsSaved.emit(True)

    def __getEntryValues(self) -> dict:

        leaderData = self.__leaderLevelGroupBox.getLeadersLevels()
        vehicleData = self.__vehicleGroupBox.getVehiclesValues()
        staffData = self.__staffGroupBox.getStaffValues()
        instructionData = self.__instructionGroupBox.getInstructionValues()
        scenarioData = self.__alarmScenarioBox.getAlarmScenariosData()

        keywordDataSet = {"leader": leaderData,
                          "vehicle": vehicleData,
                          "staff": staffData,
                          "instructions": instructionData,
                          "scenarios": scenarioData}

        return keywordDataSet

    def __openTreeView(self):
        self.__treeWindow = TreeViewWindow()
        self.__treeWindow.show()
