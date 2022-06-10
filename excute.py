from scrap_no1 import *
from scrap_no2 import *
from scrap_no3 import *
from scrap_no4 import *
from scrap_no5 import *
from scrap_biz import *
#from scrap_digitalMedia import *
from scrap_history import *
from scrap_korean import *
from scrap_software import *
from scrap_security import *
scraping_no1()
scraping_no2()
scraping_no3()
scraping_no4()
scraping_no5()
scraping_biz()
#scraping_dm()
scraping_history()
scraping_korean()
scraping_security()
scraping_software()

#학과별 공지사항 업데이트 해야함.
# from fb_read import *
# import sqlite3
# conn=sqlite3.connect("myapp_recent_ann.db")
# cursor= conn.cursor()
# #c.execute("CREATE TABLE myapp_recent_ann(dept TEXT, title TEXT)")
# #test()
# cursor.execute(
#     f'UPDATE myapp_recent_ann SET title = ? WHERE dept = ?',
#     ('[SW교육혁신센터] 2022년 1학기 코딩 알고리즘 경진대회 개최 안내 (~06/08까지)','digitalmedia'
#     )
# )
# conn.commit()
# cursor.close()