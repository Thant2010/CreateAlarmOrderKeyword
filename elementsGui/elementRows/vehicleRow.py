from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QCheckBox
from UtilityClasses.LayoutSpacer import LayoutSpacer
from elementsGui.elementRows.BaseHBoxRow import BaseHBoxRow


class VehicleRow(BaseHBoxRow):

    def __init__(self, vehicle):
        super().__init__()
        self.__vehicleLabel = QLabel(vehicle)
        self.__vehicleLabel.setMinimumSize(65, 30)
        self.__vehicleLabel.setProperty("weight", "bold")
        self.__vehicleLabel.setProperty("fontsize", "medium")
        self.__vehicleLabel.setAlignment(Qt.AlignCenter)
        self.__checkVehicle = QCheckBox()
        self.addWidget(self.__vehicleLabel)
        self.addItem(LayoutSpacer.horizontalFixedSpacer(40))
        self.addWidget(self.__checkVehicle)

    def getRowData(self):
        return self.__vehicleLabel.text(), self.__checkVehicle.isChecked()

    def setDefault(self):
        self.__checkVehicle.setChecked(False)

    def setRowData(self, vehicle: str, value: bool):
        if self.__vehicleLabel.text() == vehicle:
            self.__checkVehicle.setChecked(value)