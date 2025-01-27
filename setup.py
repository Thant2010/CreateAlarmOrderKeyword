import sys
import os
from cx_Freeze import setup, Executable
from os.path import dirname, join
import PyQt6

# Basisoption festlegen, um das Konsolenfenster zu unterdrücken (für GUI-Anwendungen)
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Pfad zu den PyQt6 Plugins (z.B. für Qt6 Widgets)
PYQT6_PLUGIN_DIR = os.path.join(dirname(PyQt6.__file__), 'Qt6', 'plugins')

# Build-Optionen definieren
build_exe_options = {
    "packages": [
        "json",
        "getpass",
        "datetime",
        "locale",
        "sys",
        "traceback",
        "os",
    ],
    "includes": [],
    "include_files": [
        # Ordner samt Inhalt einbinden
        ("font", "font"),
        ("icons", "icons"),
        ("json", "json"),
        ("styles", "styles"),
        # PyQt6 Plugins einbinden
        (PYQT6_PLUGIN_DIR, "Qt6/plugins"),
    ],
    # Optional: Excludes, um die Größe zu reduzieren
    "excludes": ["tkinter", "unittest"],
}

# Executable definieren
executables = [
    Executable(
        "start.py",            # Haupt-Python-Datei
        base=base,
        target_name="Create Alarm Order.exe",  # Benenne die ausführbare Datei nach Wunsch
        icon="icons/windowIcon.ico"  # Falls du ein Icon hast, gib hier den Pfad an, z.B. "icons/app.ico"
    )
]

# Setup-Aufruf
setup(
    name="Create Alarm Order",   # Name deiner Anwendung
    version="1.0",
    description="Erstellen und Bearbeitung einer Alarm- und Ausrückeordung",
    options={"build_exe": build_exe_options},
    executables=executables
)

# D:\Python\Projekte\AAO\Neue AAO\GitHub\CreateNewAlarmOrderKeyword\CreateAlarmOderKeyword> & "D:\Python\Python 3.12\python.exe" setup.py build
