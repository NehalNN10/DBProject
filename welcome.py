import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication

class welcomeScreenSL(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(welcomeScreenSL, self).__init__()

        # Load the .ui file
        uic.loadUi("welcome_screen.ui", self)