import requests
from flask import Flask
import time
import threading

app = Flask(__name__)

def line_notify_token(message, access_token):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + access_token}
    payload = {'message': message}
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code != 200:
        app.logger.error('Notification ส่งไม่สำเร็จ: %s', response.text)

def background_task():
    cnt = 1
    for _ in range(10):
        line_notify_token(f'Hello, World! {cnt}', 'ton0q6Pyo2BvhVtVONDgu4ds6mEM0Fw6b1oUNHYuSRu')
        cnt += 1
        time.sleep(1)

@app.route('/')
def index():
    return 'Flask is running and background task is started!'

if __name__ == '__main__':
    # Start the background task
    threading.Thread(target=background_task, daemon=True).start()
    app.run(host='0.0.0.0', port=80)
