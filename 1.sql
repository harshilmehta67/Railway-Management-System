create table train1(
    train_id int primary key,
    train_name varchar(20),
    starting_station_id int references station1(station_id),
    ending_station_id int references station1(station_id),
    starting_time float,  --in the form of HH.MM
    journey_time float , --denoting journey time in the form of HH.MM
    mon char(1),
    tue char(1),
    wed char(1),
    thu char(1),
    fri char(1),
    sat char(1),
    sun char(1)
)
--train id is 5 digit number
begin
insert into train1 values(10000, 'SaujantaExp' ,   100,   101,  13.00,  04.30, 'Y', 'N' ,'Y', 'N', 'Y', 'N', 'N');
insert into train1 values(10001, 'SaujantaExp2',   100,   103,  16.00,  07.30, 'N', 'Y' ,'Y', 'N', 'Y', 'N', 'Y');
insert into train1 values(10002, 'SaujantaExp3',   103,   102,  18.00,  05.30, 'N', 'Y' ,'Y', 'N', 'N', 'N', 'Y');
insert into train1 values(10003, 'mumtodelhi'  ,   104,   105,  10.00,  22.00, 'Y', 'Y' ,'Y', 'N', 'N', 'N', 'N');
insert into train1 values(10004, 'mumtosrt'    ,   104,   103,  15.30,  10.00, 'N', 'N' ,'Y', 'N', 'N', 'Y', 'Y');
insert into train1 values(10005, 'delhitorjk'  ,   105,   100,  9.30,   23.00, 'Y', 'Y' ,'N', 'N', 'N', 'Y', 'N');
end




--tier1  table is updated to table named as seat_class
create table seat_class1(
  train_id int references train1(train_id),
  sp int references train1(starting_station_id)
  ep int references train1(ending_station_id),
  price int ,
  class_category char(3),
  PRIMARY KEY (train_id, sp, ep, class_category)
)
--here class_category refers to AC1, AC2, AC3, CC,  EC, SL



create table station1(
    station_id int primary key,
    station_name varchar(20),
)
--3 digit station id
begin
insert into station1 values(100,'rjk');
insert into station1 values(101,'abd');
insert into station1 values(102,'brd');
insert into station1 values(103,'srt');
insert into station1 values(104,'mumbai');
insert into station1 values(105,'delhi');
insert into station1 values(106,'chennai')
insert into station1 values(107,'kolkatta')
end



create table ticket1(
--i think no need will include in passenger details because user with ticket is a passenger
)


create table user1(
    user_id int primary key,
    email_id varchar(50),
    name varchar(20),
    gender char(1),
    dob date,
    mobile_no int,   
)
--user id is 4 digit password for user1
--user id 1000 name ramesh
--6 digit mobile no
begin
insert into user1 values(1000,'ram@gmail.com','ram','M','01-01-2000',982370)
insert into user1 values(1001,'shyam@gmail.com','shyam','M','05-05-1987',123456)
insert into user1 values(1002,'rahim@gmail.com','rahim','M','6-12-2001',235415)
insert into user1 values(1003,'preeti@gmail.com','preeti','M','02-02-2002',432312)
end;




create table  passenger1 (
  passenger_id int references user1(user_id),
  pnr int references pnr_number_generation1(pnr),
  first_name varchar(20) ,
  last_name varchar(20)  ,
  gender char(1) NOT NULL,
  mobile_no char(10) DEFAULT NULL,  
) 
--to do how to generate pnr
create table pnr_number_generation1(
  pnr int;
  train_id int refernces train1(train_id),
  sp int references seat_class1(starting_station_id)
  ep int references seat_class1(ending_station_id),
  class_category references seat_class1(class_catefory)  
)

DROP TABLE IF EXISTS `Ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Ticket` (
  `Ticket_No` int(10) NOT NULL AUTO_INCREMENT,
  `Train_No` int(6) NOT NULL,
  `Date_of_Journey` date NOT NULL,
  `Username` varchar(15) NOT NULL,
  PRIMARY KEY (`Ticket_No`),
  KEY `Username` (`Username`),
  KEY `Train_No` (`Train_No`),
  CONSTRAINT `Ticket_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `Account` (`Username`) ON DELETE CASCADE,
  CONSTRAINT `Ticket_ibfk_2` FOREIGN KEY (`Train_No`) REFERENCES `Train` (`Train_No`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
