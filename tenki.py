import pprint
import requests
import urllib.request as req
import json
import csv

area_dic = {'aomori':'020000',
            'nara':'290000'}
output_file="weather_report.csv"
header=["ken","date","day","u","n","a","wind","wave"]

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json"
filename = 'tenki.json'

def main():
    make_csv()

def make_csv():
    with open(output_file,'w',encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)

        write_lists=get_info()

        writer.writerows(write_lists)

def get_info():
    write_lists = []
    base_url ="https://www.jma.go.jp/bosai/forecast/data/forecast/"
    for k,v in area_dic.items():

        if k.find("/"):
            prefecture = k[0:k.find("/")]
        else:
            prefecture = k

        url = base_url + v +".json"

        res = requests.get(url).json()

        for re in res:
            publishingOffice = re["publishingOffice"]
            reportDatetime = re["reportDatetime"]

            timeSeries = re["timeSeries"]

            for time in timeSeries:
                if 'pops' in time["areas"][0]:
                    pass
                elif 'temps' in time["areas"][0]:
                    pass
                elif 'tempsMax' in time["areas"][0]:
                    pass
                else:
                    for i in range(len(time["areas"])):
                        local_name = time["areas"][i]["area"]["name"]

                        for j in range(len(timeSeries[0]["timeDefines"])):
                            if 'weathers' not in time["areas"][i]:
                                weather =""
                            else:
                                weather = time["areas"][i]["weathers"][j]

                            if 'winds' not in time["areas"][i]:
                                wind = ""
                            else:
                                wind = time["areas"][i]["winds"][j]

                            if 'waves' not in time["areas"][i]:
                                wave = ""
                            else:
                                wave = time["areas"][i]["waves"][j]

                            timeDefine = time["timeDefines"][j]

                            write_list = []
                            write_list.append(prefecture)
                            write_list.append(publishingOffice)
                            write_list.append(reportDatetime)
                            write_list.append(local_name)
                            write_list.append(timeDefine)
                            write_list.append(weather)
                            write_list.append(wind)
                            write_lists.append(write_list)
    return write_lists
if __name__ == '__main__':
    main()
