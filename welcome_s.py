import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication

class Welcome_S(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('welcome_screen_student.ui', self)

def main():
    app = QApplication(sys.argv)
    student_id = 'S12345'
    window = Welcome_S()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
