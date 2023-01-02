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

@app.route('/qp', methods=["GET", "POST"])
def prev_papers():
    if request.method == "GET":
        return render_template("qp_GET.html")
    if request.method == "POST":
        value = request.form.get('value')
        # return value
        mycursor.execute("SELECT * FROM test")
        # print(mycursor.fetchall())
        final = []
        for i in mycursor.fetchall():
            if value in i[0] or i[1]:
                final.append(i)
        for i in range(100-len(final)):
            final.append([])
        return render_template("qp_POST.html", link1=final[0][1], content1=final[0][0])



if __name__ == '__main__':
    app.run()