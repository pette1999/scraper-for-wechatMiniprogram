import json
import csv

def writeToFile(filename, data):
    with open(filename, 'a', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # write the data
        writer.writerow(data)

def writeCollege(filename):
    f = open('colleges.json')
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

writeCollege('./data/colleges.csv')