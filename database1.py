import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "yashilpostgresql",
                                  host='localhost',
                                  port = "5432",
                                  database = "postgres")

    cursor = connection.cursor()
    query1 = "create table user1(user_id int primary key,email_id varchar(30),name varchar(50),gender char(1),dob date,mobile_no int)"
    query2 = "insert into user1 values(1000,'abc@gmail.com','ram','M','01-01-2000',98987672)"
    #query = "insert into student values(%s,%s)"
    #var = id,name
    #cursor.execute(query,var)
    query3 = "select user_id,name from user1"
    cursor.execute(query3)
    connection.commit()
    print("success  Fecthing Values")
    result = cursor.fetchall()
    for i in result:
        print(i[0])
        print(i[1])
    connection = psycopg2.connect(user = "postgres",
                                  password = "yashilpostgresql",
                                  host='localhost',
                                  port = "5432",
                                  database = "postgres")
    query3 = "select * from user1"
    cursor.execute(query3)
    connection.commit()
    print("success  Fecthing Values")
    result = cursor.fetchall()
    for i in result:
       print(i)
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
#link where i got this from :https://pynative.com/python-postgresql-tutorial/
#query for day from date select extract(dow from date '08-12-2019');