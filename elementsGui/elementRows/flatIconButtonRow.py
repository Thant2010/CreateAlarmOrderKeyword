from PyQt6.QtWidgets import QVBoxLayout
from globals import iconButtons
from elementsGui.buttons.flatIconButton import FlatIconButton
from utilityClasses.LayoutSpacer import LayoutSpacer

class FlatIconButtonRow(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.__buttons = []
        for key in iconButtons.keys():
            self.__buttons.append(FlatIconButton(key))
        for button in self.__buttons:
            self.addWidget(button)

        self.insertItem(self.count() - 1, LayoutSpacer.verticalExpandingSpacer())

    def setFunctionToButton(self, index, funtion):
        self.__buttons[index].clicked.connect(funtion)
