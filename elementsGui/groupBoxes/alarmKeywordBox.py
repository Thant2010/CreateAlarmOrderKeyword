from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLineEdit

from globals import alarmCategorys
from elementsGui.groupBoxes.baseGroupBox import BaseGroupBox


class AlarmKeywordGroupBox(BaseGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle("Alarmstichwort")
        self.setMinimumSize(450, 70)
        self.__comboCategory = QComboBox()
        self.__setupComboBox()
        self.__keywordText = QLineEdit()
        self.__keywordText.setMinimumHeight(40)
        self.__keywordText.setProperty("fontsize", "medium")
        __layout = QHBoxLayout()
        __layout.addWidget(self.__comboCategory)
        __layout.addWidget(self.__keywordText)
        self.setLayout(__layout)

    def __setupComboBox(self):
        self.__comboCategory.setMinimumHeight(40)
        self.__comboCategory.addItem("---")
        for category in alarmCategorys:
            self.__comboCategory.addItem(category)
        self.__comboCategory.setMaxVisibleItems(len(alarmCategorys) + 1)
        self.__comboCategory.setEditable(True)
        self.__comboCategory.lineEdit().setReadOnly(True)
        self.__comboCategory.lineEdit().setAlignment(Qt.AlignCenter)
        self.__comboCategory.setSizeAdjustPolicy(QComboBox.AdjustToContents)

    def getKeywordValue(self) -> str:
        """return category, keywordvalue as string"""
        if self.__comboCategory.currentIndex() != 0:
            return self.__comboCategory.currentText(), self.__keywordText.text()


    def setKeywordData(self, category: str, keyword: str):
        index = self.__comboCategory.findText(category)
        if index != -1:
            self.__comboCategory.setCurrentIndex(index)
            self.__keywordText.setText(keyword)

    def setDefault(self):
        self.__comboCategory.setCurrentIndex(0)
        self.__keywordText.setText("")
