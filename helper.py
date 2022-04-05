import json
import csv
import os
from tqdm import tqdm

def createCSV(filename, header):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

def writeToFile(filename, data):
    with open(filename, 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # write the data
        writer.writerow(data)

def readCol(filename, colName):
    id = []
    file = csv.DictReader(open(filename, 'r'))
    for col in file:
        id.append(col[colName])

    return id

def removeJsonFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        print("Can not delete the file as it doesn't exists")

def clearCSVfile(filename, header):
    try:
        os.remove(filename)
        createCSV(filename, header)
    except:
        pass

def writeCollege(filename):
    clearCSVfile(filename, ['rank#','admissionTotalNumber','大学','University','isPiublic','website'])
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
    clearCSVfile(filename, ['rank#','id','admissionTotalNumber','学校','城市','service'])
    f = open('./data/json/chineseHighSchools.json')
    data = json.load(f)

    for i in data:
        d = []
        d.append(i['sortNumber'])
        d.append(i['highSchool'].get('id'))
        d.append(i['admissionTotalNumber'])
        d.append(i['highSchool'].get('title'))
        d.append(i['highSchool'].get('svCityName'))
        d.append(i['highSchool'].get('service'))
        writeToFile(filename, d)

def writeInternationalHighSchool(filename):
    clearCSVfile(filename, ['rank#','id','admissionTotalNumber','school','学校','国家','isPublic'])
    f = open('./data/json/internationalHighSchools.json')
    data = json.load(f)
    for i in data:
        d = []
        d.append(i['sortNumber'])
        d.append(i['highSchool'].get('id'))
        d.append(i['admissionTotalNumber'])
        d.append(i['highSchool'].get('title'))
        d.append(i['highSchool'].get('titleEn'))
        d.append(i['highSchool'].get('countryName'))
        d.append(i['highSchool'].get('isPublic'))
        writeToFile(filename, d)

def writeAdvisors(filename):
    clearCSVfile(filename, ['rank#','机构','offers','城市','svLevelTitle','电话','地址','service','special','wechat'])
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

def writeChineseHighDetail(filename):
    university = ['学校'] + readCol('./data/csv/colleges.csv', '大学')
    highschools = readCol('./data/csv/chineseHighSchools.csv', '学校')
    clearCSVfile(filename, university)
    f = open('./data/json/chineseHighDetails.json')
    data = json.load(f)
    for i in tqdm(range(len(data))):
        row = [highschools[i]]
        for j in university[1:]:
            index = 0
            for k in data[i]:
                index += 1
                if k['college'].get('title') == j:
                    row.append(k['admissionTotalNumber'])
                    break
                if index == len(data[i]):
                    row.append('')
        writeToFile(filename,row)

def writeInternationalHighDetail(filename):
    university = ['Schools'] + readCol('./data/csv/colleges.csv', '大学')
    highschools = readCol('./data/csv/internationalHighSchools.csv', 'school')
    clearCSVfile(filename, university)
    f = open('./data/json/internationalHighDetails.json')
    data = json.load(f)
    for i in tqdm(range(len(data))):
        row = [highschools[i]]
        for j in university[1:]:
            index = 0
            for k in data[i]:
                index += 1
                if k['college'].get('title') == j:
                    row.append(k['admissionTotalNumber'])
                    break
                if index == len(data[i]):
                    row.append('')
        writeToFile(filename, row)


writeInternationalHighDetail('./data/csv/internationalHighDetails.csv')