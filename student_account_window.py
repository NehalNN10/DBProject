import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout

class StudentAccountWindow(QWidget):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Student Resource Account')
        self.setGeometry(100, 100, 600, 400)

        borrowed_resources = [
            {'resource_id': '001', 'resource_name': 'Microphone', 'due_date': '2023-11-30'},
            {'resource_id': '002', 'resource_name': 'Camera', 'due_date': '2023-12-15'},
            {'resource_id': '003', 'resource_name': 'Flash drive', 'due_date': '2023-12-10'},
        ]

        self.lbl_account = QLabel(f'Student Account: {self.student_id}')
        self.table_account = QTableWidget()
        self.table_account.setColumnCount(3)
        self.table_account.setHorizontalHeaderLabels(['Resource ID', 'Resource Name', 'Due Date'])
        self.table_account.setRowCount(len(borrowed_resources))

        for row, resource in enumerate(borrowed_resources):
            self.table_account.setItem(row, 0, QTableWidgetItem(resource['resource_id']))
            self.table_account.setItem(row, 1, QTableWidgetItem(resource['resource_name']))
            self.table_account.setItem(row, 2, QTableWidgetItem(resource['due_date']))

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_account)
        layout.addWidget(self.table_account)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    student_id = 'S12345'
    window = StudentAccountWindow(student_id)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
