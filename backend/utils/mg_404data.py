#coding=utf_8
'''
Created on 2018-2-23
@author:jht
'''
from bson import ObjectId
from pymongo import MongoClient
from backend.utils import config
class Mogo_db:
    def __init__(self):
       self.database='report'
       self.table='404data'
       self.ip=config.mg_ip
       self.port=config.mg_port
    def connectmongodb(self):
        client = MongoClient(self.ip,self.port)
        db = client[self.database]
        table=db[self.table]
        return table
    #insert
    def insertcase(self,data):
        caseconfig=self.connectmongodb()
        caseconfig.save(data)
    #select
    def select(self):
        tbcase=self.connectmongodb()
        result=tbcase.find().sort([("time",-1)]).limit(1)
        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)
        return l

if __name__=="__main__":
    from backend.utils.get_currenttime import get_currentdate
    timenow=get_currentdate()
    data={'url':'las.secoo.com','error':'test.html','time':timenow}

    print(Mogo_db().select())
