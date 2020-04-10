from flask import Flask, redirect, url_for, request,  render_template
import psycopg2
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/welcome.html')


@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
       wel_come = request.form

       if(wel_come["name"] == "admin"):
         admin_password  = wel_come["password"]
         admin_name      = wel_come["user_name"]
         if (admin_password == "admin123" and admin_name == "admin"):
            print("admin login success")
            return render_template('/admin.html')
         else:
               return render_template('/welcome.html')

       elif (wel_come["name"] == "user"):
         user_password = wel_come["password"]
         user_name = wel_come["user_name"]
         query = "select user_id,name from user1"
         cursor.execute(query)
         user_records = cursor.fetchall()
         for i in user_records:
            if i[0] == int(user_password) and i[1] == user_name :
                temp = 1
                break
         if (temp==1):
            cursor.execute("select station_name,station_id from station1 order by station_name")
            result = cursor.fetchall()
            print(result)
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
      
      query = "select check_user_id(%s);"
      user_id = str(user_id)
      cursor.execute(query,(user_id,))
      #connection.commit()
      dummy = cursor.fetchone()
      if ( dummy[0] == 0) :
        cursor.execute("insert into user1 values(%s,%s,%s,%s,%s,%s)", (user_id, emailid,user_name,gender,dob,mobile_no,))
        connection.commit()
        if dummy[0] == 0 :
            cursor.execute("select * from station1 order by station_name")
            result = cursor.fetchall()
            return render_template('user_dashboard.html',name = user_name, user_id = user_id, value = result)
        else :
            return render_template('signup.html')
      else:
         return render_template('signup.html')


@app.route('/user_knowScedule_bookTicek',methods=['POST','GET'])
def user_knowSchedule_bookTicket():
   if request.method == 'POST':
      data = request.form
      print(data)
      sp    = data["sp"]
      ep    = data["ep"]
      tarik = data["tarik"]
      query = "select * from dis_train2(%s,%s,%s)"
      user_name = data["user_name"]
      user_id = data["user_id"]
      cursor.execute(query,(sp,ep,tarik))
      result = cursor.fetchall()
      
      return render_template('user_knowScheduleAndBookTicket.html', value = result, user_name = user_name, user_id = user_id, tarik = tarik)

@app.route('/user_knowScedule_bookTicek',methods=['POST','GET'])
def user_bookTicket():
   if request.method == 'POST':
      data = request.form
      print(data)
      user_id = data["user_id"]
      train_id = data["train_id"]
      tarik = data["tarik"]
      seat_category = data["seat_category"]
      query = "select extract(dow from  TIMESTAMP %s)"
      cursor.execute(query,(tarik,))
      result = cursor.fetchone()
      print(int(result[0]))
      divas = int(result[0])

      query = "select starting_station_id,ending_station_id from train1 where train_id = %s"
      cursor.execute(query,(train_id,))
      result = cursor.fetchall()
      
      from_station_id = result[0][0]
      to_station_id = result[0][1]

      query = "select station_name from station1 where station_id = %s"
      cursor.execute(query,(from_station_id,))
      from_station_name = cursor.fetchone()
      print(from_station_name)

      query = "select station_name from station1 where station_id = %s"
      cursor.execute(query,(to_station_id,))
      to_station_name = cursor.fetchone()
      print(to_station_name)
      #convert this date to day in the variable divas
      #create a sql input(train_id,day,seat_category)
      #output is (train_id,from_station_name,to_station_name,date,ticket_fair,status,)
      query = "select book_seat(%s,%s,%s)"
      cursor.execute(query,(train_id,divas,seat_category))
      connection.commit()
      ticketFair = cursor.fetchone()

     # return render_template('user_eTicket.html', status,fair_paid, user_id,train_id,from_station,to_station,tarik,pnr_status,seat_category,ticket_fair = ticket_fair)

@app.route('/trainBetweenTwoStations' , methods = ['POST','GET'])
def trainBetweenTwoStations(): 
   if request.method == 'POST':
      data = request.form
      f_station = data["f_station"]
      t_station = data["t_station"]
      query = "select * from train_btwn(%s,%s)"
      cursor.execute(query,(f_station,t_station))
      result = cursor.fetchall()
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
            total_revenue = total_revenue + result[0]
         if keys == 'tue':
            cursor.execute(query,(train_id,2))
            result = cursor.fetchone()
            total_revenue = total_revenue + result[0]
         if keys == 'wed':
            cursor.execute(query,(train_id,3))
            result = cursor.fetchone()
            total_revenue = total_revenue + result[0]
         if keys == 'thu':
            cursor.execute(query,(train_id,4))
            result = cursor.fetchone()
            total_revenue = total_revenue + result[0]
         if keys == 'fri':
            cursor.execute(query,(train_id,5))
            result = cursor.fetchone()
            total_revenue = total_revenue + result[0]
         if keys == 'sat':
            cursor.execute(query,(train_id,6))
            result = cursor.fetchone()
            total_revenue = total_revenue + result[0]
         if keys == 'sun':
            cursor.execute(query,(train_id,7))
            result = cursor.fetchone()
            total_revenue = total_revenue + result[0]
      query = "select train_name from train1 where train_id = %s"
      cursor.execute(query,(train_id,))
      train_name = cursor.fetchone()[0]
      print(total_revenue)
      print(train_name)
      return render_template('revenue.html', train_id = train_id, train_name = train_name,rev = total_revenue)


@app.route('/<name> <user_id>')
def login_success(name,user_id):
    return 'welcome %s' % name


if __name__ == '__main__':
   connection = psycopg2.connect(user = "postgres",password = "yashilpostgresql",host='localhost',port = "5432", database = "postgres")
   cursor = connection.cursor()
   app.run(debug=True)


# link for understanding connection with html form and flask https://pythonise.com/series/learning-flask/flask-working-with-forms
