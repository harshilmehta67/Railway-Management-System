create table train1(
    train_id int primary key,
    train_name varchar(20),
    starting_station_id int references station1(station_id),
    ending_station_id int references station1(station_id),
    starting_time float,  --in the form of HH.MM
    journey_time float , --denoting journey time in the form of HH.MM
)
begin
insert into train1 values(1000,'SaujantaExp' ,   100,   101,  13.00,  04.30);
insert into train1 values(1001,'SaujantaExp2',   100,   103,  16.00,  07.30);
insert into train1 values(1002,'SaujantaExp3',   103,   102,  18.00,  05.30);
insert into train1 values(1003,'mumtodelhi'  ,   104,   105,  10.00,  22.00);
insert into train1 values(1004,'mumtosrt'    ,   104,   103,  15.30,  10.00);
insert into train1 values(1005,'delhitorjk'  ,   105,   100,  9.30,   23.00);
end



create table tier1(
    tier_type int,
    train_id int references train1(train_id),
    total_seat int,
    PRIMARY KEY(tier_type,train_id)
)

create table station1(
    station_id int primary key,
    station_name varchar(20),
    platforms int
)
begin
insert into station1 values(100,'rjk',4);
insert into station1 values(101,'abd',12);
insert into station1 values(102,'brd',8);
insert into station1 values(103,'srt',9);
insert into station1 values(104,'mumbai',20);
insert into station1 values(105,'delhi',25);
end