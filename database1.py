import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "yashilpostgresql",
                                  host='localhost',
                                  port = "5432",
                                  database = "postgres")

    cursor = connection.cursor()
<<<<<<< HEAD
    #query1 = "create table user1(user_id int primary key,email_id varchar(30),name varchar(50),gender char(1),dob date,mobile_no int)"
    #query2 = "insert into user1 values(1000,'abc@gmail.com','ram','M','01-01-2000',98987672)"
    #query = "insert into student values(%s,%s)"
    #var = id,name
    #cursor.execute(query,var)
    #query3 = "select user_id,name from user1"
    #cursor.execute(query3)
    #connection.commit()
    #print("success  Fecthing Values")
    #result = cursor.fetchall()
    # for i in result:
    #     print(i[0])
    #     print(i[1])
    connection = psycopg2.connect(user = "postgres",
                                  password = "yashilpostgresql",
                                  host='localhost',
                                  port = "5432",
                                  database = "postgres")
    cursor = connection.cursor()
    cursor.callproc('dis_train',[104,101,'05-04-2020',])

    # query3 = "select * from user1"
    # cursor.execute(query3)
    # connection.commit()

    print("success  Fecthing Values")
    result = cursor.fetchall()
    for i in result:
       print(i)
    
=======
    query1 = "create table user1(user_id int primary key,email_id varchar(30),name varchar(50),gender char(1),dob date,mobile_no int)"
    query2 = "insert into user1 values(1000,'abc@gmail.com','ram','M','01-01-2000',98987672)"
    #query = "insert into student values(%s,%s)"
    #var = id,name
    #cursor.execute(query,var)
    
    cursor.execute(query2)
    connection.commit()
    print("success  Fecthing Values")
    # result = cursor.fetchall()
    # for i in result:
    #     print(i)

>>>>>>> aaf36fd4f86d07b5b0f4e63eba31db696152b61f
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
<<<<<<< HEAD
#link where i got this from :https://pynative.com/python-postgresql-tutorial/
#query for day from date select extract(dow from date '08-12-2019');
=======
#link where i got this from :https://pynative.com/python-postgresql-tutorial/
>>>>>>> aaf36fd4f86d07b5b0f4e63eba31db696152b61f