from flask import Flask, redirect, url_for, request,  render_template
import psycopg2
from flask import flash
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/welcome.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if request.method == 'POST':
       return render_template('welcome.html')

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
       wel_come = request.form

       if(wel_come["name"] == "admin"):
         admin_password  = wel_come["password"]
         admin_name      = wel_come["user_name"]
         if (admin_password == "admin123" and admin_name == "admin"):
            return render_template('admin_homepage.html')
         else:
               return render_template('welcome.html')

       elif (wel_come["name"] == "user"):
         user_password = wel_come["password"]
         user_name = wel_come["user_name"]
         query = "select user_id,name from user1"
         cursor.execute(query)
         user_records = cursor.fetchall()
         temp = 0
         for i in user_records:
            if i[0] == int(user_password) and i[1] == user_name :
                temp = 1
                break
         if (temp==1):
            cursor.execute("select station_name,station_id from station1 order by station_name")
            result = cursor.fetchall()
            return render_template('user_dashboard.html',name = user_name, user_id = user_password, value = result)
         else :
               return render_template('welcome.html')             
       else:
          return render_template('signup.html')

@app.route('/signup.html', methods=['POST','GET'])
def signup():
   if request.method == 'POST':
      user_signup      = request.form
      user_id = user_signup.get("user_id")
      emailid = user_signup["email_id"]
      user_name = user_signup["name"]
      gender = user_signup["gender"]
      dob = user_signup["dob"]
      mobile_no = user_signup["mobile_no"]
      try:
         query = "select check_user_id(%s);"
         user_id = str(user_id)
         cursor.execute(query,(user_id,))
         #connection.commit()
         dummy = cursor.fetchone()
         if ( dummy[0] == 0) :
           cursor.execute("insert into user1 values(%s,%s,%s,%s,%s,%s)", (user_id, emailid,user_name,gender,dob,mobile_no,))
           connection.commit()
           query = "update user1 set balance = 0 where user_id = %s"
           cursor.execute(query,(user_id,))
           connection.commit()
           if dummy[0] == 0 :
               cursor.execute("select * from station1 order by station_name")
               result = cursor.fetchall()
               return render_template('user_dashboard.html',name = user_name, user_id = user_id, value = result)
           else :
               return render_template('signup.html')
         else:
            return render_template('signup.html')
      except psycopg2.Error as e:
         print(e)
         print(user_id)
         print("failed")
         #flash('Looks like you have changed your name!')
         message = "invalid Credentials Please go Back to Main Page"
         return render_template('signup.html', message = message)



@app.route('/user_knowScedule_bookTicket',methods=['POST','GET'])
def user_knowSchedule_bookTicket():
   if request.method == 'POST':
      data = request.form
      sp    = data["sp"]
      ep    = data["ep"]
      tarik = data["tarik"]
      query = "select * from dis_train2(%s,%s,%s)"
      user_name = data["user_name"]
      user_id = data["user_id"]
      cursor.execute(query,(sp,ep,tarik))
      result = cursor.fetchall()
      query = "select balance from user1 where user_id=%s"
      cursor.execute(query,(user_id,))
      balance = cursor.fetchone()
      balance = int(balance[0])
      print(balance)
      return render_template('user_knowScheduleAndBookTicket.html', value = result, user_name = user_name, user_id = user_id, tarik = tarik, balance=balance)

@app.route('/user_bookTicket',methods=['POST','GET'])
def user_bookTicket():
   if request.method == 'POST' or 'GET':
      data = request.form
      user_id = data["user_id"]
      train_id = data["train_id"]
      tarik = data["tarik"]
      seat_category = data["seat_category"]

      query = "select extract(dow from  TIMESTAMP %s)"
      cursor.execute(query,(tarik,))
      result = cursor.fetchone()
      divas = int(result[0])

      query = "select starting_station_id,ending_station_id from train1 where train_id = %s"
      cursor.execute(query,(train_id,))
      result = cursor.fetchall()
      
      from_station_id = result[0][0]
      to_station_id = result[0][1]

      query = "select station_name from station1 where station_id = %s"
      cursor.execute(query,(from_station_id,))
      from_station_name = cursor.fetchone()
      from_station_name = from_station_name[0]

      query = "select station_name from station1 where station_id = %s"
      cursor.execute(query,(to_station_id,))
      to_station_name = cursor.fetchone()
      to_station_name = to_station_name[0]
      #convert this date to day in the variable divas
      #create a sql input(train_id,day,seat_category)
      #output is (train_id,from_station_name,to_station_name,date,ticket_fair,status,)
      
      query = "select name from user1 where user_id=%s"
      cursor.execute(query,(user_id,))
      user_name = cursor.fetchone()
      user_name = user_name[0]
      query = "select book_seat(%s,%s,%s)"
      cursor.execute(query,(train_id,divas,seat_category))
      ticket_fair = cursor.fetchone()
      ticket_fair = int(ticket_fair[0])
      query = "select balance from user1 where user_id=%s"
      cursor.execute(query,(user_id,))
      balance = cursor.fetchone()
      balance = int(balance[0])
      if ticket_fair > 100000 :
         if ticket_fair - 100000 > balance:
            return render_template('welcome.html')
         else:
            query = "insert into passenger1 values(nextval('pnr_seq'),%s,%s,%s,%s,'C')"
            cursor.execute(query,(user_id,train_id,divas,seat_category,))
            connection.commit()
            ticket_fair = ticket_fair - 100000
            query = "update user1 set balance = balance - %s where user_id = %s"
            cursor.execute(query,(ticket_fair,user_id,))
            connection.commit()
      else:
         if ticket_fair > balance:
            return render_template('welcome.html')
         else:
            query = "update user1 set balance = balance - %s where user_id = %s"
            cursor.execute(query,(ticket_fair,user_id,))
            connection.commit()
            query = "insert into passenger1 values(nextval('pnr_seq'),%s,%s,%s,%s,'W')"
            cursor.execute(query,(user_id,train_id,divas,seat_category,))
            connection.commit()


      query = "select pnr from passenger1 where passenger_id = %s"
      cursor.execute(query,(user_id,))
      passenger_pnrno = cursor.fetchone()
      passenger_pnrno = passenger_pnrno[0]

      query = "select status from passenger1 where passenger_id = %s"
      cursor.execute(query,(user_id,))
      status = cursor.fetchone()
      status = status[0]

      query = "select train_name from train1 where train_id = %s"
      cursor.execute(query,(train_id,))
      train_name = cursor.fetchone()
      train_name = train_name[0]

      if status == 'C':
         status = 'CONFIRMED'
      else:
         status = 'RESERVED'


      return render_template('user_eTicket.html',user_name = user_name, user_id = user_id, from_station_name = from_station_name, to_station_name = to_station_name, seat_category = seat_category, ticket_fair = ticket_fair, passenger_pnrno=passenger_pnrno, doj= tarik, status=status,train_id= train_id, train_name=train_name)
      
@app.route('/addmoney', methods=['POST','GET'])
def addmoney():
   if request.method == 'POST':
      data = request.form
      user_id = data["user_id"]
      balance = data["balance"]
      query = "update user1 set balance = balance + %s where user_id = %s"
      cursor.execute(query,(balance,user_id,))
      connection.commit()
      user_name= data["user_name"]
      cursor.execute("select * from station1 order by station_name")
      result = cursor.fetchall()
      return render_template('user_dashboard.html',name = user_name, user_id = user_id, value = result)

@app.route('/admin_amend_data', methods=['POST','GET'])
def admin_amend_data():
   if request.method == 'POST':
      return render_template('admin_amend_data.html')

@app.route('/add_train', methods=['POST', 'GET'])
def add_train():
    if request.method == 'POST':
        details = request.form
      #   print(details)
        train_id = details["train_id"]
        train_name = details["train_name"]
        sp = details["sp"]
        ep = details["ep"]
        st = details["st"]
        jt = details["jt"]
        d1 , d2 , d3 , d4 , d5 , d6 ,d7 = ['N']*7
        for keys in details.keys():
         if keys == 'mon':
            d1 = 'Y'
            #print("onf")
         if keys == 'tue':
            d2 = 'Y'
         if keys == 'wed':
            d3 = 'Y'
         if keys == 'thu':
            d4 = 'Y'
         if keys == 'fri':
            d5 = 'Y'
         if keys == 'sat':
            d6 = 'Y'
         if keys == 'sun':
            d7 = 'Y'
        cursor.execute("insert into train1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(train_id,train_name,sp,ep,st,jt,d1,d2,d3,d4,d5,d6,d7))
        connection.commit()
        return render_template('admin_amend_data.html')

@app.route('/delete_train', methods=['POST', 'GET'])
def delete_train():
    if request.method == 'POST':
        details = request.form
        #print(details)
        train_id = details["train_id"]
        print(train_id)
        cursor.execute("DELETE FROM train1 WHERE train1.train_id = %s",(train_id,))
        connection.commit()
        return render_template('admin_amend_data.html')


@app.route('/add_station', methods=['POST', 'GET'])
def add_station():
    if request.method == 'POST':
        details = request.form
        #print(details)
        #print(train_id)
        station_id = details["station_id"]
        station_name = details["station_name"]
        cursor.execute("insert into station1 values(%s,%s)",(station_id,station_name))
        connection.commit()
        return render_template('admin_amend_data.html')

@app.route('/delete_station', methods=['POST', 'GET'])
def delete_station():
    if request.method == 'POST':
        details = request.form
        print(details)
        station_id = details["station_id"]
        print(station_id)
        cursor.execute("DELETE FROM station1 WHERE station1.station_id = %s",(station_id,))
        connection.commit()
        return render_template('admin_amend_data.html')

@app.route('/cancelTicket1', methods=['POST','GET'])
def cancelTicket1():
   if request.method == 'POST':
      data = request.form
      print(data)
      pnr_no = data["pnr"]
      user_name= data["user_name"]
      user_id = data["user_id"]
      query = "select cancel_ticket(%s)"
      cursor.execute(query,(pnr_no,))
      connection.commit()
      cursor.execute("select * from station1 order by station_name")
      result = cursor.fetchall()
      return render_template('user_dashboard.html',name = user_name, user_id = user_id, value = result)


@app.route('/bookedTickets', methods=['POST', 'GET'])
def bookedTickets():
    if request.method == 'POST':
        data = request.form
        user_id = data["user_id"]
        query = "select * from show_tickets(%s)"
        cursor.execute(query,(user_id,))
        result = cursor.fetchall()
        return render_template('bookedTickets.html',value = result)

@app.route('/seat_category', methods=['POST', 'GET'])
def seat_category():
    if request.method == 'POST':
        data = request.form
        
        train_id = data["train_id"]

        ac1_p = data["seat_price_AC1"] 
        ac1_s = data["total_seat_AC1"]
        ac1_b = data["booked_seat_AC1"]

        ac2_p = data["seat_price_AC2"] 
        ac2_s = data["total_seat_AC2"]
        ac2_b = data["booked_seat_AC2"]

        ac3_p = data["seat_price_AC3"] 
        ac3_s = data["total_seat_AC3"]
        ac3_b = data["booked_seat_AC3"]


        cc_p = data["seat_price_CC"] 
        cc_s = data["total_seat_CC"]
        cc_b = data["booked_seat_CC"]

        ec_p = data["seat_price_EC"] 
        ec_s = data["total_seat_EC"]
        ec_b = data["booked_seat_EC"]
        
        sl_p = data["seat_price_SL"] 
        sl_s = data["total_seat_SL"]
        sl_b = data["booked_seat_SL"]

        query = "insert into seat_class2 values(%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s)"
        #insert into seat_class2 values(10000, 1, 800,50,0, 500,50,0, 0,0,0, 200,100,0, 340,110,0, 0,0,0)

        for keys in data.keys():
            if keys == 'mon':
               cursor.execute(query,(train_id,1, ac1_p,ac1_s,ac1_b, ac2_p,ac2_s,ac2_b, ac3_p,ac3_s,ac3_b, cc_p,cc_s,cc_b, ec_p,ec_s,ec_b, sl_p,sl_s,sl_b,))
               connection.commit()
            if keys == 'tue':
               cursor.execute(query,(train_id,2, ac1_p,ac1_s,ac1_b, ac2_p,ac2_s,ac2_b, ac3_p,ac3_s,ac3_b, cc_p,cc_s,cc_b, ec_p,ec_s,ec_b, sl_p,sl_s,sl_b,))
               connection.commit()
            if keys == 'wed':
               cursor.execute(query,(train_id,3, ac1_p,ac1_s,ac1_b, ac2_p,ac2_s,ac2_b, ac3_p,ac3_s,ac3_b, cc_p,cc_s,cc_b, ec_p,ec_s,ec_b, sl_p,sl_s,sl_b,))
               connection.commit()
            if keys == 'thu':
               cursor.execute(query,(train_id,4, ac1_p,ac1_s,ac1_b, ac2_p,ac2_s,ac2_b, ac3_p,ac3_s,ac3_b, cc_p,cc_s,cc_b, ec_p,ec_s,ec_b, sl_p,sl_s,sl_b,))
               connection.commit()
            if keys == 'fri':
               cursor.execute(query,(train_id,5, ac1_p,ac1_s,ac1_b, ac2_p,ac2_s,ac2_b, ac3_p,ac3_s,ac3_b, cc_p,cc_s,cc_b, ec_p,ec_s,ec_b, sl_p,sl_s,sl_b,))
               connection.commit()   
            if keys == 'sat':
               cursor.execute(query,(train_id,6, ac1_p,ac1_s,ac1_b, ac2_p,ac2_s,ac2_b, ac3_p,ac3_s,ac3_b, cc_p,cc_s,cc_b, ec_p,ec_s,ec_b, sl_p,sl_s,sl_b,))
               connection.commit()
            if keys == 'sun':
               cursor.execute(query,(train_id,7, ac1_p,ac1_s,ac1_b, ac2_p,ac2_s,ac2_b, ac3_p,ac3_s,ac3_b, cc_p,cc_s,cc_b, ec_p,ec_s,ec_b, sl_p,sl_s,sl_b,))
               connection.commit()

        return render_template('admin_amend_data.html')


@app.route('/deleteUser' , methods = ['POST','GET'])
def deleteUser(): 
   if request.method == 'POST':
      data = request.form
      user_id = data["user_id"]
      query = "delete from user1 where user_id=%s"
      cursor.execute(query,(user_id,))
      connection.commit()
      return render_template('admin_amend_data.html')


@app.route('/trainBetweenTwoStations' , methods = ['POST','GET'])
def trainBetweenTwoStations(): 
   if request.method == 'POST':
      data = request.form
      f_station = data["f_station"]
      t_station = data["t_station"]
      query = "select * from train_btwn(%s,%s)"
      cursor.execute(query,(f_station,t_station))
      result = cursor.fetchall()
      print(result)
      return render_template('trainBetweenTwoStation.html', value = result)

@app.route('/trainBetweenTwoDates', methods = ['POST','GET'])
def count_trainBetweenTwoDates():
   if request.method == 'POST':
      data = request.form
      f_date = data["f_date"]
      t_date = data["t_date"]
      query = "select * from train_btwn_date(%s,%s)"
      cursor.execute(query,(f_date,t_date))
      result = cursor.fetchall()
      return render_template('trainBetweenTwoDates.html', value = result)


@app.route('/revenue',methods=['POST','GET'])
def revenue():
   if request.method == 'POST':
      data = request.form
      print(data)
      train_id = data["train_id"]
      query = "select revenue(%s,%s)"
      total_revenue = 0
      for keys in data.keys():
         if keys == 'mon':
            cursor.execute(query,(train_id,1))
            result = cursor.fetchone()
            total_revenue = total_revenue + int(result[0])
         if keys == 'tue':
            cursor.execute(query,(train_id,2))
            result = cursor.fetchone()
            total_revenue = total_revenue + int(result[0])
         if keys == 'wed':
            cursor.execute(query,(train_id,3))
            result = cursor.fetchone()
            total_revenue = total_revenue + int(result[0])
         if keys == 'thu':
            cursor.execute(query,(train_id,4))
            result = cursor.fetchone()
            total_revenue = total_revenue + int(result[0])
         if keys == 'fri':
            cursor.execute(query,(train_id,5))
            result = cursor.fetchone()
            total_revenue = total_revenue + int(result[0])
         if keys == 'sat':
            cursor.execute(query,(train_id,6))
            result = cursor.fetchone()
            total_revenue = total_revenue + int(result[0])
         if keys == 'sun':
            cursor.execute(query,(train_id,7))
            result = cursor.fetchone()
            total_revenue = total_revenue + int(result[0])
      query = "select train_name from train1 where train_id = %s"
      cursor.execute(query,(train_id,))
      train_name = cursor.fetchone()[0]
      print(total_revenue)
      print(train_name)
      return render_template('revenue.html', train_id = train_id, train_name = train_name,rev = total_revenue)

@app.route('/knowDeletedTickets',methods=['POST','GET'])
def knowDeletedTickets():
   if request.method == 'POST':
      data = request.form
      print(data)
      train_id = data["train_id"]
      for keys in data.keys():
         if keys == 'mon':
            query = "select * from deleted_tickes where train_id = %s and dayno = 1"
         if keys == 'tue':
            query = "select * from deleted_tickes where train_id = %s and dayno = 2"
         if keys == 'wed':
            query = "select * from deleted_tickes where train_id = %s and dayno = 3"
         if keys == 'thu':
            query = "select * from deleted_tickes where train_id = %s and dayno = 4"
         if keys == 'fri':
            query = "select * from deleted_tickes where train_id = %s and dayno = 5"
         if keys == 'sat':
            query = "select * from deleted_tickes where train_id = %s and dayno = 6"
         if keys == 'sun':
            query = "select * from deleted_tickes where train_id = %s and dayno = 7"
         
      cursor.execute(query,(train_id,))
      result = cursor.fetchall()
      print(result)
      return render_template('deletedTickets.html', value = result)
            

@app.route('/<name> <user_id>')
def login_success(name,user_id):
    return 'welcome %s' % name


if __name__ == '__main__':
   connection = psycopg2.connect(user = "postgres",password = "yashilpostgresql",host='localhost',port = "5432", database = "postgres")
   cursor = connection.cursor()
   app.run(debug=True)


# link for understanding connection with html form and flask https://pythonise.com/series/learning-flask/flask-working-with-forms
