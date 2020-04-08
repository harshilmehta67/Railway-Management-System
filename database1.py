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
tarik = '08-04-2020'
query = "select dis_train2(%s,%s,%s)"
cursor.execute(query,(sp,ep,tarik))

#cursor.execute("insert into user1 values(%s,%s,%s,%s,%s,%s)", (user_id, emailid,user_name,gender,dob,mobile_no))
#connection.commit()
result = cursor.fetchall()
print(result)
print("success  Fecthing Values")