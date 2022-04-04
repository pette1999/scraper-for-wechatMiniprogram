import requests
from requests.structures import CaseInsensitiveDict
from tqdm import tqdm
import json

headers = CaseInsensitiveDict()
headers["Host"] = "meiben666.com"
headers["jwt"] = "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDg5MzYwNzYsInN1YiI6IntcImlzdXVlZEF0XCI6MTY0ODkzNjA3NjAwNSxcInVzZXJJZFwiOlwiNDQ0NjNmNWMtOWY2ZS00ODgzLTlhZGUtNWM0ZWEyNmZhOWRkXCJ9In0.ZKV0_mqYmh9ee7QzuyJQCIbhRvVAJOybzU654-GzANQ"
headers["content-type"] = "application/json;charset=UTF-8"
headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123c) NetType/WIFI Language/zh_CN"
headers["Referer"] = "https://servicewechat.com/wxa16727f16c02cc80/63/page-frame.html"

def grabColleges():
    url = "https://meiben666.com/api/mb/rank/collegeAdmissionRank"
    colleges = []
    for j in tqdm(range(20)):
        data = '{"openid":1,"year":"2022","collegeContryId":"0","collegeLabel":"","eduLevel":"bk","offerType":"ALL","pn":' + str(j+1) + ',"size":15,"childPn":1,"childSize":3,"comProvinceId":"0","queryString":""}'
        resp = requests.post(url, headers=headers, data=data)
        for i in resp.json().get('rankList'):
            colleges.append(i)
    # print(colleges)
    with open('./data/json/colleges.json', 'w', encoding='utf-8') as f:
        json.dump(colleges, f, ensure_ascii=False, indent=2)

def grabChinaHighSchools():
    url = 'https://meiben666.com/api/mb/rank/highSchoolRank'
    highschools = []
    for j in tqdm(range(30)):
        data = '{"openid":1,"highSchoolContry":1,"offerLabel":"","year":"2022","pn":' + str(j+1) + ',"size":15,"childPn":1,"eduLevel":"bk","childSize":3,"comProvinceId":"0","queryString":""}'
        resp = requests.post(url, headers=headers, data=data)
        for i in resp.json().get('rankList'):
            highschools.append(i)
    with open('./data/json/chineseHighSchools.json', 'w', encoding='utf-8') as f:
        json.dump(highschools, f, ensure_ascii=False, indent=2)

def grabInternationalHighSchools():
    url = 'https://meiben666.com/api/mb/rank/highSchoolRank'
    international = []
    for j in tqdm(range(30)):
        data = '{"openid":1,"highSchoolContry":2,"offerLabel":"","year":"2022","pn":' + str(j+1) + ',"size":15,"childPn":1,"eduLevel":"bk","childSize":3,"comProvinceId":"0","queryString":""}'
        resp = requests.post(url, headers=headers, data=data)
        for i in resp.json().get('rankList'):
            international.append(i)
    with open('./data/json/internationalHighSchools.json', 'w', encoding='utf-8') as f:
        json.dump(international, f, ensure_ascii=False, indent=2)


grabInternationalHighSchools()