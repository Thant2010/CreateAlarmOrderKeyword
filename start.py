import locale
import sys
import traceback

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication
from utilityFunctions.writeErrorToLogFile import writeErrorToLogFile
from elementsGui.mainPage import MainPage


def exceptionHandler(exc_type, exc_value, exc_tb):
    tb = "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    writeErrorToLogFile(f'{tb}')
    QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("styles/styles.qss", "r") as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)
    app.setStyle("Fusion")
    locale.setlocale(locale.LC_ALL, 'de_DE')
    QtGui.QFontDatabase.addApplicationFont('font/Leoscar Sans Serif.ttf')
    QtGui.QFontDatabase.addApplicationFont('font/Leoscar Serif.ttf')
    QtGui.QFontDatabase.addApplicationFont('font/Orbitron-VariableFont_wght.ttf')

    sys.excepthook = exceptionHandler

    w = MainPage()
    sys.exit(app.exec())
