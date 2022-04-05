import requests
from requests.structures import CaseInsensitiveDict
from tqdm import tqdm
import json
import helper
import os
import time

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
        try:
            resp = requests.post(url, headers=headers, data=data)
            for i in resp.json().get('rankList'):
                colleges.append(i)
        except:
            pass
    # Clean up the json file
    helper.removeJsonFile('./data/json/colleges.json')
    with open('./data/json/colleges.json', 'w', encoding='utf-8') as f:
        json.dump(colleges, f, ensure_ascii=False, indent=2)
    # write data to csv file
    helper.writeCollege('./data/csv/colleges.csv')

def grabChinaHighSchools():
    url = 'https://meiben666.com/api/mb/rank/highSchoolRank'
    highschools = []
    for j in tqdm(range(30)):
        data = '{"openid":1,"highSchoolContry":1,"offerLabel":"","year":"2022","pn":' + str(j+1) + ',"size":15,"childPn":1,"eduLevel":"bk","childSize":3,"comProvinceId":"0","queryString":""}'
        try:
            resp = requests.post(url, headers=headers, data=data)
            for i in resp.json().get('rankList'):
                highschools.append(i)
        except:
            pass
    # Clean up the json file
    helper.removeJsonFile('./data/json/chineseHighSchools.json')
    with open('./data/json/chineseHighSchools.json', 'w', encoding='utf-8') as f:
        json.dump(highschools, f, ensure_ascii=False, indent=2)
    helper.writeChineseHighSchool('./data/csv/chineseHighSchools.csv')

def grabInternationalHighSchools():
    url = 'https://meiben666.com/api/mb/rank/highSchoolRank'
    international = []
    for j in tqdm(range(30)):
        data = '{"openid":1,"highSchoolContry":2,"offerLabel":"","year":"2022","pn":' + str(j+1) + ',"size":15,"childPn":1,"eduLevel":"bk","childSize":3,"comProvinceId":"0","queryString":""}'
        try:
            resp = requests.post(url, headers=headers, data=data)
            for i in resp.json().get('rankList'):
                international.append(i)
        except:
            pass
    # Clean up the json file
    helper.removeJsonFile('./data/json/internationalHighSchools.json')
    with open('./data/json/internationalHighSchools.json', 'w', encoding='utf-8') as f:
        json.dump(international, f, ensure_ascii=False, indent=2)
    helper.writeInternationalHighSchool('./data/csv/internationalHighSchools.csv')

def grabAdvisors():
    url = 'https://meiben666.com/api/mb/rank/adviserRank'
    advisors = []
    for j in tqdm(range(15)):
        data = '{"openid":1,"year":"2022","offerLabel":"","eduLevel":"bk","pn":' + str(j+1) + ',"size":15,"comProvinceId":"0","collegeContryId":"0","queryString":""}'
        try:
            resp = requests.post(url, headers=headers, data=data)
            for i in resp.json().get('rankList'):
                advisors.append(i)
        except:
            pass
    # Clean up the json file
    helper.removeJsonFile('./data/json/advisors.json')
    with open('./data/json/advisors.json', 'w', encoding='utf-8') as f:
        json.dump(advisors, f, ensure_ascii=False, indent=2)
    helper.writeAdvisors('./data/csv/advisors.csv')

def grabChineseHighDetails():
    # grabChinaHighSchools()
    url = 'https://meiben666.com/api/mb/rank/offerListByHighSchool'
    school_details = []
    ids = helper.readCol('./data/csv/chineseHighSchools.csv', 'id')
    for i in tqdm(ids):
        time.sleep(1)
        details = []
        for j in tqdm(range(10)):
            data = '{"openid":1,"highSchoolId":"' + i + '","year":"2022","pn":' + str(j+1) + ',"size":15,"childPn":1,"childSize":3,"parentHighSchoolContry":"1","parentComProvinceId":"0","parentOfferLabel":"","parentEduLevel":"bk"}'
            try:
                resp = requests.post(url, headers=headers, data=data)
                for k in resp.json().get('rankList'):
                    details.append(k)
            except:
                pass
        school_details.append(details)
    # Clean up the json file
    helper.removeJsonFile('./data/json/chineseHighDetails.json')
    with open('./data/json/chineseHighDetails.json', 'w', encoding='utf-8') as f:
        json.dump(school_details, f, ensure_ascii=False, indent=2)

def grabInternationalHighDetails():
    grabInternationalHighSchools()
    url = 'https://meiben666.com/api/mb/rank/offerListByHighSchool'
    school_details = []
    ids = helper.readCol('./data/csv/internationalHighSchools.csv', 'id')
    for i in tqdm(ids):
        time.sleep(1)
        details = []
        for j in tqdm(range(5)):
            data = '{"openid":1,"highSchoolId":"' + i + '","year":"2022","pn":' + str(j+1) + ',"size":15,"childPn":1,"childSize":3,"parentHighSchoolContry":"2","parentComProvinceId":"0","parentOfferLabel":"","parentEduLevel":"bk"}'
            try:
                resp = requests.post(url, headers=headers, data=data)
                for k in resp.json().get('rankList'):
                    details.append(k)
            except:
                pass
        school_details.append(details)
    helper.removeJsonFile('./data/json/internationalHighDetails.json')
    with open('./data/json/internationalHighDetails.json', 'w', encoding='utf-8') as f:
        json.dump(school_details, f, ensure_ascii=False, indent=2)

def grabAdvisorDetails():
    grabAdvisors()
    url = 'https://meiben666.com/api/mb/rank/offerListByAdviserRank'
    advisor_details = []
    ids = helper.readCol('./data/csv/advisors.csv', 'id')
    for i in tqdm(ids):
        time.sleep(1)
        details = []
        for j in tqdm(range(10)):
            data = '{"openid":1,"adviserId":"' + i + '","year":"2022","pn":' + str(j+1) + ',"size":15,"childPn":1,"childSize":3,"parentHighSchoolContry":"0","parentComProvinceId":"0","parentOfferLabel":"","parentEduLevel":"bk"}'
            try:
                resp = requests.post(url, headers=headers, data=data)
                for k in resp.json().get('rankList'):
                    details.append(k)
            except:
                pass
        advisor_details.append(details)
    helper.removeJsonFile('./data/json/advisorDetails.json')
    with open('./data/json/advisorDetails.json', 'w', encoding='utf-8') as f:
        json.dump(advisor_details, f, ensure_ascii=False, indent=2)


grabAdvisorDetails()