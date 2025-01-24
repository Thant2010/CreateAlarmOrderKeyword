from PySide6.QtWidgets import QHBoxLayout
from abc import abstractmethod

class BaseHBoxRow(QHBoxLayout):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getRowData(self):
        pass

    @abstractmethod
    def setDefault(self):
        pass

    @abstractmethod
    def setRowData(self, key, value):
        pass