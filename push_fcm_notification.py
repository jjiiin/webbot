from firebase_admin import messaging
import datetime


def send_to_firebase_cloud_messaging(dept,keyword,token_,link_):
    # This registration token comes from the client FCM SDKs.
    registration_token = token_
    # See documentation on defining a message payload.
    message = messaging.Message(
    notification=messaging.Notification(
        title=f'SWUTICE-{dept}',
        body=f'\"{keyword}\"키워드가 포함된 공지사항이 등록됐습니다.',
    ),android=messaging.AndroidConfig( 
        ttl=datetime.timedelta(seconds=3600), 
        priority='normal', 
        notification=messaging.AndroidNotification( 
            icon='stock_ticker_update', color='#f45342' ), 
            ), 
            apns=messaging.APNSConfig( 
                payload=messaging.APNSPayload( 
                    aps=messaging.Aps(badge=42), ), 
                    ), 
                    data={ 
                        'URL':link_,  },
    token=registration_token,
    )
    
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

def send_to_firebase_cloud_messaging_test():
    # This registration token comes from the client FCM SDKs.
    registration_token = "dsYc79uLQnOLdwtRWPi6jO:APA91bH8oLpnWGV1TvwlFG_pTtsjhURFTH481pVU32V6Fmc05InqmLQRaSRECCYJ48b0FE8Y8m7Wsh70-uVXlt6Xpa8K1HpouKRhmfOwqeVrJjZYkj7SfOjN1G5uAx0Wwz1717oTFGUF"
    # See documentation on defining a message payload.
    message = messaging.Message(
    notification=messaging.Notification(
        title=f'1시간 경과',
        body=f'1시간 경과',
    ),android=messaging.AndroidConfig( 
        ttl=datetime.timedelta(seconds=3600), 
        priority='normal', 
        notification=messaging.AndroidNotification( 
            icon='stock_ticker_update', color='#f45342' ), 
            ), 
            apns=messaging.APNSConfig( 
                payload=messaging.APNSPayload( 
                    aps=messaging.Aps(badge=42), ), 
                    ), 
                    data={ 
                        'URL':"",  },
    token=registration_token,
    )
    
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)