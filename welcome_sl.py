import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication

from view_resources import viewResources

class welcomeScreenSL(QtWidgets.QMainWindow):
    def __init__(self, username):
        # Call the inherited classes __init__ method
        super(welcomeScreenSL, self).__init__()

        # Load the .ui file
        uic.loadUi("welcome_screen.ui", self)
        self.label_2.setText("Welcome, " + username)
        self.viewResources.clicked.connect(self.vr)

    def vr(self):
        self.hide()
        self.res_win = viewResources()
        self.res_win.show()