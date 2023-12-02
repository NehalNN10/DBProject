# Importing essential modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QHeaderView,
)

from welcome import welcomeScreenSL
from db_manager import db_manager
import sys

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Login, self).__init__()

        # Load the .ui file
        uic.loadUi("login.ui", self)
        self.login_btn.clicked.connect(self.loginBtn)

    def loginBtn(self):
        # ? determining user type
        temp = self.userID.toPlainText().strip().split("@")
        if temp[1][:2] == "st":
            usertype = "Student"
        else:
            usertype = "SL"
        del temp
        print(usertype)

        # printing out password for testing purposes
        print(self.passwordEntry.text())
        self.userID.setPlainText("")
        self.passwordEntry.setText("")

        self.hide()
        self.club_info = welcomeScreenSL()
        self.club_info.show()
