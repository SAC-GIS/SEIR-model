import csv
import json
import sys
import collections # 有序字典
 
def trans(path):
    jsonData=open(path+'.json')
    #csvfile = open(path+'.csv', 'w')#此处这样写会导致写出来的文件会有空行
    csvfile = open(path+'.csv', 'wb')#python2下
    data = {}
    keys_write = True
    writer = csv.writer(csvfile)
    # def is_json(jsonData):
    #     try:
    #         json.loads(jsonData)
    #     except Exception as e:
    #       return e
    # return True
    # is_json(jsonData)
    for line in jsonData:#获取属性列表
        print(line[0:-1])
        dic=json.loads(line[0:-1])
        keys=dic.keys()
        break
            
    for dic in jsonData:#读取json数据的每一行，将values数据一次一行的写入csv中
 
        print(dic)
        dic=json.loads(dic[0:])
        
        for key in keys:
            if dic.has_key(key):
                data[key] = dic[key]
            else:
                data[key] = ""
        print(data)
 
        if keys_write == True:
            writer.writerow(data.keys())
        writer.writerow(data.values())
        keys_write = False
        
    jsonData.close()
    csvfile.close()
trans(r'C:\Users\o\Desktop\疫情预测\SEIR\data\corona_virus_of_china')