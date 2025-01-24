from PyQt5.QtCore import pyqtSignal, QObject


class SignalManager(QObject):

    onSelectKeyword = pyqtSignal(list)

    def __init__(self):
        super().__init__()


signalManager = SignalManager()