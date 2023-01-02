import os
import mysql.connector

mydb = mysql.connector.connect(
  host="sql6.freemysqlhosting.net",
  user="sql6587674",
  password="XgvFNgAXeW",
  database="sql6587674"

)

# exit()
mycursor = mydb.cursor()



# mycursor.execute("CREATE TABLE test (name VARCHAR(255), phone VARCHAR(255))")

# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SHOW TABLES")

# mycursor.execute("DROP TABLE test")
# mycursor.execute("CREATE TABLE test (course VARCHAR(255), link VARCHAR(255))")
sql = "INSERT INTO test (course, link) VALUES (%s, %s)"
val = ("Operating systems", "http://silver.nitt.edu/courseplan/CSE/2022-JAN/B.Tech/II-YEAR/CSPC43_OPERATING_SYSTEMS_B.pdf")
# mycursor.execute(sql, val)
mydb.commit()
mycursor.execute("SELECT * FROM test")
for x in mycursor.fetchall():
    print(x)