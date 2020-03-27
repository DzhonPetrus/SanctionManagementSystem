# DROP DATABASE SANCTION_MANAGEMENT;
CREATE DATABASE SANCTION_MANAGEMENT
USE SANCTION_MANAGEMENT

CREATE TABLE _USER(
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    _Username varchar(25) NOT NULL,
    _Password varchar(25) NOT NULL,
    _Role BIT DEFAULT(0)
)

CREATE TABLE ADDRESS(
    AddressID varchar(25) PRIMARY KEY,
    UnitNo varchar(20),
    StreetName varchar(20),
    Brgy varchar(20),
    City varchar(30),
    ZipCode varchar(5)

)

CREATE TABLE STUDENT(
    StudentNo varchar(25) PRIMARY KEY NOT NULL,
    FName varchar(25) NOT NULL,
    MName varchar(25) NOT NULL,
    LName varchar(25) NOT NULL,
    XTName varchar(3),
    ContactNo varchar(11),
    Email varchar(25),
    AddressID varchar(25),
    DateOfBirth DATE,
    Course varchar(15),
    Section varchar(10),
    SchoolYear int,
    FOREIGN KEY(AddressID) REFERENCES ADDRESS(AddressID)
)

CREATE TABLE SANCTIONTYPE(
    TypeID VARCHAR(10) PRIMARY KEY NOT NULL,
    _Description TINYTEXT NOT NULL
)

CREATE TABLE SANCTION(
    SanctionCode VARCHAR(10) PRIMARY KEY NOT NULL,
    TypeID VARCHAR(10) NOT NULL,
    _Description TINYTEXT NOT NULL,
    FOREIGN KEY(TypeID)  REFERENCES SANCTIONTYPE(TypeID)
)

CREATE TABLE SANCTIONLOG(
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    StudentNo varchar(25),
    SanctionCode varchar(10),
    DateLog DATETIME DEFAULT CURRENT_TIMESTAMP(),
    _Status ENUM('PENDING', 'PARTIAL', 'SERVED') DEFAULT 'PENDING',
    DateUpdated DATETIME ON UPDATE CURRENT_TIMESTAMP(),
    Remarks TINYTEXT,
    Duration TIME,
    FOREIGN KEY(StudentNo) REFERENCES STUDENT(StudentNo),
    FOREIGN KEY(SanctionCode) REFERENCES SANCTION(SanctionCode)
)

CREATE TABLE SERVICE(
    ServiceID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    LogID int,
    TimeIn TIME DEFAULT CURRENT_TIME(),
    TimeOut TIME, #ON UPDATE NOT SUPPORTED
    ServiceDate DATE DEFAULT CURRENT_DATE(),
    FOREIGN KEY(LogID) REFERENCES SANCTIONLOG(LogID)
)
