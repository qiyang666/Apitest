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
       self.database='testcase'
       self.table='ipconfig'
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
    def update_mg(self,_id,url,iplist):
        tbcase=self.connectmongodb()

        tbcase.update({"_id":ObjectId(_id)},{'$set':{"url":url,"iplist":iplist}})

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
    def select_ipconfigurl(self,url):
        tbcase=self.connectmongodb()
        re=tbcase.find({"url":url})
        l=[]
        for i in re:
            l.append(i)
        return l
    def selectbyid(self,_id):
        tbcase=self.connectmongodb()
        result=tbcase.find_one({"_id":ObjectId(_id)})

        result['_id']=str(result['_id'])

        return result

    def select_ipconfig_option(self):
        ipselction=Mogo_db().select()


        return ipselction

if __name__=="__main__":

    # data={'url':'las.secoo.com','iplist':['192.168.1.1','192.168.2.2']}
    #
    # # Mogo_db().insertcase(data)
    # Mogo_db().update_mg("5ad9969eaeddbf1608c51b8d","las.secoo.com",['1'])
    # print(Mogo_db().select_ipconfigurl("las.secoo.com"))
    # print(Mogo_db().select())
    # Mogo_db().delete_mg("5ad98d50aeddbf18f07be00c")
    # Mogo_db().update_mg("5a96548daeddbf246010273f","ab","cd","2900")
    print(Mogo_db().selectbyid("5ad9b332c3666e096eb464ac"))