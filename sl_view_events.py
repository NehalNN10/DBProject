import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)

from datetime import datetime
from db_manager import db_manager


class PastEventsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Past Events")
        self.setGeometry(100, 100, 800, 400)

        self.db = db_manager()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(
            ["Club Name", "Location", "Date", "Time", "Budget"]
        )

        layout.addWidget(QLabel("Past Events"))
        layout.addWidget(self.table_widget)

        central_widget.setLayout(layout)

        self.populate_table()

    def populate_table(self):
        # Dummy data for past events (replace with data from your database)
        past_events = [
            # {
            #     "club_name": "Science Club",
            #     "location": "Auditorium",
            #     "date": "2023-11-10",
            #     "time": "10:00 AM",
            #     "budget": "$500",
            #     "feedback": "Good",
            # },
            # {
            #     "club_name": "Literature Club",
            #     "location": "Library",
            #     "date": "2023-11-15",
            #     "time": "2:00 PM",
            #     "budget": "$300",
            #     "feedback": "Excellent",
            # },
            # {
            #     "club_name": "Music Club",
            #     "location": "Open Ground",
            #     "date": "2023-11-20",
            #     "time": "5:00 PM",
            #     "budget": "$700",
            #     "feedback": "Satisfactory",
            # },
        ]

        self.db.connect()

        self.db.cursor.execute("SELECT * FROM Events")

        for row_data in self.db.cursor.fetchall():
            past_events.append(
                {
                    "event_name": row_data[1],
                    "location": row_data[4],
                    "date": row_data[2].strftime('%Y-%m-%d'),
                    "time": row_data[3].strftime('%H:%M-%D'),
                    "budget": str(row_data[5])
                }
            )

        self.db.close_connection()

        self.table_widget.setRowCount(len(past_events))
        for row, event in enumerate(past_events):
            self.table_widget.setItem(row, 0, QTableWidgetItem(event["event_name"]))
            self.table_widget.setItem(row, 1, QTableWidgetItem(event["location"]))
            self.table_widget.setItem(row, 2, QTableWidgetItem(event["date"]))
            self.table_widget.setItem(row, 3, QTableWidgetItem(event["time"]))
            self.table_widget.setItem(row, 4, QTableWidgetItem(event["budget"]))


# def main():
#     app = QApplication(sys.argv)
#     window = PastEventsWindow()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()
