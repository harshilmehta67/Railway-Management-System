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
insert into train1 values(10006,  'ontime'     ,   104,   101,  13.30,  05.45, 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y');
end


create table seat_class2(
  train_id int references train1(train_id),
  working_day int,
  AC1_price int ,
  AC1_total_seats int ,
  AC1_booked_seats int ,
  AC2_price int ,
  AC2_total_seats int ,
  AC2_booked_seats int ,
  AC3_price int ,
  AC3_total_seats int ,
  AC3_booked_seats int ,
  CC_price int ,
  CC_total_seats int ,
  CC_booked_seats int ,
  EC_price int ,
  EC_total_seats int ,
  EC_booked_seats int ,
  SL_price int ,
  SL_total_seats int ,
  SL_booked_seats int ,
  PRIMARY KEY (train_id, working_day)
)
insert into seat_class2 values(10000, 1, 800,50,0, 500,50,0, 0,0,0, 200,100,0, 340,110,0, 0,0,0)
insert into seat_class2 values(10000, 3, 800,50,0, 500,50,0, 0,0,0, 200,100,0, 340,110,0, 0,0,0)
insert into seat_class2 values(10000, 5, 800,50,0, 500,50,0, 0,0,0, 200,100,0, 340,110,0, 0,0,0)

--tier1  table is updated to table named as seat_class
create table seat_class1(
  train_id int references train1(train_id),
  sp int references train1(starting_station_id)
  ep int references train1(ending_station_id),
  price int ,
  total_seats,
  booked_seats,
  class_category varchar(3),
  PRIMARY KEY (train_id, sp, ep, class_category)
)
insert into seat_class1 values(10006, 104, 101, 101,  800,  50, 0, 'AC1')
insert into seat_class1 values(10006, 104, 101, 101,  500,  50, 0, 'AC2')
insert into seat_class1 values(10006, 104, 101, 101,    0,   0, 0, 'AC3')
insert into seat_class1 values(10006, 104, 101, 101,  200, 100, 0, 'CC')
insert into seat_class1 values(10006, 104, 101, 101,    0,   0, 0, 'EC')
insert into seat_class1 values(10006, 104, 101, 101,  340, 110, 0, 'SL')
--here class_category refers to AC1, AC2, AC3, CC,  EC, SL



create table station1(
    station_id int primary key,
    station_name varchar(20)
)
--3 digit station id
begin
	insert into station1 values(100,'rjk');
	insert into station1 values(101,'abd');
	insert into station1 values(102,'brd');
	insert into station1 values(103,'srt');
	insert into station1 values(104,'mumbai');
	insert into station1 values(105,'delhi');
	insert into station1 values(106,'chennai');
	insert into station1 values(107,'kolkatta');
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


------------------------------------------------------------------------------------------------------
--procedure for schedule: input is from station id and to station id , date
--output is table

create or replace function dis_train2(s_stat int, e_stat int, tarik date)
returns table(
s_stat_name varchar(20),
e_stat_name varchar(20),
t_name varchar(20),
s_time float,
j_time float,
ac1_p int,
ac1_s int,
ac2_p int,
ac2_s int,
ac3_p int,
ac3_s int,
cc_p int,
cc_s int,
ec_p int,
ec_s int,
sl_p int,
sl_s int
)
as $dis_train2$
declare
dayno int;
begin
	select extract(dow from  tarik) into dayno;
	return query
	select distinct 
	(select station_name from station1 where station_id=s_stat),
	(select station_name from station1 where station_id=e_stat),
	train1.train_name,train1.starting_time,train1.journey_time,
	seat_class2.ac1_price,seat_class2.ac1_total_seats,
	seat_class2.ac2_price,seat_class2.ac2_total_seats,
	seat_class2.ac3_price,seat_class2.ac3_total_seats,
	seat_class2.cc_price,seat_class2.cc_total_seats,
	seat_class2.ec_price,seat_class2.ec_total_seats,
	seat_class2.sl_price,seat_class2.sl_total_seats
	from train1,seat_class2,station1
	where(train1.starting_station_id=s_stat and train1.ending_station_id=e_stat and train1.train_id=seat_class2.train_id 
		  and seat_class2.working_day=dayno);
end;
$dis_train2$ language plpgsql;
select dis_train2(100,101,'04-08-2020')


----function for cheking user id dummy values---------------------------------------------------------------
create or replace function check_user_id(u_id int)
returns int as $check_user_id$
  declare
    is_pre int;
  begin
    is_pre :=0;
    select count(*) into is_pre from user1 where user_id=u_id;
      if(is_pre=1) then
        raise notice 'Already exists';
      else
        raise notice 'New user';
      end if;
    return is_pre;
  end;
$check_user_id$ language plpgsql; 

select check_user_id(1000);

-----------------function for book seat ------------------------------------------------------------------
select book_seat(10000,1,'ac1')

create or replace function book_seat(t_id int, days int, categ varchar)
returns int as $book_seat$
declare
che int;
begin
	if(categ='ac1') then
		select ac1_total_seats into che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=0)then
			raise notice'No seets left';
		else
			update seat_class2 set ac1_total_seats=ac1_total_seats-1,ac1_booked_seats=ac1_booked_seats+1
			where(train_id = t_id and working_day=days);
		return ac1_price from seat_class2 where(train_id = t_id and working_day=days) ;
		end if;
	elsif(categ='ac2')then
		select ac2_total_seats into che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=0)then
			raise notice'No seets left';
		else
			update seat_class2 set ac2_total_seats=ac2_total_seats-1,ac2_booked_seats=ac2_booked_seats+1
			where(train_id = t_id and working_day=days);
		return ac2_price from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	elsif(categ='ac3')then
		select ac3_total_seats into che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=0)then
			raise notice'No seets left';
		else
			update seat_class2 set ac3_total_seats=ac3_total_seats-1,ac3_booked_seats=ac3_booked_seats+1
			where(train_id = t_id and working_day=days);
		return ac3_price from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	elsif(categ='cc')then
		select cc_total_seats into che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=0)then
			raise notice'No seets left';
		else
			update seat_class2 set cc_total_seats=cc_total_seats-1,cc_booked_seats=cc_booked_seats+1
			where(train_id = t_id and working_day=days);
		return cc_price from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	elsif(categ='ec')then
		select ec_total_seats into che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=0)then
			raise notice'No seets left';
		else
			update seat_class2 set ec_total_seats=ec_total_seats-1,ec_booked_seats=ec_booked_seats+1
			where(train_id = t_id and working_day=days);
		return ec_price from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	elsif(categ='sl')then
		select sl_total_seats into che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=0)then
			raise notice'No seets left';
		else
			update seat_class2 set sl_total_seats=sl_total_seats-1,sl_booked_seats=sl_booked_seats+1
			where(train_id = t_id and working_day=days);
		return sl_price from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	else
		raise notice 'No such option';
		return 0;
	end if;
	return 0;
end;
$book_seat$
language plpgsql