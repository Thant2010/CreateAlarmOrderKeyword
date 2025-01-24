from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton
from UtilityClasses.shadowEffect import ShadowEffect
from globals import iconButtons

class FlatIconButton(QPushButton):

    def __init__(self, key):
        super().__init__()
        self.setFixedSize(128, 128)
        self.setIconSize(QSize(100, 100))
        self.setGraphicsEffect(ShadowEffect().shadow)
        self.setIcon(QIcon(iconButtons[key][0]))
        self.setToolTip(iconButtons[key][1])
        self.setFlat(True)
        self.setProperty("iconButton", True)