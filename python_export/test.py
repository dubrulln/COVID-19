import csv
import json
# import requests


# response = requests.get('https://connect.deezer.com/oauth/auth.php')

# print("reponse")
# print(response.content)



# data = [["Ravi", "9", "550"], ["Joe", "8", "500"], ["Brian", "9", "520"]]
# with open('students.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerows(data)


def convert_csv_to_json(csv_path):

    headers = []
    liste = []
    csv_version = 1 # csv version


    with open(csv_path, 'r') as csvfile:
        val = {}
        spamreader = csv.reader(csvfile, delimiter=',',)
        for row in spamreader:
            if row[0] == 'Province/State':
                headers = row[0: 6]
                print (headers)
            else:
                # headers = row[2: 5] + row[7: 10]
                headers = ['Province/State', 'Country/Region', 'Last Update', 'Confirmed', 'Deaths', 'Recovered']
                print (headers)
                csv_version = 2
            break

        for row in spamreader:
            if csv_version == 1:
                row = row[0: 6]              # get rid if useless info
            if csv_version == 2:
                row = row[2: 5] + row[7: 10] # remap to old format

            for i, j in enumerate(row):
                val[headers[i]] = j

            liste.append(val)
        print(liste)

    return liste


json_info = convert_csv_to_json("Z:\\Nicolas\\git\\github\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports\\03-21-2020.csv")
with open('03-21-2020.json', 'w') as outfile:
    json.dump(json_info, outfile)