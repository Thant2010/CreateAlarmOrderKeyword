from PyQt6.QtWidgets import QVBoxLayout, QGroupBox

from globals import vehicles
from elementsGui.elementRows.vehicleRow import VehicleRow
from utilityClasses.DataManager import DataManager
from utilityClasses.SignalManager import signalManager


class VehicleGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        signalManager.onSelectKeyword.connect(self.__setKeywordData)
        self.setTitle("Fahrzeuge")
        self.setMinimumWidth(150)
        __layout = QVBoxLayout()
        self.__vehicleRows = []
        for vehicle in vehicles:
            self.__vehicleRows.append(VehicleRow(vehicle))

        for row in self.__vehicleRows:
            __layout.addItem(row)
        self.setLayout(__layout)

    def getVehiclesValues(self):
        vehicleData = dict()
        for row in self.__vehicleRows:
            rowData = row.getRowData()
            vehicleData[rowData[0]] = rowData[1]

        return vehicleData

    def __setKeywordData(self, category: str, keyword: str):
        vehilceData = DataManager.getKeywordData(category, keyword, "vehicle")
        for key in vehilceData.keys():
            for row in self.__vehicleRows:
                row.setRowData(key, vehilceData[key])

