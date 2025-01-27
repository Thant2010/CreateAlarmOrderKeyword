from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox, QHBoxLayout, QLineEdit, QGroupBox

from globals import alarmCategorys
from utilityClasses.SignalManager import signalManager

class AlarmKeywordGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        signalManager.onEntryIsSaved.connect(self.__setDefault)
        signalManager.onSelectKeyword.connect(self.__setKeywordData)
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
        self.__comboCategory.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__comboCategory.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

    def getKeywordValue(self) -> str:
        """return category, keywordvalue as string"""
        if self.__comboCategory.currentIndex() != 0:
            return self.__comboCategory.currentText(), self.__keywordText.text()


    def __setKeywordData(self, category: str, keyword: str):
        index = self.__comboCategory.findText(category)
        if index != -1:
            self.__comboCategory.setCurrentIndex(index)
            self.__keywordText.setText(keyword)

    def __setDefault(self, isSaved):
        if isSaved:
            self.__comboCategory.setCurrentIndex(0)
            self.__keywordText.setText("")
