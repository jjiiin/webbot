import pyrebase
from firebase_admin import credentials
from firebase_admin import db
from push_fcm_notification import *
import time

firebaseConfig = {
    "apiKey": "AIzaSyAjJNUWcRdpfeuiytIB_22ZjFXn_ydoHqw",
    "authDomain": "swprojectapp.firebaseapp.com",
    "databaseURL": "https://swprojectapp-default-rtdb.firebaseio.com",
    "projectId": "swprojectapp",
    "storageBucket": "swprojectapp.appspot.com",
    "messagingSenderId": "1063005594107",
    "appId": "1:1063005594107:web:2df2ef2ad8ea33a4ebab5e",
    "measurementId": "G-D3J218FJBZ"
}
firebase =pyrebase.initialize_app(firebaseConfig)
# cred = credentials.Certificate('./serviceAccountKey.json')
# firebase=firebase_admin.initialize_app(cred,{
#     'databaseURL': 'https://swprojectapp-default-rtdb.firebaseio.com'
# })

db=firebase.database()
auth=firebase.auth()

def keywordList():
    keyword=db.child('keyword').get()
    kwList=[]
    for key, val in keyword.val().items():
        kwList.append(val)
    return kwList

def tokenList(keyword):
    token=db.child('keyword_subscribe').child(keyword).get()
    tokenList=[]
    for key, val in token.val().items():
        tokenList.append(val)
    return token.val().items()


def notificationList(keyword, link, uid, dept):
    print("notilist")
    current_time = time.localtime()
    body=f'\"{keyword}\" 키워드가 포함된 공지사항이 등록됐습니다.'
    date={'year':int(current_time.tm_year), 'month': int(current_time.tm_mon), 'day':int(current_time.tm_mday), 'hour':int(current_time.tm_hour), 'minute':int(current_time.tm_min), 'second':int(current_time.tm_sec),}
    db.child('users').child(uid).child(
        'notification').push({'dept':dept, 'body':body, 'date':date, 'link':link,})

def test():
    db.child('test').child('0611').push({'jiin':'test'})

def deptSubscribe(uid, deptNum):
    for i in range(1,4):
        major="major"+str(i)
        sub_major=db.child('users').child(uid).child(major).get()
        if sub_major.val()==deptNum:
            return True
    else:
        return False


def pushNotification(content,link,dept,deptNum):
    print("push!!!!!\n")
    kwList=keywordList()#파이어베이스에서 keyword리스트 가져옴
    for i in kwList:
        if(i in content):
            tkList=tokenList(i)
            for key, value in tkList:
                if deptNum !=0:
                    #학과 공지사항
                    #key(=uid)를 검사해서 해당 학과를 구독했는지 알아봐야함.  
                    if deptSubscribe(key,deptNum)==True:
                        notificationList(i,link,key,dept)
                        send_to_firebase_cloud_messaging(dept,i,value,link)
                
                else:
                    #학교 공지사항
                    notificationList(i,link,key,dept)
                    send_to_firebase_cloud_messaging(dept,i,value,link)