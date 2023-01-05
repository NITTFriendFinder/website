import pickle
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





#     # AWS Secrets
#     AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
#     AWS_KEY_ID = environ.get('AWS_KEY_ID')


@app.route('/')
def hello_world():
    return render_template('home_page.html')

@app.route('/qp', methods=["GET", "POST"])
def prev_papers():
    if request.method == "GET":
        # final = []
        mycursor.execute("SELECT DISTINCT courseid FROM question_paper")
        courseid = list(mycursor.fetchall())
        mycursor.execute("SELECT DISTINCT year FROM question_paper")
        year = list(mycursor.fetchall())
        mycursor.execute("SELECT DISTINCT prof FROM question_paper")
        prof = list(mycursor.fetchall())
        for i in range(len(courseid)):
            courseid[i] = courseid[i][0]
        for i in range(len(year)):
            year[i] = year[i][0]
        for i in range(len(prof)):
            prof[i] = prof[i][0]
        for i in range(100-len(courseid)):
            courseid.append("")
        for i in range(20-len(year)):
            year.append("")
        for i in range(20-len(prof)):
            prof.append("")
        return render_template("qp_GET.html", courseid1 = courseid[0] , courseid2 = courseid[1] , courseid3 = courseid[2] , courseid4 = courseid[3] , courseid5 = courseid[4] , courseid6 = courseid[5] , courseid7 = courseid[6] , courseid8 = courseid[7] , courseid9 = courseid[8] , courseid10 = courseid[9] , courseid11 = courseid[10] , courseid12 = courseid[11] , courseid13 = courseid[12] , courseid14 = courseid[13] , courseid15 = courseid[14] , courseid16 = courseid[15] , courseid17 = courseid[16] , courseid18 = courseid[17] , courseid19 = courseid[18] , courseid20 = courseid[19] , courseid21 = courseid[20] , courseid22 = courseid[21] , courseid23 = courseid[22] , courseid24 = courseid[23] , courseid25 = courseid[24] , courseid26 = courseid[25] , courseid27 = courseid[26] , courseid28 = courseid[27] , courseid29 = courseid[28] , courseid30 = courseid[29] , courseid31 = courseid[30] , courseid32 = courseid[31] , courseid33 = courseid[32] , courseid34 = courseid[33] , courseid35 = courseid[34] , courseid36 = courseid[35] , courseid37 = courseid[36] , courseid38 = courseid[37] , courseid39 = courseid[38] , courseid40 = courseid[39] , courseid41 = courseid[40] , courseid42 = courseid[41] , courseid43 = courseid[42] , courseid44 = courseid[43] , courseid45 = courseid[44] , courseid46 = courseid[45] , courseid47 = courseid[46] , courseid48 = courseid[47] , courseid49 = courseid[48] , courseid50 = courseid[49] , courseid51 = courseid[50] , courseid52 = courseid[51] , courseid53 = courseid[52] , courseid54 = courseid[53] , courseid55 = courseid[54] , courseid56 = courseid[55] , courseid57 = courseid[56] , courseid58 = courseid[57] , courseid59 = courseid[58] , courseid60 = courseid[59] , courseid61 = courseid[60] , courseid62 = courseid[61] , courseid63 = courseid[62] , courseid64 = courseid[63] , courseid65 = courseid[64] , courseid66 = courseid[65] , courseid67 = courseid[66] , courseid68 = courseid[67] , courseid69 = courseid[68] , courseid70 = courseid[69] , courseid71 = courseid[70] , courseid72 = courseid[71] , courseid73 = courseid[72] , courseid74 = courseid[73] , courseid75 = courseid[74] , courseid76 = courseid[75] , courseid77 = courseid[76] , courseid78 = courseid[77] , courseid79 = courseid[78] , courseid80 = courseid[79] , courseid81 = courseid[80] , courseid82 = courseid[81] , courseid83 = courseid[82] , courseid84 = courseid[83] , courseid85 = courseid[84] , courseid86 = courseid[85] , courseid87 = courseid[86] , courseid88 = courseid[87] , courseid89 = courseid[88] , courseid90 = courseid[89] , courseid91 = courseid[90] , courseid92 = courseid[91] , courseid93 = courseid[92] , courseid94 = courseid[93] , courseid95 = courseid[94] , courseid96 = courseid[95] , courseid97 = courseid[96] , courseid98 = courseid[97] , courseid99 = courseid[98] , courseid100 = courseid[99], year1 = year[0], year2 = year[1], year3 = year[2], year4 = year[3], year5 = year[4], year6 = year[5], year7 = year[6], year8 = year[7], year9 = year[8], year10 = year[9], year11 = year[10], year12 = year[11], year13 = year[12], year14 = year[13], year15 = year[14], year16 = year[15], year17 = year[16], year18 = year[17], year19 = year[18], year20 = year[19], prof1 = prof[0], prof2 = prof[1], prof3 = prof[2], prof4 = prof[3], prof5 = prof[4], prof6 = prof[5], prof7 = prof[6], prof8 = prof[7], prof9 = prof[8], prof10 = prof[9], prof11 = prof[10], prof12 = prof[11], prof13 = prof[12], prof14 = prof[13], prof15 = prof[14], prof16 = prof[15], prof17 = prof[16], prof18 = prof[17], prof19 = prof[18], prof20 = prof[19])
    if request.method == "POST":
        sem = request.form.get('sem')
        dept = request.form.get('dept')
        courseid = request.form.get('courseid')
        exam = request.form.get('exam')
        year = request.form.get('year')
        prof = request.form.get('prof')

        final = list(mycursor.execute("SELECT * FROM question_paper"))
        # u_id, sem, dept, courseid, exam, year, prof, link
        '''
        for i in final:
            if sem!="blank" and sem != i[1]:
                final.remove(i)
            if dept!="blank" and dept != i[2]:
                final.remove(i)
            if courseid!="blank" and courseid != i[3]:
                final.remove(i)
            if exam!="blank" and exam != i[4]:
                final.remove(i)
            if year!="blank" and year != i[5]:
                final.remove(i)
            if prof!="blank" and prof not in i[6]:
                final.remove(i)
        '''

        f = open("before_value.bin", "wb")
        pickle.dump(final, f)
        f.close()
        for i in range(100-len(final)):
            final.append(["", "", "", "", "", "", ""])
        f = open("after_value.bin", "wb")
        pickle.dump(final, f)
        f.close()
        return render_template("qp_POST.html", link1=final[0][7], content1 = final[0][0], link2=final[1][7], content2 = final[1][0], link3=final[2][6], content3 = final[2][0], link4=final[3][6], content4 = final[3][0], link5=final[4][6], content5 = final[4][0], link6=final[5][6], content6 = final[5][0], link7=final[6][6], content7 = final[6][0], link8=final[7][6], content8 = final[7][0], link9=final[8][6], content9 = final[8][0], link10=final[9][6], content10 = final[9][0], link11=final[10][6], content11 = final[10][0], link12=final[11][6], content12 = final[11][0], link13=final[12][6], content13 = final[12][0], link14=final[13][6], content14 = final[13][0], link15=final[14][6], content15 = final[14][0], link16=final[15][6], content16 = final[15][0], link17=final[16][6], content17 = final[16][0], link18=final[17][6], content18 = final[17][0], link19=final[18][6], content19 = final[18][0], link20=final[19][6], content20 = final[19][0], link21=final[20][6], content21 = final[20][0], link22=final[21][6], content22 = final[21][0], link23=final[22][6], content23 = final[22][0], link24=final[23][6], content24 = final[23][0], link25=final[24][6], content25 = final[24][0], link26=final[25][6], content26 = final[25][0], link27=final[26][6], content27 = final[26][0], link28=final[27][6], content28 = final[27][0], link29=final[28][6], content29 = final[28][0], link30=final[29][6], content30 = final[29][0], link31=final[30][6], content31 = final[30][0], link32=final[31][6], content32 = final[31][0], link33=final[32][6], content33 = final[32][0], link34=final[33][6], content34 = final[33][0], link35=final[34][6], content35 = final[34][0], link36=final[35][6], content36 = final[35][0], link37=final[36][6], content37 = final[36][0], link38=final[37][6], content38 = final[37][0], link39=final[38][6], content39 = final[38][0], link40=final[39][6], content40 = final[39][0], link41=final[40][6], content41 = final[40][0], link42=final[41][6], content42 = final[41][0], link43=final[42][6], content43 = final[42][0], link44=final[43][6], content44 = final[43][0], link45=final[44][6], content45 = final[44][0], link46=final[45][6], content46 = final[45][0], link47=final[46][6], content47 = final[46][0], link48=final[47][6], content48 = final[47][0], link49=final[48][6], content49 = final[48][0], link50=final[49][6], content50 = final[49][0], link51=final[50][6], content51 = final[50][0], link52=final[51][6], content52 = final[51][0], link53=final[52][6], content53 = final[52][0], link54=final[53][6], content54 = final[53][0], link55=final[54][6], content55 = final[54][0], link56=final[55][6], content56 = final[55][0], link57=final[56][6], content57 = final[56][0], link58=final[57][6], content58 = final[57][0], link59=final[58][6], content59 = final[58][0], link60=final[59][6], content60 = final[59][0], link61=final[60][6], content61 = final[60][0], link62=final[61][6], content62 = final[61][0], link63=final[62][6], content63 = final[62][0], link64=final[63][6], content64 = final[63][0], link65=final[64][6], content65 = final[64][0], link66=final[65][6], content66 = final[65][0], link67=final[66][6], content67 = final[66][0], link68=final[67][6], content68 = final[67][0], link69=final[68][6], content69 = final[68][0], link70=final[69][6], content70 = final[69][0], link71=final[70][6], content71 = final[70][0], link72=final[71][6], content72 = final[71][0], link73=final[72][6], content73 = final[72][0], link74=final[73][6], content74 = final[73][0], link75=final[74][6], content75 = final[74][0], link76=final[75][6], content76 = final[75][0], link77=final[76][6], content77 = final[76][0], link78=final[77][6], content78 = final[77][0], link79=final[78][6], content79 = final[78][0], link80=final[79][6], content80 = final[79][0], link81=final[80][6], content81 = final[80][0], link82=final[81][6], content82 = final[81][0], link83=final[82][6], content83 = final[82][0], link84=final[83][6], content84 = final[83][0], link85=final[84][6], content85 = final[84][0], link86=final[85][6], content86 = final[85][0], link87=final[86][6], content87 = final[86][0], link88=final[87][6], content88 = final[87][0], link89=final[88][6], content89 = final[88][0], link90=final[89][6], content90 = final[89][0], link91=final[90][6], content91 = final[90][0], link92=final[91][6], content92 = final[91][0], link93=final[92][6], content93 = final[92][0], link94=final[93][6], content94 = final[93][0], link95=final[94][6], content95 = final[94][0], link96=final[95][6], content96 = final[95][0], link97=final[96][6], content97 = final[96][0], link98=final[97][6], content98 = final[97][0], link99=final[98][6], content99 = final[98][0], link100=final[99][6], content100 = final[99][0])



if __name__ == '__main__':
    app.run()