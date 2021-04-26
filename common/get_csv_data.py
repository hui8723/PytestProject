import csv

# 从csv中获取用例
def get_csv_data(filePath):
    with open(filePath, 'r') as fp:
        data = []
        try:
            reader = csv.reader(fp)
            headers = next(reader)
            for row in reader:
                data.append(row)
        except Exception as e:
            print('Exception is %s'%e)
        finally:
            fp.close()
    return data

'''
获取所有csv文件的用例，目前只演示一个文件
'''
def get_csv_datas():
    datas = get_csv_data('../data/test.csv')
    # TODO 给list添加下标
    return datas

