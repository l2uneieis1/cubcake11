import sys
import requests

def line_notify_token(message, access_token):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + access_token}
    payload = {'message': message}
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code != 200:
        print('Notification ส่งไม่สำเร็จ', response.text)

token = 'ton0q6Pyo2BvhVtVONDgu4ds6mEM0Fw6b1oUNHYuSRu'
message = 'Hello World'

line_notify_token(message, token)
