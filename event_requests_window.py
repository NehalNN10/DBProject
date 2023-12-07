import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from db_manager import db_manager


class EventRequestsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.db = db_manager()
        self.load_event_requests()

    def init_ui(self):
        self.setWindowTitle("Event Requests")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.lbl_requests = QLabel("Event Requests:")
        layout.addWidget(self.lbl_requests)

        self.table_requests = QTableWidget()
        self.table_requests.setColumnCount(4)
        self.table_requests.setHorizontalHeaderLabels(
            ["Event Request ID", "Club Name", "Event Name", "Event Description"]
        )
        layout.addWidget(self.table_requests)

        self.btn_approve = QPushButton("Approve Event")
        self.btn_approve.clicked.connect(self.approve_event)
        layout.addWidget(self.btn_approve)

        self.btn_reject = QPushButton("Reject Event")
        layout.addWidget(self.btn_reject)
        self.btn_approve.clicked.connect(self.reject_event)

        central_widget.setLayout(layout)

        # self.table_requests.itemClicked.connect(self.row_clicked)

    # def row_clicked(self, item):
    # current_row = item.row()
    #
    # event_request_id = self.table_requests.item(current_row, 0).text()
    # club_name = self.table_requests.item(current_row, 1).text()
    # event_name = self.table_requests.item(current_row, 2).text()
    # event_description = self.table_requests.item(current_row, 3).text()

    def load_event_requests(self):
        event_requests = [
            {
                "event_request_id": 1,
                "club_name": "Science Club",
                "event_name": "Science Fair",
                "event_description": "An exhibition of science projects",
            },
            {
                "event_request_id": 2,
                "club_name": "Music Club",
                "event_name": "Concert",
                "event_description": "Live music performance",
            },
        ]

        self.db.connect()

        self.db.cursor.execute("SELECT * FROM Event_Request WHERE Approved = 0")

        for row_data in self.db.cursor.fetchall():
            event_requests.append(
                {
                    "event_request_id": row_data[0],
                    "club_name": row_data[2],
                    "event_name": row_data[1],
                    "event_description": "Nada",
                }
            )

        self.db.close_connection()

        self.table_requests.setRowCount(len(event_requests))
        for i, request in enumerate(event_requests):
            self.table_requests.setItem(
                i, 0, QTableWidgetItem(str(request["event_request_id"]))
            )
            self.table_requests.setItem(i, 1, QTableWidgetItem(request["club_name"]))
            self.table_requests.setItem(i, 2, QTableWidgetItem(request["event_name"]))
            self.table_requests.setItem(
                i, 3, QTableWidgetItem(request["event_description"])
            )

    def approve_event(self):
        selected_row = self.table_requests.currentRow()
        if selected_row != -1:
            event_request_id = self.table_requests.item(selected_row, 0).text()
            print(f"Approved Event Request ID: {event_request_id}")

            self.db.connect()

            # Update the Event_Request's Approved status to 1 (approved)
            self.db.cursor.execute(
                """
                UPDATE Event_Request
                SET Approved = 1
                WHERE Event_Request_ID = ?
                """,
                (event_request_id,),
            )
            self.db.cursor.commit()

            # Retrieve the details of the approved event request
            self.db.cursor.execute(
                """
                SELECT Event_Name, Date, Time, Location, Budget
                FROM Event_Request
                WHERE Event_Request_ID = ?
                """,
                (event_request_id,),
            )
            event_details = self.db.cursor.fetchone()

            if event_details:
                # Insert a new record into the Events table using the retrieved details
                self.db.cursor.execute(
                    """
                    INSERT INTO Events(Event_Name, Date, Time, Location, Budget)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    event_details[1:6],
                )
                self.db.cursor.commit()
                print("New event record inserted into Events table")

            self.db.close_connection()

    def reject_event(self):
        selected_row = self.table_requests.currentRow()
        if selected_row != -1:
            event_request_id = self.table_requests.item(selected_row, 0).text()
            print(f"Rejected Event Request ID: {event_request_id}")

            self.db.connect()

            # Update the Event_Request's Approved status to 2 (rejected)
            self.db.cursor.execute(
                """
                UPDATE Event_Request
                SET Approved = 0
                WHERE Event_Request_ID = ?
                """,
                (event_request_id,)
            )
            self.db.cursor.commit()

            self.db.close_connection()
