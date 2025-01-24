from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTreeView
from UtilityClasses.DataManager import DataManager
from UtilityClasses.SignalManager import signalManager


class TreeViewWindow(QWidget):

    __maxLevel = 1

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Element wählen")
        self.setWindowIcon(QIcon("icons/windowIcon.ico"))
        self.setMinimumSize(300, 300)
        self.setWindowModality(Qt.ApplicationModal)

        __layout = QVBoxLayout()
        self.setLayout(__layout)

        self.__treeViewWidget = QTreeView()
        self.__treeViewWidget.doubleClicked.connect(self.on_item_double_clicked)

        self.__itemModel = QStandardItemModel()
        self.__itemModel.setHorizontalHeaderLabels(["Kategorien"])

        self.__addItemsToTreeView(self.__itemModel.invisibleRootItem(), 0, TreeViewWindow.__maxLevel)

        self.__treeViewWidget.setModel(self.__itemModel)

        __layout.addWidget(self.__treeViewWidget)


    def __addItemsToTreeView(self, parent, level: int, max_level: int, aaoData=None):
        if level > max_level:
            return

        if aaoData is None:
            aaoData = DataManager.getFullData()

        for key, value in aaoData.items():
            item = QStandardItem(str(key))
            item.setEditable(False)
            parent.appendRow(item)
            if isinstance(value, dict) and level < max_level:
                self.__addItemsToTreeView(item, level + 1, max_level, value)

    def on_item_double_clicked(self, index: QModelIndex):
        if TreeViewWindow.__isNotRootNode(index):
            itemHierachy = []
            while index.isValid():
                item = self.__itemModel.itemFromIndex(index)
                itemHierachy.append(item.text())
                index = index.parent()
            itemHierachy.reverse()

            signalManager.onSelectKeyword.emit(itemHierachy)

            self.close()

    @staticmethod
    def __isNotRootNode(index: QModelIndex) -> bool:
        parent = index.parent()
        return index.isValid() and parent.isValid()