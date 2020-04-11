import psycopg2

# try:
#     connection = psycopg2.connect(user = "postgres",
#                                   password = "yashilpostgresql",
#                                   host='localhost',
#                                   port = "5432",
#                                   database = "postgres")
#     cursor = connection.cursor()
#     user_id=1103
#     user_name='p'
#     emailid = 'e'
#     gender = 'F'
#     dob = '12-12-2009'
#     mobile_no = 108349
#     cursor.execute("insert into user1 values(%s,%s,%s,%s,%s,%s)", (user_id, emailid,user_name,gender,dob,mobile_no))
#     #connection.commit()
#     print("success  Fecthing Values")

# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)

# finally:
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
#link where i got this from :https://pynative.com/python-postgresql-tutorial/
#query for day from date select extract(dow from date '08-12-2019');
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
trian_id = "10010"
station_id = 111
#cursor.execute("DELETE FROM station1 WHERE station1.station_id = %s",(station_id,))
#cursor.execute("DELETE FROM train1 WHERE train1.train_id = 10010")
#connection.commit()
sp    = 100
ep    = 101


#connection.commit()
query = "select train_btwn_date(%s,%s)"
f_date = '11-04-2020'
t_date = '13-04-2020'
cursor.execute(query,(f_date,t_date))
train_name = cursor.fetchall()


user_id = 1100
query = "select name from user1 where user_id=%s"
cursor.execute(query,(user_id,))
user_name = cursor.fetchone()
print(user_name)
user_name = user_name[0]

train_id = 10000
divas = 1
seat_category = 'AC1'

query = "select book_seat(%s,%s,%s)"
cursor.execute(query,(train_id,divas,seat_category))
ticketFair = cursor.fetchone()
if int(ticketFair[0]) > 100000 :
   query = "insert into passenger1 values(%s,nextval('pnr_seq'),%s,%s,%s,%s,'confirm')"
   cursor.execute(query,(user_id,user_name,train_id,divas,seat_category,))
   connection.commit()
else:
   query = "insert into passenger1 values(%s,nextval('pnr_seq'),%s,%s,%s,%s,'reserved')"
   cursor.execute(query,(user_id,user_name,train_id,divas,seat_category,))
   connection.commit()