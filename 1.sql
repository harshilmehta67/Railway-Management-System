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
-- create table seat_class1(
--   train_id int references train1(train_id),
--   sp int references train1(starting_station_id)
--   ep int references train1(ending_station_id),
--   price int ,
--   total_seats,
--   booked_seats,
--   class_category varchar(3),
--   PRIMARY KEY (train_id, sp, ep, class_category)
-- )
-- insert into seat_class1 values(10006, 104, 101, 101,  800,  50, 0, 'AC1')
-- insert into seat_class1 values(10006, 104, 101, 101,  500,  50, 0, 'AC2')
-- insert into seat_class1 values(10006, 104, 101, 101,    0,   0, 0, 'AC3')
-- insert into seat_class1 values(10006, 104, 101, 101,  200, 100, 0, 'CC')
-- insert into seat_class1 values(10006, 104, 101, 101,    0,   0, 0, 'EC')
-- insert into seat_class1 values(10006, 104, 101, 101,  340, 110, 0, 'SL')
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



--about ticket for user, user with ticket is passenger so he cna know his details thorugh this
-- keep status as confirm or reserved
create table  passenger1 (
  passenger_id int references user1(user_id),
  pnr SERIAL   primary key,
  first_name varchar(20) ,
  train_id int references train1(train_id),
  dayno int,
  seat_category varchar(3),
  status varchar(20)
)
--generate sequence of pnr from 100.....
CREATE SEQUENCE pnr_seq start 100000000 increment 1;
INSERT INTO passenger1 VALUES (1808,nextval('pnr_seq'),'Shilpa',10000,3,'AC1','confirm');

------------------------------------------------------------------------------------------------------
--procedure for schedule: input is from station id and to station id , date
--output is table
create or replace function dis_train2(s_stat int, e_stat int, tarik date)
returns table(
s_stat_name varchar(20),
e_stat_name varchar(20),
t_name varchar(20),
t_id int,
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
	if(tarik<current_date) then
		raise exception 'Date invalid';
	end if;
	select extract(dow from  tarik) into dayno;
	return query
	select distinct 
	(select station_name from station1 where station_id=s_stat),
	(select station_name from station1 where station_id=e_stat),
	train1.train_name,train1.train_id,train1.starting_time,train1.journey_time,
	seat_class2.ac1_price,seat_class2.ac1_total_seats-seat_class2.ac1_booked_seats,
	seat_class2.ac2_price,seat_class2.ac2_total_seats-seat_class2.ac2_booked_seats,
	seat_class2.ac3_price,seat_class2.ac3_total_seats-seat_class2.ac3_booked_seats,
	seat_class2.cc_price,seat_class2.cc_total_seats-seat_class2.cc_booked_seats,
	seat_class2.ec_price,seat_class2.ec_total_seats-seat_class2.ec_booked_seats,
	seat_class2.sl_price,seat_class2.sl_total_seats-seat_class2.sl_booked_seats
	from train1,seat_class2,station1
	where(train1.starting_station_id=s_stat and train1.ending_station_id=e_stat and train1.train_id=seat_class2.train_id 
		  and seat_class2.working_day=dayno);
end;
$dis_train2$ language plpgsql;
select dis_train2(100,101,'20-04-2020')


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
select book_seat(10000,1,'AC1')

create or replace function book_seat(t_id int, days int, categ varchar)
returns int as $book_seat$
declare
che int;
baki_che int;
begin
	if(categ='AC1') then
		select ac1_total_seats,ac1_booked_seats into che,baki_che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=baki_che)then
			raise notice'No seats left';
			return ac1_price from seat_class2 where(train_id = t_id and working_day=days) ;
		else
			update seat_class2 set ac1_booked_seats=ac1_booked_seats+1
			where(train_id = t_id and working_day=days);
			return ac1_price+100000 from seat_class2 where(train_id = t_id and working_day=days) ;
		end if;

	elsif(categ='AC2')then
		select ac2_total_seats,ac2_booked_seats into che,baki_che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=baki_che)then
			raise notice'No seats left';
			return ac2_price from seat_class2 where(train_id = t_id and working_day=days) ;
		else
			update seat_class2 set ac2_booked_seats=ac2_booked_seats+1
			where(train_id = t_id and working_day=days);
			return ac2_price+100000 from seat_class2 where(train_id = t_id and working_day=days);
		end if;

	elsif(categ='AC3')then
		select ac3_total_seats,ac3_booked_seats into che,baki_che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=baki_che)then
			raise notice'No seats left';
			return ac3_price from seat_class2 where(train_id = t_id and working_day=days) ;
		else
			update seat_class2 set ac3_booked_seats=ac3_booked_seats+1
			where(train_id = t_id and working_day=days);
			return ac3_price+1000000 from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	elsif(categ='CC')then
		select cc_total_seats,cc_booked_seats into che,baki_che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=baki_che)then
			raise notice'No seats left';
			return cc_price from seat_class2 where(train_id = t_id and working_day=days) ;
		else
			update seat_class2 set cc_booked_seats=cc_booked_seats+1
			where(train_id = t_id and working_day=days);
			return cc_price+100000 from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	elsif(categ='EC')then
		select ec_total_seats,ec1_booked_seats into che,baki_che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=baki_che)then
			raise notice'No seats left';
			return ec_price from seat_class2 where(train_id = t_id and working_day=days) ;
		else
			update seat_class2 set ec_booked_seats=ec_booked_seats+1
			where(train_id = t_id and working_day=days);
			return ec_price+100000 from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	elsif(categ='SL')then
		select sl_total_seats,sl_booked_seats into che,baki_che from seat_class2 where(train_id = t_id and working_day=days);
		if(che=baki_che)then
			raise notice'No seats left';
			return sl_price from seat_class2 where(train_id = t_id and working_day=days) ;
		else
			update seat_class2 set sl_booked_seats=sl_booked_seats+1
			where(train_id = t_id and working_day=days);
			return sl_price+100000 from seat_class2 where(train_id = t_id and working_day=days);
		end if;
	else
		raise notice 'No such option';
		return 0;
	end if;
end;
$book_seat$
language plpgsql

------total revenue generated for a particular train on a day--------------------------------------
create or replace function revenue(t_id int, dofweek int) returns int
as $revenue$
begin
return (seat_class2.ac1_price*seat_class2.ac1_booked_seats) +
(seat_class2.ac2_price*seat_class2.ac2_booked_seats) +
(seat_class2.ac3_price*seat_class2.ac3_booked_seats) +
(seat_class2.cc_price*seat_class2.cc_booked_seats) +
(seat_class2.ec_price*seat_class2.ec_booked_seats) +
(seat_class2.sl_price*seat_class2.sl_booked_seats)
from seat_class2 where train_id=t_id and working_day=dofweek;
end;
$revenue$
language plpgsql

select revenue(10001,2)



-----------------------------------train running between two dates---------------------------------------------------------------------
create or replace function train_btwn_date(f_date date, t_date date)
returns table(
t_id int,
t_name varchar(20),
s_station int,
e_station int,
day_int int
)
as $train_btwn_date$
declare
day1 int;
day2 int;
begin
select extract(dow from f_date) into day1;
select extract(dow from t_date) into day2;
if(day1<day2) then
return query select distinct train1.train_id,train1.train_name,train1.starting_station_id,
train1.ending_station_id,seat_class2.working_day from train1,seat_class2
where seat_class2.working_day >= day1 and seat_class2.working_day <= day2;
else
return query select distinct train1.train_id,train1.train_name,train1.starting_station_id,
train1.ending_station_id,seat_class2.working_day from train1,seat_class2
where seat_class2.working_day >= day2 and seat_class2.working_day <= 7 and
seat_class2.working_day >= 0 and seat_class2.working_day <= day1;
end if;
end;
$train_btwn_date$
language plpgsql
select train_btwn_date('11-04-2020','15-04-2020')


------------------------------------trains running between two stations----------------------------------------------
create or replace function train_btwn(stat1 varchar, stat2 varchar)
returns table(
t_id int,
t_name varchar(20),
on_mon char(1),
on_tue char(1),
on_wed char(1),
on_thr char(1),
on_fri char(1),
on_sat char(1),
on_sun char(1)
) as $train_btwn$
begin
return query select train_id,train_name,mon,tue,wed,thu,fri,sat,sun from train1
where(starting_station_id = (select station_id from station1 where station_name=stat1)
and ending_station_id = (select station_id from station1 where station_name=stat2));
end;
$train_btwn$
language plpgsql

select train_btwn('mumbai','delhi')


-----------------------------------------------------TRIGGERS--------------------------------------------------------
-------------------------------Trigger of cheking user input variables-----------------------------------------------
create or replace function check_user1_proc() returns trigger as
$check_user1_proc$
begin
	if(new.user_id <1000 or new.user_id>9999) then
		raise exception 'User ID invalid';
	end if;
	if(new.name is NULL) then
		raise exception 'Name not written';
	end if;
	if(new.gender <> 'F' and new.gender <> 'M') then
		raise exception 'No such Gender ';
	end if;
	if(new.mobile_no >999999 or new.mobile_no<100000) then
		raise exception 'Mobile number invalid';
	end if;
	return new;
end;
$check_user1_proc$
language plpgsql;

create trigger check_user1
before insert or update on user1
	for each row execute procedure check_user1_proc();

----------------------------------------Trigger of cheking train data input-----------------------------------------
create or replace function check_train1_proc() returns trigger as
$train_user1_proc$
begin
	if(new.train_name is NULL) then
		raise exception 'Train name not written';
	end if;
	if(new.starting_station_id = new.ending_station_id) then
		raise exception 'Train is having same starting station and ending station';
	end if;
	if(new.starting_time > 24 or new.starting_time < 0) then
		raise exception 'Starting time is invalid';
	end if;
	if(new.mon='N' and new.tue='N' and new.wed='N' and new.thu='N' and new.fri='N' and new.sat='N' and new.sun='N')then
		raise exception 'Train is not working on any day';
	end if;
	return new;
end;
$train_user1_proc$
language plpgsql;

create trigger check_train1
before insert or update on train1
	for each row execute procedure check_train1_proc();

insert into train1 values('107',null,101,101,25,2.5,'N','N','N','N','N','N','N');

