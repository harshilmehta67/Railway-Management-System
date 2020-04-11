import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "yashilpostgresql",
                                  host='localhost',
                                  port = "5432",
                                  database = "postgres")
    cursor = connection.cursor()
    query1 = "insert into passenger1 values (nextval('pnr_seq'),1000,10000,1,'CC','C')"
    
    #query = "select cancel_ticket(%s)"
    #pnr_no = 105
    #cursor.execute(query,(pnr_no,))
    #connection.commit()
    cursor.execute("select * from passenger1")
    result = cursor.fetchall()

    print(result)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

#link where i got this from :https://pynative.com/python-postgresql-tutorial/
