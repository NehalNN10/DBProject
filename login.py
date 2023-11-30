import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.login_btn.clicked.connect(self.club_information_screen)

    def club_information_screen(self):
        self.hide()
        self.club_info = ClubInfo()
        self.club_info.show()

def main():
    app = QApplication(sys.argv)
    student_id = 'S12345'
    window = Login()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()