CREATE TABLE [Resource_Request] (
    Resource_Request_ID int IDENTITY(1,1) PRIMARY KEY,
    Resource_ID int NOT NULL,
    Borrower_ID int NOT NULL,
    Due_Date date NOT NULL,
    Approved BIT,
    Approving_staff_ID int,
    CONSTRAINT [FK_Resource_Request_Resources] FOREIGN KEY ([Resource_ID]) REFERENCES [Resources]([Resource_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Resource_Request_Borrower] FOREIGN KEY ([Borrower_ID]) REFERENCES [Borrower]([Borrower_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Resource_Request_Staff] FOREIGN KEY ([Approving_staff_ID]) REFERENCES [StudentLife_Staff]([Staff_ID]) ON UPDATE CASCADE
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
    Club_Name varchar(100) NOT NULL,
    CONSTRAINT [FK_Club_Teams_Teams] FOREIGN KEY ([Team_ID]) REFERENCES [Teams]([Team_ID]) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE [Borrowed_Resources] (
    Resource_ID int IDENTITY(1,1) PRIMARY KEY,
    Borrower_ID int NOT NULL,
    Event_ID int NOT NULL,
    Due_Date date NOT NULL,
    CONSTRAINT [FK_Borrowed_Resources_Resources] FOREIGN KEY ([Resource_ID]) REFERENCES [Resources]([Resource_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Borrowed_Resources_Borrower] FOREIGN KEY ([Borrower_ID]) REFERENCES [Borrower]([Borrower_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Borrowed_Resources_Events] FOREIGN KEY ([Event_ID]) REFERENCES [Events]([Event_ID]) ON UPDATE CASCADE
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
    Attended BIT NOT NULL,
    CONSTRAINT [FK_Member_Attendance_Events] FOREIGN KEY ([Event_ID]) REFERENCES [Events]([Event_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Member_Attendance_Students] FOREIGN KEY ([Student_ID]) REFERENCES [Students]([Student_ID]) ON UPDATE CASCADE
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
    Approving_staff_ID int,
    CONSTRAINT [FK_Event_Request_Clubs] FOREIGN KEY ([Club_Name]) REFERENCES [Clubs]([Club_Name]) ON UPDATE CASCADE
);

-- Continue modifying the remaining tables using the IDENTITY property for primary keys

CREATE TABLE [Clubs] (
    Club_ID int IDENTITY(1,1) PRIMARY KEY,
    Club_Name varchar(100) NOT NULL,
    Funds decimal NOT NULL
);

CREATE TABLE [Borrower] (
    Borrower_ID int IDENTITY(1,1) PRIMARY KEY,
    Team_ID int NOT NULL,
    Club_Name varchar(100) NOT NULL,
    Student_ID varchar(100) NOT NULL,
    Role varchar(100) NOT NULL,
    CONSTRAINT [FK_Borrower_Teams] FOREIGN KEY ([Team_ID]) REFERENCES [Teams]([Team_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Borrower_Clubs] FOREIGN KEY ([Club_Name]) REFERENCES [Clubs]([Club_Name]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Borrower_Students] FOREIGN KEY ([Student_ID]) REFERENCES [Students]([Student_ID]) ON UPDATE CASCADE
);

CREATE TABLE [EventClub] (
    EventClub_ID int IDENTITY(1,1) PRIMARY KEY,
    Event_ID int NOT NULL,
    Club_Name varchar(100) NOT NULL,
    CONSTRAINT [FK_EventClub_Events] FOREIGN KEY ([Event_ID]) REFERENCES [Events]([Event_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_EventClub_Clubs] FOREIGN KEY ([Club_Name]) REFERENCES [Clubs]([Club_Name]) ON UPDATE CASCADE
);

CREATE TABLE [Club_member] (
    ClubMember_ID int IDENTITY(1,1) PRIMARY KEY,
    Club_Name varchar(100) NOT NULL,
    Student_ID varchar(100) NOT NULL,
    Team_ID int NOT NULL,
    Position varchar(100) NOT NULL,
    CONSTRAINT [FK_Club_member_Clubs] FOREIGN KEY ([Club_Name]) REFERENCES [Clubs]([Club_Name]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Club_member_Students] FOREIGN KEY ([Student_ID]) REFERENCES [Students]([Student_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_Club_member_Teams] FOREIGN KEY ([Team_ID]) REFERENCES [Teams]([Team_ID]) ON UPDATE CASCADE
);

CREATE TABLE [Club_Funds_Tracker] (
    ClubFundsTracker_ID int IDENTITY(1,1) PRIMARY KEY,
    Club_Name varchar(100) NOT NULL,
    Amount decimal NOT NULL,
    Reason varchar(100) NOT NULL,
    CONSTRAINT [FK_Club_Funds_Tracker_Clubs] FOREIGN KEY ([Club_Name]) REFERENCES [Clubs]([Club_Name]) ON UPDATE CASCADE
);

CREATE TABLE [EventFeedback] (
    EventFeedback_ID int IDENTITY(1,1) PRIMARY KEY,
    Event_ID int NOT NULL,
    Student_ID varchar(100) NOT NULL,
    Feedback varchar(100) NOT NULL,
    CONSTRAINT [FK_EventFeedback_Events] FOREIGN KEY ([Event_ID]) REFERENCES [Events]([Event_ID]) ON UPDATE CASCADE,
    CONSTRAINT [FK_EventFeedback_Students] FOREIGN KEY ([Student_ID]) REFERENCES [Students]([Student_ID]) ON UPDATE CASCADE
);