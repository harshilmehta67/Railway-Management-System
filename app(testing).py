from flask import Flask, redirect, url_for, request,  render_template
import psycopg2
app(testing) = Flask(__name__)

@app.route('/')
def test_route():
    user_details = {
        'name': 'John',
        'email': 'john@doe.com'
    }
    return render_template('test.html', user=user_details)