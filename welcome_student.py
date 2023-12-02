import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication


class welcomeScreenStudent(QtWidgets.QMainWindow):
    def __init__(self, username):
        # Call the inherited classes __init__ method
        super(welcomeScreenStudent, self).__init__()

        # Load the .ui file
        uic.loadUi("welcome_screen.ui", self)
        self.label_2.setText("Welcome, " + username)
