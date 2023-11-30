from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class UpdateFinancesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Finances")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        amount_label = QLabel("Amount:")
        self.amount_input = QLineEdit()

        reason_label = QLabel("Reason:")
        self.reason_input = QLineEdit()

        update_button = QPushButton("Update Finances")
        update_button.clicked.connect(self.update_finances)

        layout.addWidget(amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(reason_label)
        layout.addWidget(self.reason_input)
        layout.addWidget(update_button)

        central_widget.setLayout(layout)

    def update_finances(self):
        amount = self.amount_input.text()
        reason = self.reason_input.text()
        print("Amount:", amount)
        print("Reason:", reason)
