# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from main_window import MainWindow

LOAD_UI_STATIC  = True

def load_ui_dynamic():
        ui_file_name = "alternativewindow.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        global window
        window = loader.load(ui_file)
        ui_file.close()
        if not window:
            print(loader.errorString())
            sys.exit(-1)

def load_ui_static():
    global window
    window = MainWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if LOAD_UI_STATIC:
        load_ui_static()
    else:
        load_ui_dynamic()
    window.show()

    sys.exit(app.exec())


