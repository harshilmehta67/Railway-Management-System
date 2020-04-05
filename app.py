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
<<<<<<< HEAD
       #print(wel_come)
=======
       print(wel_come)
>>>>>>> aaf36fd4f86d07b5b0f4e63eba31db696152b61f
       
       if(wel_come["name"] == "admin"):
         admin_password = wel_come["password"]
         admin_name = wel_come["user_name"]
         if (admin_password == "admin123" and admin_name == "admin"):
            print("admin login success")
            return render_template('/admin.html')
         else:
               return render_template('/welcome.html')
       elif (wel_come["name"] == "user"):
<<<<<<< HEAD
         user_password = wel_come["password"]
         user_name = wel_come["user_name"]
         try:
           print("dfdfg")
           connection = psycopg2.connect(user = "postgres",password = "yashilpostgresql",host='localhost',port = "5432", database = "postgres")
           cursor = connection.cursor()
           query = "select user_id,name from user1"
           cursor.execute(query)
           user_records = cursor.fetchall()
           for i in user_records:
              if i[0] == int(user_password) and i[1] == user_name :
                  temp = 1
                  break
=======
         print("hi")
         try:
           connection = psycopg2.connect(user = "postgres",password = "yashilpostgresql",host='localhost',port = "5432", database = "postgres")
           cursor = connection.cursor()
           query = "select user_id,user_name from user1"
           cursor.execute(query)
           user_records = cursor.fetchall()
           print(user_records)
           #connection.commit()
           
>>>>>>> aaf36fd4f86d07b5b0f4e63eba31db696152b61f
         except (Exception, psycopg2.Error) as error :
           print ("Error while connecting to PostgreSQL", error)
         finally:
           if(connection):
              cursor.close()
              connection.close()
              print("PostgreSQL connection is closed")
<<<<<<< HEAD
         print(temp)
         if (temp==1):
               print("to pachi")
               return render_template('user_dashboard.html')
         else :
               return render_template('welcome.html')             
       else:
          #print("signup page error")
          return render_template('signup.html')

@app.route('/signup.html', methods=['POST','GET'])
def signup():
   if request.method == 'POST':
      user_signup      = request.form
      print(user_signup)
      user_id = user_signup.get("user_id")
      emailid = user_signup["email_id"]
      user_name = user_signup["name"]
      gender = user_signup["gender"]
      dob = user_signup["dob"]
      mobile_no = user_signup["mobile_no"]
      try:
          connection = psycopg2.connect(user = "postgres",password = "yashilpostgresql",host='localhost',port = "5432", database = "postgres")
          cursor = connection.cursor()
          cursor.callproc('check_user_id',[user_id,])
          dummy = cursor.fetchall()
          if (dummy == 0) :
            cursor.execute("insert into user1 values(%s,%s,%s,%s,%s,%s)", (user_id, emailid,user_name,gender,dob,mobile_no))
            connection.commit()
            print("success in insering new user values")
      except (Exception, psycopg2.Error) as error :
         print ("Error while connecting to PostgreSQL", error)
      finally:
         if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
         if dummy == 0 :
            return redirect(url_for('success',name = user_name))
         else :
            return render_template('signup.html')
   else:
      return render_template('signup.html')
=======
         return redirect(url_for('success',name = "user_name"))
       else:
          print("hi")
>>>>>>> aaf36fd4f86d07b5b0f4e63eba31db696152b61f


@app.route('/user_login')
def user_login():
    return render_template('/user_login.html')
# def user_login():
#    if request.method == 'POST':
#       user      = request.form
#       user_id = user.get("id_no")
#       user_name = user["name"]
#       try:
#           connection = psycopg2.connect(user = "postgres",password = "yashilpostgresql",host='localhost',port = "5432", database = "postgres")

#           cursor = connection.cursor()
#           cursor.execute("insert into student values(%s,%s)", (user_id, user_name))
#           connection.commit()
#           print("success")
#       except (Exception, psycopg2.Error) as error :
#          print ("Error while connecting to PostgreSQL", error)
#       finally:
#          if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")
#       return redirect(url_for('success',name = user_name))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user_name))


@app.route('/login-success/<name>')
def success(name):
    return 'welcome %s' % name


if __name__ == '__main__':
    app.run(debug=True)


# link for understanding connection with html form and flask https://pythonise.com/series/learning-flask/flask-working-with-forms
