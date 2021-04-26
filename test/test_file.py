import json
import os
import csv
from common.get_csv_data import get_csv_datas

# file_path = os.path.join(os.path.dirname(__))

def test_json_file():
    print(os.getcwd())
    with open('../data/test.json', 'r') as fp:
        jsondata = json.load(fp)
        print(jsondata['name'])
        print(type(jsondata))
        # dictdata = json.loads(jsondata)
        # print(type(dictdata))

def test_csv_file():
    # with open('../data/test.csv', 'r') as fp:
    #     data = []
    #     try:
    #         reader = csv.reader(fp)
    #         headers = next(reader)
    #         for row in reader:
    #             data.append(row)
    #     except Exception as e:
    #         print('Exception is %s'%e)
    #     finally:
    #         fp.close()
    data = get_csv_datas()
    print(data)



