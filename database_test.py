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

mycursor.execute("DROP TABLE question_papers")
'''# mycursor.execute("CREATE TABLE test (course VARCHAR(255), link VARCHAR(255))")
sql = "INSERT INTO test (course, link) VALUES (%s, %s)"
val = ("Operating systems", "http://silver.nitt.edu/courseplan/CSE/2022-JAN/B.Tech/II-YEAR/CSPC43_OPERATING_SYSTEMS_B.pdf")
# mycursor.execute(sql, val)
mydb.commit()
mycursor.execute("SELECT * FROM test")
for x in mycursor.fetchall():
    print(x)'''



val = '''("1", "2022", "CSE", "MAIR31", "jitraj", "CT1", "https://drive.google.com/file/d/1_hg8BL9FpM924UCJpws_sUf-j46J0A48/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("2", "2022", "CSE", "CSPE32", "sitara", "CT1", "https://drive.google.com/file/d/1_7XUj-HucGRv-j-2hyW0ZtFTJOoIUMZf/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("3", "2022", "CSE", "CSPC33", "", "CT1", "https://drive.google.com/file/d/1ttEagKvyW5evtcaezON31QHq24UckXzy/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("4", "2022", "CSE", "CSPC32", "sai krishna", "CT1", "https://drive.google.com/file/d/1hO5JU9CDU9Ujatn2IsqXNocVtS-hPYg3/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("5", "2022", "CSE", "CSPC34", "", "CT1", "https://drive.google.com/file/d/1NckMlLJe2TBn-SKGwlS6LLVYu8fVkGk_/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("6", "2022", "CSE", "CSPC31", "bala krishna", "CT1", "https://drive.google.com/file/d/108YTU5S-SIo55wWCsNPMIhEGmJMGzMR6/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("7", "2022", "CSE", "CSPC34", "", "CT2", "https://drive.google.com/file/d/1rOqrjpExJvIxx3BgFldnupxjKPWtBsGF/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("8", "2022", "CSE", "CSPC33", "", "CT2", "https://drive.google.com/file/d/1MXNx7KL_AdHvW0o95l4U5N0QhZaZu9FF/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("9", "2022", "CSE", "CSPE32", "sitara", "CT2", "https://drive.google.com/file/d/16KEhFB8Js69BB6-wAcBteYkj5kpx4yio/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

val = '''("10", "2022", "CSE", "CSPC31", "bala krishna", "CT2", "https://drive.google.com/file/d/1-SEWDK1269X1HCCISP4l1aunjcLi1ppj/view?usp=share_link")'''
mycursor.execute("INSERT INTO question_paper(u_id, year, dept, prof, courseID, link) VALUES" + val)

mydb.commit()
mycursor.execute("SELECT * FROM test")
for x in mycursor.fetchall():
  print(x)