import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QCalendarWidget,
    QPushButton,
    QWidget,
)


class BorrowResourceWindow(QMainWindow):
    def __init__(self, student_id="S12345"):
        super().__init__()
        self.student_id = student_id
        self.resource_names = ["Resource 1", "Resource 2", "Resource 3"]
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Borrow a Resource")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.lbl_student = QLabel(f"Student ID: {self.student_id}")
        self.lbl_select_resource = QLabel("Select a Resource:")
        self.cb_resource_names = QComboBox()
        self.cb_resource_names.addItems(self.resource_names)
        self.lbl_tentative_due_date = QLabel("Select a Tentative Due Date:")
        self.calendar_due_date = QCalendarWidget()
        self.btn_borrow = QPushButton("Request Resource")
        self.btn_borrow.clicked.connect(self.borrow_resource)

        layout.addWidget(self.lbl_student)
        layout.addWidget(self.lbl_select_resource)
        layout.addWidget(self.cb_resource_names)
        layout.addWidget(self.lbl_tentative_due_date)
        layout.addWidget(self.calendar_due_date)
        layout.addWidget(self.btn_borrow)
        central_widget.setLayout(layout)

    def borrow_resource(self):
        selected_resource = self.cb_resource_names.currentText()
        due_date = self.calendar_due_date.selectedDate().toString("yyyy-MM-dd")
        print(f"Student ID: {self.student_id}")
        print(f"Selected Resource: {selected_resource}")
        print(f"Tentative Due Date: {due_date}")


# def main():
#     app = QApplication(sys.argv)
#     student_id = 'S12345'
#     window = BorrowResourceWindow(student_id)
#     window.show()
#     sys.exit(app.exec())

# if __name__ == '__main__':
#     main()
