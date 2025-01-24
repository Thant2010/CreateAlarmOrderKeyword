from PySide6.QtCore import Signal, QObject


class SignalManager(QObject):

    onSelectKeyword = Signal(list)

    def __init__(self):
        super().__init__()


signalManager = SignalManager()