CREATE TABLE [Resource_Request] (
    Resource_Request_ID int IDENTITY(1,1) PRIMARY KEY,
    Resource_ID int NOT NULL,
    Borrower_ID int NOT NULL,
    Due_Date date NOT NULL,
    Approved BIT,
    Approving_staff_ID int
);

CREATE TABLE [Resources] (
    Resource_ID int IDENTITY(1,1) PRIMARY KEY,
    Resource_Name varchar(100) NOT NULL,
    Value decimal NOT NULL,
    Purchase_Date date NOT NULL
);

CREATE TABLE [Teams] (
    Team_ID int IDENTITY(1,1) PRIMARY KEY,
    Team_Name varchar(100) NOT NULL
);

CREATE TABLE [StudentLife_Staff] (
    Staff_ID int IDENTITY(1,1) PRIMARY KEY,
    Staff_Name varchar(100) NOT NULL
);

CREATE TABLE [Club_Teams] (
    Team_ID int IDENTITY(1,1) PRIMARY KEY,
    Club_Name varchar(100) NOT NULL
);

CREATE TABLE [Borrowed_Resources] (
    Resource_ID int IDENTITY(1,1) PRIMARY KEY,
    Borrower_ID int NOT NULL,
    Event_ID int NOT NULL,
    Due_Date date NOT NULL
);

CREATE TABLE [Events] (
    Event_ID int IDENTITY(1,1) PRIMARY KEY,
    Event_Name varchar(100) NOT NULL,
    Date date NOT NULL,
    Time time NOT NULL,
    Location varchar(100) NOT NULL,
    Budget decimal NOT NULL
);

CREATE TABLE [Member_Attendance] (
    Attendance_ID int IDENTITY(1,1) PRIMARY KEY,
    Event_ID int NOT NULL,
    Student_ID varchar(100) NOT NULL,
    Attended BIT NOT NULL
);

CREATE TABLE [Students] (
    Student_ID varchar(100) PRIMARY KEY,
    Student_Name varchar(100) NOT NULL
);

CREATE TABLE [Event_Request] (
    Event_Request_ID int IDENTITY(1,1) PRIMARY KEY,
    Event_Name varchar(100) NOT NULL,
    Club_Name varchar(100) NOT NULL,
    Date date NOT NULL,
    Time time NOT NULL,
    Location varchar(100) NOT NULL,
    Budget decimal NOT NULL,
    Approved BIT NOT NULL,
    Approving_staff_ID int
);

CREATE TABLE [Clubs] (
    Club_Name varchar(100) PRIMARY KEY,
    Funds decimal NOT NULL
);

CREATE TABLE [Borrower] (
    Borrower_ID int IDENTITY(1,1) PRIMARY KEY,
    Team_ID int NOT NULL,
    Club_Name varchar(100) NOT NULL,
    Student_ID varchar(100) NOT NULL,
    Role varchar(100) NOT NULL
);

CREATE TABLE [EventClub] (
    EventClub_ID int IDENTITY(1,1) PRIMARY KEY,
    Event_ID int NOT NULL,
    Club_Name varchar(100) NOT NULL
);

CREATE TABLE [Club_member] (
    ClubMember_ID int IDENTITY(1,1) PRIMARY KEY,
    Club_Name varchar(100) NOT NULL,
    Student_ID varchar(100) NOT NULL,
    Team_ID int NOT NULL,
    Position varchar(100) NOT NULL
);

CREATE TABLE [Club_Funds_Tracker] (
    ClubFundsTracker_ID int IDENTITY(1,1) PRIMARY KEY,
    Club_Name varchar(100) NOT NULL,
    Amount decimal NOT NULL,
    Reason varchar(100) NOT NULL
);

CREATE TABLE [EventFeedback] (
    EventFeedback_ID int IDENTITY(1,1) PRIMARY KEY,
    Event_ID int NOT NULL,
    Student_ID varchar(100) NOT NULL,
    Feedback varchar(100) NOT NULL
);
