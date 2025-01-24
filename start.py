import locale
import sys
import traceback

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from UtilityFunctions.writeErrorToLogFile import writeErrorToLogFile
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
    QtGui.QFontDatabase.addApplicationFont('Font/Leoscar Sans Serif.ttf')
    QtGui.QFontDatabase.addApplicationFont('Font/Leoscar Serif.ttf')
    QtGui.QFontDatabase.addApplicationFont('font/Orbitron-VariableFont_wght.ttf')

    sys.excepthook = exceptionHandler

    w = MainPage()
    #w = TreeViewWindow()
    sys.exit(app.exec_())
