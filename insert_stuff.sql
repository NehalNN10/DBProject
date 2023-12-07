-- Clear all data from tables
DELETE FROM Resources;
DELETE FROM Teams;
DELETE FROM StudentLife_Staff;
DELETE FROM Club_Teams;
DELETE FROM Borrowed_Resources;
DELETE FROM Events;
DELETE FROM Member_Attendance;
DELETE FROM Students;
DELETE FROM Event_Request;
DELETE FROM Clubs;
DELETE FROM Borrower;
DELETE FROM EventClub;
DELETE FROM Club_member;
DELETE FROM Club_Funds_Tracker;
DELETE FROM EventFeedback;

-- Insert into Resources table
SET IDENTITY_INSERT Resources ON;
INSERT INTO Resources (Resource_ID, Resource_Name, Value, Purchase_Date) VALUES
    (1, 'Microphone', 150.00, '2023-01-15'),
    (2, 'Camera', 500.00, '2023-03-20'),
    (3, 'Flash drive', 20.00, '2023-05-10');
SET IDENTITY_INSERT Resources OFF;

-- Insert into Teams table
SET IDENTITY_INSERT Teams ON;
INSERT INTO Teams (Team_ID, Team_Name) VALUES
    (1, 'Team A'),
    (2, 'Team B'),
    (3, 'Team C');
SET IDENTITY_INSERT Teams OFF;

-- Insert into StudentLife_Staff table
SET IDENTITY_INSERT StudentLife_Staff ON;
INSERT INTO StudentLife_Staff (Staff_ID, Staff_Name) VALUES
    (101, 'John Doe'),
    (102, 'Jane Smith'),
    (103, 'Alice Johnson');
SET IDENTITY_INSERT StudentLife_Staff OFF;

-- Insert into Club_Teams table
SET IDENTITY_INSERT Club_Teams ON;
INSERT INTO Club_Teams (Team_ID, Club_Name) VALUES
    (1, 'Science Club'),
    (2, 'Literature Club'),
    (3, 'Music Club');
SET IDENTITY_INSERT Club_Teams OFF;

-- Insert into Borrowed_Resources table
SET IDENTITY_INSERT Borrowed_Resources ON;
INSERT INTO Borrowed_Resources (Resource_ID, Borrower_ID, Event_ID, Due_Date) VALUES
    (1, 101, 201, '2023-08-20'),
    (2, 102, 202, '2023-09-10'),
    (3, 103, 203, '2023-07-25');
SET IDENTITY_INSERT Borrowed_Resources OFF;

-- Insert into Events table
SET IDENTITY_INSERT Events ON;
INSERT INTO Events (Event_Name, Date, Time, Location, Budget) VALUES
    ('Science Fair', '2023-08-15', '10:00:00', 'Auditorium', 1000.00),
    ('Literature Symposium', '2023-09-05', '13:00:00', 'Library', 800.00),
    ('Music Concert', '2023-07-20', '19:00:00', 'Open Ground', 1200.00);
SET IDENTITY_INSERT Events OFF;

-- Insert into Member_Attendance table
SET IDENTITY_INSERT Member_Attendence ON;
INSERT INTO Member_Attendance (Event_ID, Student_ID, Attended) VALUES
    (201, 'S12345', 1),
    (202, 'S23456', 0),
    (203, 'S34567', 1);
SET IDENTITY_INSERT Memeber_Attendence OFF;

-- Insert into Students table
SET IDENTITY_INSERT Students ON;
INSERT INTO Students (Student_ID, Student_Name) VALUES
    ('S12345', 'John Doe'),
    ('S23456', 'Jane Smith'),
    ('S34567', 'Alice Johnson');
SET IDENTITY_INSERT Students OFF;

-- Insert into Event_Request table
SET IDENTITY_INSERT Event_Request ON;
INSERT INTO Event_Request (Event_Request_ID, Event_Name, Club_Name, Date, Time, Location, Budget, Approved, Approving_staff_ID) VALUES
    (301, 'Seminar', 'Science Club', '2023-10-10', '14:00:00', 'Conference Hall', 500.00, 1, 101),
    (302, 'Drama Festival', 'Literature Club', '2023-11-05', '18:00:00', 'Auditorium', 700.00, 0, NULL),
    (303, 'Charity Concert', 'Music Club', '2023-12-15', '20:00:00', 'Open Ground', 1000.00, 0, NULL);
SET IDENTITY_INSERT Event_Request OFF;

-- Insert into Clubs table
SET IDENTITY_INSERT Clubs ON;
INSERT INTO Clubs (Club_Name, Funds) VALUES
    ('Science Club', 5000.00),
    ('Literature Club', 3000.00),
    ('Music Club', 7000.00);
SET IDENTITY_INSERT Clubs OFF;

-- Insert into Borrower table
SET IDENTITY_INSERT Borrower ON;
INSERT INTO Borrower (Borrower_ID, Team_ID, Club_Name, Student_ID, Role) VALUES
    (101, 1, 'Science Club', 'S12345', 'President'),
    (102, 2, 'Literature Club', 'S23456', 'Vice President'),
    (103, 3, 'Music Club', 'S34567', 'Secretary');
SET IDENTITY_INSERT Borrower OFF;

-- Insert into EventClub table
SET IDENTITY_INSERT EventClub ON;
INSERT INTO EventClub (Event_ID, Club_Name) VALUES
    (201, 'Science Club'),
    (202, 'Literature Club'),
    (203, 'Music Club');
SET IDENTITY_INSERT EventClub OFF;

-- Insert into Club_member table
SET IDENTITY_INSERT Event_Request ON;
INSERT INTO Club_member (Club_Name, Student_ID, Team_ID, Position) VALUES
    ('Science Club', 'S12345', 1, 'President'),
    ('Literature Club', 'S23456', 2, 'Vice President'),
    ('Music Club', 'S34567', 3, 'Secretary');
SET IDENTITY_INSERT Event_Request OFF;

-- Insert into Club_Funds_Tracker table
SET IDENTITY_INSERT Club_Funds_Tracker ON;
INSERT INTO Club_Funds_Tracker (Club_Name, Amount, Reason) VALUES
    ('Science Club', 1000.00, 'Fundraising'),
    ('Literature Club', 500.00, 'Event expenses'),
    ('Music Club', 1200.00, 'Equipment purchase');
SET IDENTITY_INSERT Club_Funds_Tracker OFF;

-- Insert into EventFeedback table
SET IDENTITY_INSERT EventFeedback ON;
INSERT INTO EventFeedback (Event_ID, Student_ID, Feedback) VALUES
    (201, 'S12345', 'Great event, well organized!'),
    (202, 'S23456', 'Good effort, but needs improvement.'),
    (203, 'S34567', 'Excellent performance, enjoyed it!');
SET IDENTITY_INSERT EventFeedback OFF;
