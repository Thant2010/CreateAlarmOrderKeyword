from PyQt6.QtCore import pyqtSignal, QObject


class SignalManager(QObject):

    onSelectKeyword = pyqtSignal(str, str)
    onEntryIsSaved = pyqtSignal(bool)

    def __init__(self):
        super().__init__()


signalManager = SignalManager()