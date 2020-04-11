import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "yashilpostgresql",
                                  host='localhost',
                                  port = "5432",
                                  database = "postgres")
    cursor = connection.cursor()
    user_id=1103
    user_name='p'
    emailid = 'e'
    gender = 'F'
    dob = '12-12-2009'
    mobile_no = 108349
    #cursor.execute("insert into user1 values(%s,%s,%s,%s,%s,%s)", (user_id, emailid,user_name,gender,dob,mobile_no))
    #connection.commit()
    #this function inserts values into table user1
    print("success  Fecthing Values")

    query = "select * from train_btwn_date(%s,%s)"
    #this is my inbuit fuction which takes two input date as paramter and gives output as a tables  
    #the function given below
    f_date = '11-04-2020'
    t_date = '13-04-2020'
    cursor.execute(query,(f_date,t_date))
    train_name = cursor.fetchall()
    for i in train_name:
       print(train_name)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

#link where i got this from :https://pynative.com/python-postgresql-tutorial/

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