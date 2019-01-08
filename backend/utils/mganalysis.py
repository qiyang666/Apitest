#coding=utf_8
'''
Created on 2018-2-23
@author:jht
'''
import datetime
import time
from backend.utils import mg_callcounts
from bson import ObjectId
from pymongo import MongoClient
from backend.utils import config
class Mogo_dbana:
    def __init__(self):
       self.database='testcase'
       self.table='dataanalysis'
       self.ip=config.mg_ip
       self.port=config.mg_port
    def connectmongodb(self):
        client = MongoClient(self.ip,self.port)
        db = client[self.database]
        table=db[self.table]
        return table
    #insert
    def insertanalysis(self,datalist,pro_name,api_level):
        tbcase=self.connectmongodb()
        for data in datalist:
            data['pro_name']=pro_name
            data['api_level']=api_level
            data.pop("response")
            data['time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            tbcase.save(data)
        if len(mg_callcounts.Mogo_dbcount().select())==0:

            mg_callcounts.Mogo_dbcount().insertcase(len(datalist))
        else:
            last_count=mg_callcounts.Mogo_dbcount().select()[0]['count']
            mg_callcounts.Mogo_dbcount().insertcase(len(datalist)+last_count)
    def selectbyname(self,name):
        tbcase=self.connectmongodb()
        end=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        start=(datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
        result=tbcase.find({"name":name,"time":{"$gte":start, "$lt":end}})
        l=[]
        countstatus=[]
        for i in result:
            countstatus.append(i['assert'])
            i['_id']=str(i['_id'])
            l.append(i)
        total=len(countstatus)
        sucess=countstatus.count(True)
        fail=total-sucess
        d={"total":total,"sucess":sucess,"fail":fail,"data":l}

        return d
    def select(self):
        tbcase=self.connectmongodb()
        result=tbcase.find()
        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)
        return l

    def selectfalse(self):
        tbcase=self.connectmongodb()
        result=tbcase.find({"assert":False})
        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)
        return l
    def select_responsetime(self):
        tbcase=self.connectmongodb()
        result=tbcase.find()
        totaltime=0
        for i in result:
            totaltime=totaltime+i["responsetime"]
        return totaltime

if __name__=="__main__":
    print(Mogo_dbana().select())
