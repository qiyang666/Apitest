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
       self.database='config'
       self.table='caseconfig'
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
      #update
    def update_mg(self,_id,config,name,createtime,data):
        tbcase=self.connectmongodb()

        tbcase.update({"_id":ObjectId(_id)},{'$set':{"config":config,"name":name,"createtime":createtime,"data":data}})

    #delete
    def delete_mg(self,_id):
        tbcase=self.connectmongodb()
        tbcase.delete_one({'_id':ObjectId(_id)})

    #select
    def select(self):
        tbcase=self.connectmongodb()
        result=tbcase.find()
        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)
        return l
    def select_configname(self,name):
        tbcase=self.connectmongodb()
        re=tbcase.find({"name":name})
        l=[]
        for i in re:
            l.append(i)
        return l
    def selectbyid(self,_id):
        tbcase=self.connectmongodb()
        result=tbcase.find_one({"_id":ObjectId(_id)})

        result['_id']=str(result['_id'])

        return result



if __name__=="__main__":

    a={"config": {
        'variable_binds': [{'Product_Id': '17212913'}],
        "request": {
            "headers": {
                "product": "1",
                "device-id": "867600024493404",
                "Content-Length": "47",
                "appver": "5.8.9",
                "app_ver": "5.8.9",
                "platform-type": "1",
                "upk": "911877d3c2dd49a8b05ba73d79003511%7C462806171677%7C9d4c96d348b34ff0b5a449800423b977%7C60F6528F2F9ED7EEC0A850582C289827",
                "platform-ver": "6.0",
                "sysver": "6.0",
                "device_id": "867600024493404",
                "app-ver": "5.8.9"
            }
        }
    }
    }

    # Mogo_db().insertcase(data)
    # Mogo_db().insertcase(a)
    # Mogo_db().select()
    #Mogo_db().delete_mg("5a94c8feaeddbf2e1c9eea64")
    Mogo_db().update_mg("5a96548daeddbf246010273f","ab","cd","2900")