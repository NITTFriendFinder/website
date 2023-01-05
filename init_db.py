import sqlite3
mydb = sqlite3.connect(database="database.db", check_same_thread=False)
mycursor = mydb.cursor()

# mycursor.execute("DROP TABLE question_paper")
mycursor.execute("CREATE TABLE IF NOT EXISTS question_paper(u_id INT, sem VARCAHR(2), dept VARCHAR(10), courseid VARCHAR(5), exam VARCHAR(10), year VARCHAR(4), prof VARCHAR(20), link VARCHAR(50))")
# u_id, sem, dept, courseid, exam, year, prof, link

mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("1", "3", "CSE", "MAIR31", "CT1", "2022", "jitraj", "https://drive.google.com/file/d/1_hg8BL9FpM924UCJpws_sUf-j46J0A48/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("2", "3", "CSE", "CSPE32", "CT1", "2022", "sitara", "https://drive.google.com/file/d/1_7XUj-HucGRv-j-2hyW0ZtFTJOoIUMZf/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("3", "3", "CSE", "CSPC33", "CT1", "2022", "", "https://drive.google.com/file/d/1ttEagKvyW5evtcaezON31QHq24UckXzy/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("4", "3", "CSE", "CSPC32", "CT1", "2022", "sai krishna", "https://drive.google.com/file/d/1hO5JU9CDU9Ujatn2IsqXNocVtS-hPYg3/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("5", "3", "CSE", "CSPC34", "CT1", "2022", "", "https://drive.google.com/file/d/1NckMlLJe2TBn-SKGwlS6LLVYu8fVkGk_/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("6", "3", "CSE", "CSPC31", "CT1", "2022", "bala krishna", "https://drive.google.com/file/d/108YTU5S-SIo55wWCsNPMIhEGmJMGzMR6/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("7", "3", "CSE", "CSPC34", "CT2", "2022", "", "https://drive.google.com/file/d/1rOqrjpExJvIxx3BgFldnupxjKPWtBsGF/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("8", "3", "CSE", "CSPC33", "CT2", "2022", "", "https://drive.google.com/file/d/1MXNx7KL_AdHvW0o95l4U5N0QhZaZu9FF/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("9", "3", "CSE", "CSPE32", "CT2", "2022", "sitara", "https://drive.google.com/file/d/16KEhFB8Js69BB6-wAcBteYkj5kpx4yio/view?usp=share_link")''')
mycursor.execute('''INSERT INTO question_paper(u_id, sem, dept, courseID, exam, year, prof, link) VALUES ("10", "3", "CSE", "CSPC31", "CT2", "2022", "bala krishna", "https://drive.google.com/file/d/1-SEWDK1269X1HCCISP4l1aunjcLi1ppj/view?usp=share_link")''')
mydb.commit()