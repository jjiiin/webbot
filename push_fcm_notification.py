
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin import datetime
from pyfcm import FCMNotification

#cred_path=os.path.join(BASE_DIR)
cred = credentials.Certificate('serviceAccountKey.json')
default_app=firebase_admin.initialize_app(cred)
API_KEY="AAAA94ASIfs:APA91bEsEWCCLNcGKVoqwkmRp0ImFuXa3NAZ0rC5sbCjF8Fi1pCz77lzM1dYbCVEKiJysHKDO4943OaSkW8qI5NM4eH72BolGUd4SJdok-EwCMvN29WJAi73URgVU3ypYHQNbsmwSAgh"
push_service=FCMNotification(api_key=API_KEY)
def send_to_firebase_cloud_messaging(dept,keyword,token_,link_):
    # This registration token comes from the client FCM SDKs.
    registration_token = token_
    # See documentation on defining a message payload.
    message = messaging.Message(
    notification=messaging.Notification(
        title=f'SWUTICE-{dept}',
        body=f'\"{keyword}\"키워드가 포함된 공지사항이 등록됐습니다.',
    ), data={  'URL':link_,  },
        token=registration_token,
    )
    data_message_={
        "body":f'\"{keyword}\"키워드가 포함된 공지사항이 등록됐습니다.',
        "title":f'SWUTICE-{dept}'
    }
    response = messaging.send(message)
    #response=push_service.single_device_data_message(registration_id=token_,data_message=data_message_)
    # Response is a message ID string.
    print('Successfully sent message:', response)
