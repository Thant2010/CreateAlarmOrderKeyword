from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class ShadowEffect:
    """
    Returns a DropShadowEffect
    """
    def __init__(self):
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(25)
        self.shadow.setOffset(5, 3)
        self.shadow.setColor(Qt.black)
