from PyQt6 import QtWidgets, uic

class EventInput(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('events.ui', self)
