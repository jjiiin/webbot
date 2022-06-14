import requests
from bs4 import BeautifulSoup
from fb_read import*
from push_fcm_notification import *
from db_crud import*

#장학
dept='main_2'
dept_kr='장학'
def scraping_no2():
    url="https://www.swu.ac.kr//front/boardlist.do?bbsConfigFK=5&currentPage=$1"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Accept-Language":"ko-KR,ko"}
    res=requests.get(url,headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'html.parser',from_encoding="utf-8")
    tbody=soup.find("tbody")
    announcements=tbody.find_all("tr")
    title_before=titleGetDB(dept)[0]
    # title_before=""
    cnt=0
    count=0
    title_update=""
    for index, value in enumerate(announcements):
        temp=value.find_all("td")
        temp_index=str(temp[0].text).replace("\n","")
        #print(temp_index)
        if count == 1:
            print("count")
            title_before=titleGetDB(dept)[0]
        if temp_index not in "TOP":
            title=str(temp[1].text).replace("\n","").replace("새글","")
            #sqlite에 저장된 공지(제목)과 크롤링해온 제목 비교하기
            print("title_before "+title_before)
            print("title "+title)
            if(title_before!=title):
                cnt+=1
                if title_before in title:
                    print("제목 변경"+title)
                    updateDB(title,dept)
                    count+=1
                    break
                find_link=temp[1].a.attrs["onclick"].split("'")
                frag_link=str(find_link[3])
                link="http://www.swu.ac.kr/front/boardview.do?&pkid=" + frag_link +"&currentPage=1&menuGubun=1&siteGubun=1&bbsConfigFK=4&searchField=ALL&searchValue=&searchLowItem=ALL"
                contents_tmp=contentExtraction(link)
                #키워드 리스트랑 비교해서 푸쉬알림 보내기
                content=title+contents_tmp
                pushNotification(content,link,dept_kr,0)
                if(cnt==1):
                    title_update=title
                    # if title_before=="":
                    #     insertDB(title_update,content,link)
                    #     break
                #fb-keyword목록과 비교하기
            else: 
                #공지사항이 update됐을 때만 sqlite 수정하기.
                if cnt!=0:
                    print("title_update"+title_update)
                    updateDB(title_update,dept)
                    count+=1
                break
    else:
        updateDB(title_update,dept)

def contentExtraction(link):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Accept-Language":"ko-KR,ko"}
    res=requests.get(link,headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'html.parser',from_encoding="utf-8")
    content_text=soup.find("div",{"class":"contents"}).text.replace("\n","").replace(" ","")
    return(str(content_text))