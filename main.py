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




# import mysql.connector
# mydb = mysql.connector.connect(
#   host="sql6.freemysqlhosting.net",
#   user="sql6587674",
#   password="XgvFNgAXeW",
#   database="sql6587674"

# )
import sqlite3
mydb = sqlite3.connect(database="ss.db", check_same_thread=False)
mycursor = mydb.cursor()

# mycursor.execute("DROP TABLE question_paper")
mycursor.execute("CREATE TABLE question_paper(u_id INT, year VARCHAR(4), dept VARCHAR(10), prof VARCHAR(20), courseID VARCHAR(5), exam VARCHAR(10), link VARCHAR(30))")


mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("1", "2022", "CSE", "MAIR31", "jitraj", "CT1", "https://drive.google.com/file/d/1_hg8BL9FpM924UCJpws_sUf-j46J0A48/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("2", "2022", "CSE", "CSPE32", "sitara", "CT1", "https://drive.google.com/file/d/1_7XUj-HucGRv-j-2hyW0ZtFTJOoIUMZf/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("3", "2022", "CSE", "CSPC33", "", "CT1", "https://drive.google.com/file/d/1ttEagKvyW5evtcaezON31QHq24UckXzy/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("4", "2022", "CSE", "CSPC32", "sai krishna", "CT1", "https://drive.google.com/file/d/1hO5JU9CDU9Ujatn2IsqXNocVtS-hPYg3/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("5", "2022", "CSE", "CSPC34", "", "CT1", "https://drive.google.com/file/d/1NckMlLJe2TBn-SKGwlS6LLVYu8fVkGk_/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("6", "2022", "CSE", "CSPC31", "bala krishna", "CT1", "https://drive.google.com/file/d/108YTU5S-SIo55wWCsNPMIhEGmJMGzMR6/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("7", "2022", "CSE", "CSPC34", "", "CT2", "https://drive.google.com/file/d/1rOqrjpExJvIxx3BgFldnupxjKPWtBsGF/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("8", "2022", "CSE", "CSPC33", "", "CT2", "https://drive.google.com/file/d/1MXNx7KL_AdHvW0o95l4U5N0QhZaZu9FF/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("9", "2022", "CSE", "CSPE32", "sitara", "CT2", "https://drive.google.com/file/d/16KEhFB8Js69BB6-wAcBteYkj5kpx4yio/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, year, dept, prof, courseID, exam, link) VALUES ("10", "2022", "CSE", "CSPC31", "bala krishna", "CT2", "https://drive.google.com/file/d/1-SEWDK1269X1HCCISP4l1aunjcLi1ppj/view?usp=share_link")''')
mydb.commit()





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
        mycursor.execute("SELECT * FROM question_paper")
        mydb.commit()
        final = list(mycursor.fetchall())
        # for i in mycursor.fetchall():
        #     if value in i[0] or i[1]:
        #         final.append(i)
        # for i in range(100-len(final)):
        #     final.append([])
        return render_template("qp_POST.html", link1=final[0][1], content1=final[0][0])



if __name__ == '__main__':
    app.run()