from PyQt6 import QtWidgets, uic
class ClubInfo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('club_info.ui', self)
