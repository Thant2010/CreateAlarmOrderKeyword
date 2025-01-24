from PyQt5.QtCore import pyqtSignal, QObject
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class SignalManager(QObject):
    # Definiere das Signal als Instanzattribut
    selection_signal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

    def emit_selection(self, category, keyword):
        """Instanzmethode zum Auslösen des Signals"""
        self.selection_signal.emit(category, keyword)

    def connect_signal(self, slot):
        """Instanzmethode zum Verbinden des Signals mit einem Slot"""
        self.selection_signal.connect(slot)

    @staticmethod
    def get_instance():
        """Statische Methode, um die einzige Instanz des SignalManagers zu erhalten"""
        if not hasattr(SignalManager, '_instance'):
            SignalManager._instance = SignalManager()
        return SignalManager._instance

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # SignalManager-Instanz holen und Signal verbinden
        self.signal_manager = SignalManager.get_instance()
        self.signal_manager.connect_signal(self.update_labels)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hauptfenster')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Ausgewählte Kategorie und Schlüsselwort: ', self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        # Button zum Öffnen des zweiten Fensters
        self.open_button = QPushButton('Öffne Auswahlfenster', self)
        self.open_button.clicked.connect(self.open_selection_window)
        self.layout.addWidget(self.open_button)

        self.setLayout(self.layout)

    def open_selection_window(self):
        # Öffne das Auswahlfenster
        self.selection_window = SelectionWindow()
        self.selection_window.show()

    def update_labels(self, category, keyword):
        self.label.setText(f'Kategorie: {category}, Schlüsselwort: {keyword}')

class SelectionWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Auswahlfenster')
        self.setGeometry(400, 100, 300, 200)

        self.layout = QVBoxLayout()

        # Beispiel für die Daten, die über den Doppelklick übergeben werden
        self.items = [
            ('Kategorie1', 'Schlüsselwort1'),
            ('Kategorie2', 'Schlüsselwort2'),
            ('Kategorie3', 'Schlüsselwort3')
        ]

        # Buttons für jedes Element in der Liste
        for category, keyword in self.items:
            button = QPushButton(f'{category} - {keyword}', self)
            button.clicked.connect(lambda checked, c=category, k=keyword: self.on_item_selected(c, k))
            self.layout.addWidget(button)

        self.setLayout(self.layout)

    def on_item_selected(self, category, keyword):
        # Signal auslösen, wenn ein Element ausgewählt wird
        signal_manager = SignalManager.get_instance()  # SignalManager-Instanz holen
        signal_manager.emit_selection(category, keyword)
        self.close()  # Fenster schließen nach Auswahl


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Erstelle das Hauptfenster
    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())
