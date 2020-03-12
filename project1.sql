CREATE database project1;

USE project1;

CREATE table Restaurants(
    Res_ID INT(5) AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    Price VARCHAR(4) NOT NULL
);

CREATE table Destination(
    Des_ID INT(5) AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    Opening_Time VARCHAR(5) NOT NULL
);

CREATE table Daytrip(
    Trip_ID INT(5) AUTO_INCREMENT PRIMARY KEY,
    Name_on_Booking VARCHAR(50) NOT NULL,
    No_of_People INT(5) NOT NULL,
    Trip_Res_ID INT(5), 
    FOREIGN KEY (Trip_Res_ID) REFERENCES Restaurants(Res_ID)
);

CREATE table DesJoin(
    Trip_ID INT(5),
    Destination_ID INT(5), 
    FOREIGN KEY (Trip_ID) REFERENCES Daytrip(Trip_ID),
    FOREIGN KEY (Destination_ID) REFERENCES Destination(Des_ID)
);


