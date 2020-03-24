import csv
import json
from pathlib import Path
# import requests
from os import listdir
from os.path import isfile, join

def convert_csv_to_json(csv_path):

    headers = []
    liste = []
    csv_version = 1 # csv version


    with open(csv_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',',)
        for row in spamreader:
            # print (row[0])
            if (row[0].encode('ascii', 'ignore')).decode("utf-8") == 'Province/State':
                headers = [x.encode('ascii', 'ignore').decode("utf-8") for x in row[0: 6]]
                # print (headers)
                # print("version 1")
            else:
                # headers = row[2: 5] + row[7: 10]
                headers = ['Province/State', 'Country/Region', 'Last Update', 'Confirmed', 'Deaths', 'Recovered']
                # print (headers)
                # print("version 2")
                csv_version = 2
            break

        for row in spamreader:
            if csv_version == 1:
                row = row[0: 6]              # get rid if useless info
            if csv_version == 2:
                row = row[2: 5] + row[7: 10] # remap to old format

            val = {}
            # print (row)
            for i, j in enumerate(row):
                if headers[i] == 'Confirmed' or headers[i] == 'Deaths' or headers[i] == 'Recovered':
                    if j:
                        val[headers[i]] = int(j)
                    else:
                        val[headers[i]] = 0
                else:
                    val[headers[i]] = j

            liste.append(val)
        # print(liste)

    return liste


# TODO
# list folder
#  if mm-dd-yyyy.json exists do nothing
#  else use mm-dd-yyyy.csv to create it

INPUT_DIR = Path("./csse_covid_19_data/csse_covid_19_daily_reports")

for f in [f_ for f_ in listdir(INPUT_DIR) if isfile(join(INPUT_DIR, f_))]:
    if f.endswith('.csv'):
        full_path = join(INPUT_DIR, f)
        full_new_path = join(INPUT_DIR, f.replace('.csv', '.json'))
        print (f)
        
        json_info = convert_csv_to_json(full_path)
        with open(full_new_path, 'w') as outfile:
            json.dump(json_info, outfile)