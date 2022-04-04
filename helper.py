import json
import csv

def writeToFile(filename, data):
    with open(filename, 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # write the data
        writer.writerow(data)

def writeCollege(filename):
    f = open('./data/json/colleges.json')
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    for i in data:
        d = []
        d.append(i['sortNumber'])
        d.append(i['admissionTotalNumber'])
        d.append(i['college'].get('title'))
        d.append(i['college'].get('titleEn'))
        d.append(i['college'].get('isPublic'))
        d.append(i['college'].get('website'))
        writeToFile(filename,d)

def writeChineseHighSchool(filename):
    f = open('./data/json/chineseHighSchools.json')
    data = json.load(f)

    for i in data:
        d = []
        d.append(i['sortNumber'])
        d.append(i['admissionTotalNumber'])
        d.append(i['highSchool'].get('title'))
        d.append(i['highSchool'].get('svCityName'))
        d.append(i['highSchool'].get('service'))
        writeToFile(filename, d)

def writeInternationalHighSchool(filename):
    f = open('./data/json/internationalHighSchools.json')
    data = json.load(f)
    for i in data:
        d = []
        d.append(i['sortNumber'])
        d.append(i['admissionTotalNumber'])
        d.append(i['highSchool'].get('title'))
        d.append(i['highSchool'].get('titleEn'))
        d.append(i['highSchool'].get('countryName'))
        d.append(i['highSchool'].get('isPublic'))
        writeToFile(filename, d)

def writeAdvisors(filename):
    f = open('./data/json/advisors.json')
    data = json.load(f)
    for i in data:
        d = []
        d.append(i['sortNumber'])
        d.append(i['adviser'].get('title'))
        d.append(i['adviser'].get('offers'))
        d.append(i['adviser'].get('svCityName'))
        d.append(i['adviser'].get('svLevelTitle'))
        d.append(i['adviser'].get('telPhone'))
        d.append(i['adviser'].get('address'))
        d.append(i['adviser'].get('service'))
        d.append(i['adviser'].get('special'))
        d.append(i['adviser'].get('wechat'))
        writeToFile(filename, d)

writeAdvisors('./data/csv/advisors.csv')