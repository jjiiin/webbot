import sqlite3



def titleGetDB(dept_):
    con=sqlite3.connect('myapp_recent_ann.db',isolation_level=None)
    cur=con.cursor()
    dept=(dept_,)
    cur.execute("SELECT title FROM myapp_recent_ann WHERE dept=?",(dept))
    con.commit()
    result=cur.fetchone()
    # cur.close()
    # con.close()
    return result

def updateDB(title, dept):
    con=sqlite3.connect('myapp_recent_ann.db',isolation_level=None)
    cur=con.cursor()
    cur.execute("UPDATE myapp_recent_ann SET title = ? WHERE dept = ?",(title,dept))
    con.commit()
    # cur.close()
    # con.close()

# def insertDB(title,content,link,dept):
#     con=sqlite3.connect('./db.sqlite3')
#     cur=con.cursor()
#     query="INSERT INTO myapp_recent_ann(dept, title, content, link) VALUES(?,?,?,?)"
#     cur.execute(query,(dept,title,content,link))
#     con.commit()
#     cur.close()
#     con.close()