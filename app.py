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
       print(wel_come)
       
       if(wel_come["name"] == "admin"):
         admin_password = wel_come["password"]
         admin_name = wel_come["user_name"]
         if (admin_password == "admin123" and admin_name == "admin"):
            print("admin login success")
            return render_template('/admin.html')
         else:
               return render_template('/welcome.html')
       elif (wel_come["name"] == "user"):
         print("hi")
         try:
           connection = psycopg2.connect(user = "postgres",password = "yashilpostgresql",host='localhost',port = "5432", database = "postgres")
           cursor = connection.cursor()
           query = "select user_id,user_name from user1"
           cursor.execute(query)
           user_records = cursor.fetchall()
           print(user_records)
           #connection.commit()
           
         except (Exception, psycopg2.Error) as error :
           print ("Error while connecting to PostgreSQL", error)
         finally:
           if(connection):
              cursor.close()
              connection.close()
              print("PostgreSQL connection is closed")
         return redirect(url_for('success',name = "user_name"))
       else:
          print("hi")


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
