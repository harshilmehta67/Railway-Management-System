import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "yashilpostgresql",
                                  host='localhost',
                                  port = "5432",
                                  database = "postgres")
    cursor = connection.cursor()
    
    #query = "select cancel_ticket(%s)"
    #pnr_no = 105
    #cursor.execute(query,(pnr_no,))
    #connection.commit()
    train_id = 10000
    cursor.execute("select * from deleted_tickes where train_id = %s and dayno = 1",(train_id,))
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
