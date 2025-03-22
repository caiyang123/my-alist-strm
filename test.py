import requests

url = "http://47.116.197.124:5244/api/admin/storage/list"

payload={}
headers = {
   'Authorization': 'alist-c12d6984-b2c5-43ed-986a-3696d9b03c7cdNKELQWdi1jfKbqhSB1MpXe8pCVk15WfHZ6a5vwM6CP1rspD5kVCiZjzFdghlDt8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)