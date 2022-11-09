import requests

line_notify_token ='OIJkmqX2WaHdf4NhQsYQiPTL8wXgOgZKqCS5QQMKMyO'
line_notify_api ='https://notify-api.line.me/api/notify'
message='mam'

headers={'Authorization':'Bearer '+line_notify_token}
data={'message':message}
r= requests.post(line_notify_api, headers = headers, data = data)
