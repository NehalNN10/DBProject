import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout

class StudentLifeOfficeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Student Life Office Requests')
        self.setGeometry(100, 100, 600, 400)

        self.lbl_requests = QLabel('Pending Requests:')
        self.table_requests = QTableWidget()
        self.table_requests.setColumnCount(4)
        self.table_requests.setHorizontalHeaderLabels(
            ['Request ID', 'Resource ID', 'Borrower ID', 'Due Date'])

        self.btn_approve = QPushButton('Approve Request')
        self.btn_approve.clicked.connect(self.approve_request)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_requests)
        layout.addWidget(self.table_requests)
        layout.addWidget(self.btn_approve)

        self.setLayout(layout)

    def load_requests(self, requests):
        self.table_requests.setRowCount(len(requests))
        for i, request in enumerate(requests):
            self.table_requests.setItem(
                i, 0, QTableWidgetItem(str(request['request_id'])))
            self.table_requests.setItem(
                i, 1, QTableWidgetItem(str(request['resource_id'])))
            self.table_requests.setItem(
                i, 2, QTableWidgetItem(str(request['borrower_id'])))
            self.table_requests.setItem(
                i, 3, QTableWidgetItem(request['due_date']))

    def approve_request(self):
        selected_row = self.table_requests.currentRow()
        if selected_row != -1:
            request_id = self.table_requests.item(selected_row, 0).text()
            print(f'Approved Request ID: {request_id}')

def main():
    app = QApplication(sys.argv)
    window = StudentLifeOfficeWindow()
    requests = [
        {'request_id': 1, 'resource_id': 101,
            'borrower_id': 201, 'due_date': '10/15/2023'},
        {'request_id': 2, 'resource_id': 102,
            'borrower_id': 202, 'due_date': '10/18/2023'}
    ]
    window.load_requests(requests)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
