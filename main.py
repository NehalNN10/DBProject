import sys
from PyQt6 import QtWidgets
from welcome_s import Welcome_S
from update_finances_window import UpdateFinancesWindow
# Import other classes as needed
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Welcome_S()
    window.show()
    sys.exit(app.exec())
