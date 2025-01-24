from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox

from UtilityClasses.shadowEffect import ShadowEffect


def MyMessageBox(windowTitle, message):
    msg = QMessageBox()
    msg.setWindowTitle(windowTitle)
    msg.setWindowIcon(QIcon("icons/windowIcon.ico"))
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setGraphicsEffect(ShadowEffect().shadow)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setGeometry(650, 450, 300, 300)

    returnvalue = msg.exec()
    if returnvalue == QMessageBox.Ok:
        pass
