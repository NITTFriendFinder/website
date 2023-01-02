import os
from wsgiref.simple_server import make_server
from flask import Flask, render_template, request
# from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.update(
    TESTING=True,
    DEBUG= True,
    # FLASK_ENV='DEV'
    SERVER_NAME="localhost:5000"
    # SECRET_KEY='GDtfDCFYjD',
)




import mysql.connector
mydb = mysql.connector.connect(
  host="sql6.freemysqlhosting.net",
  user="sql6587674",
  password="XgvFNgAXeW",
  database="sql6587674"

)
mycursor = mydb.cursor()





#     # AWS Secrets
#     AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
#     AWS_KEY_ID = environ.get('AWS_KEY_ID')


@app.route('/')
def hello_world():
    return render_template('home_page.html')

@app.route('/QP', methods=["GET", "POST"])
def prev_papers():
    if request.method == "GET":
        return render_template("qp_GET.html")
    if request.method == "POST":
        value = str(request.form.get('value'))
        return value

if __name__ == '__main__':
    app.run()