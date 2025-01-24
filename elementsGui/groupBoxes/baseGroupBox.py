from PyQt5.QtWidgets import QGroupBox
from abc import abstractmethod

class BaseGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def setKeywordData(self, category: str, keyword: str):
        pass

    @abstractmethod
    def setDefault(self):
        pass
