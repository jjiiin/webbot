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

import schedule
import time
def keyword_scraping():
    try:
        #scraping_no2()
        # scraping_korean()
        scraping_security()      
        # scraping_no3()
        # scraping_no4()
        # scraping_no5()
        # scraping_biz()
        # #scraping_dm()
        # scraping_history()
        # scraping_software()
        #scraping_no1()
    except Exception as ex:
        print('에러가 발생했습니다.',ex)



schedule.every(1).seconds.do(keyword_scraping)
while True:
    schedule.run_pending()
    now = time.localtime()
    print("******************************************")
    print("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    print("******************************************")
    time.sleep(1)

# #학과별 공지사항 업데이트 해야함.
# from fb_read import *
# import sqlite3
# conn=sqlite3.connect("myapp_recent_ann.db")
# cursor= conn.cursor()
# #c.execute("CREATE TABLE myapp_recent_ann(dept TEXT, title TEXT)")
# #test()
# cursor.execute(
#     f'UPDATE myapp_recent_ann SET title = ? WHERE dept = ?',
#     ('[정보보호특성화사업단]2022기업현장실습참여기업안내','security'
#     )
# )
# conn.commit()
# cursor.close()