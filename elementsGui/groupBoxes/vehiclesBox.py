from PyQt5.QtWidgets import QVBoxLayout

from UtilityClasses.DataManager import DataManager
from elementsGui.groupBoxes.baseGroupBox import BaseGroupBox
from globals import vehicles
from elementsGui.elementRows.vehicleRow import VehicleRow

class VehicleGroupBox(BaseGroupBox):

    def __init__(self):
        super().__init__()
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

    def setKeywordData(self, category: str, keyword: str):
        vehilceData = DataManager.getKeywordData(category, keyword, "vehicle")
        for key in vehilceData.keys():
            for row in self.__vehicleRows:
                row.setRowData(key, vehilceData[key])

    def setDefault(self):
        for row in self.__vehicleRows:
            row.setDefault()
