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
       self.table='case'
       self.ip=config.mg_ip
       self.port=config.mg_port

    def connectmongodb(self):
        client = MongoClient(self.ip,self.port)
        db = client[self.database]
        table=db[self.table]
        return table

    #insert
    def insertcase(self,data):
        tbcase=self.connectmongodb()
        tbcase.save(data)

    #delete
    def delete_mg(self,_id):
        tbcase=self.connectmongodb()
        tbcase.delete_one({'_id':ObjectId(_id)})

    #update
    def update_mg(self,_id,testcases,config,testsuitname,proname,level,conf,createtime,reqdata):
        tbcase=self.connectmongodb()
        tbcase.update({"_id":ObjectId(_id)},{'$set':{"testcases":testcases,"config":config,"testsuitname":testsuitname,"proname":proname,"level":level,"conf":conf,"createtime":createtime,"reqdata":reqdata}})

    def update_config(self,_id,config):
        tbcase=self.connectmongodb()
        tbcase.update({"_id":ObjectId(_id)},{'$set':{"config":config}})

    def update_result(self,_id,result,updatetime):
        tbcase=self.connectmongodb()
        tbcase.update({"_id":ObjectId(_id)},{'$set':{"result":result,"createtime":updatetime}})

    #select
    def select(self):
        tbcase=self.connectmongodb()
        result=tbcase.find()
        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)
        return l

    def selectbyid(self,_id):
        tbcase=self.connectmongodb()
        result=tbcase.find_one({"_id":ObjectId(_id)})

        result['_id']=str(result['_id'])

        return result

    def selectbyproject_level(self,proname,level):
        tbcase=self.connectmongodb()
        result=tbcase.find({"proname":proname,"level":level})
        l=[]
        for i in result:
            l.append(i)

        return l

    def select_caseoption(self,proname):
        caseopt=[]
        tbcase=self.connectmongodb()
        result=tbcase.find({"proname":proname})

        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)

        for i in l:
            d={'id':i['_id'],'name':i['testsuitname']}
            caseopt.append(d)
        return caseopt

        # return result
if __name__=="__main__":
    Mogo_db().connectmongodb()
    # Mogo_db().delete_mg()
    # Mogo_db().insertcase({'testcases': [{'request': {'url': 'http://las.secoo.com/api/search/keyword', 'json': {'currPage': '1', 'keyword': u'\u83f2\u62c9\u683c\u6155', 'queryType': '1', 'pageSize': '30', 'searchMode': '1'}, 'method': 'POST'}, 'name': u'\u641c\u7d22_\u5173\u952e\u5b57', 'validators': [{'expected': 200, 'check': 'status_code', 'comparator': 'eq'}, {'expected': 0, 'check': 'content.retCode', 'comparator': 'eq'}]}], 'config': {'request': {'headers': {'product': '1', 'platform-ver': '6.0', 'device-id': '867600024493404', 'sysver': '6.0', 'Content-Length': '47', 'appver': '5.8.9', 'app_ver': '5.8.9', 'device_id': '867600024493404', 'platform-type': '1', 'app-ver': '5.8.9', 'upk': '911877d3c2dd49a8b05ba73d79003511%7C462806171677%7C9d4c96d348b34ff0b5a449800423b977%7C60F6528F2F9ED7EEC0A850582C289827'}}}})
    # # Mogo_db().update_mg(data={'_id':0,'name': 'aaa','age': -27,'high': 176})
    # # data={'_id':1,'testcases': [{'request': {'url': 'http://las.secoo.com/api/search/brand', 'json': {'currPage': '1', 'queryType': '1', 'pageSize': '30', 'brandId': '2394'}, 'method': 'POST'}, 'name': u'\u641c\u7d22_\u54c1\u724c', 'validators': [{'expected': 200, 'check': 'status_code', 'comparator': 'eq'}, {'expected': 0, 'check': 'content.retCode', 'comparator': 'eq'}]}, {'request': {'url': 'http://las.secoo.com/api/search/category', 'json': {'currPage': '1', 'categoryId': '_2336_2343_', 'pageSize': '30', 'queryType': '1'}, 'method': 'POST'}, 'name': u'\u641c\u7d22_\u5206\u7c7b', 'validators': [{'expected': 200, 'check': 'status_code', 'comparator': 'eq'}, {'expected': 0, 'check': 'content.retCode', 'comparator': 'eq'}]}, {'request': {'url': 'http://las.secoo.com/api/search/keyword', 'json': {'currPage': '1', 'keyword': u'\u83f2\u62c9\u683c\u6155', 'queryType': '1', 'pageSize': '30', 'searchMode': '1'}, 'method': 'POST'}, 'name': u'\u641c\u7d22_\u5173\u952e\u5b57', 'validators': [{'expected': 200, 'check': 'status_code', 'comparator': 'eq'}, {'expected': 0, 'check': 'content.retCode', 'comparator': 'eq'}]}], 'api': {}, 'config': {'request': {'headers': {'product': '1', 'platform-ver': '6.0', 'device-id': '867600024493404', 'sysver': '6.0', 'Content-Length': '47', 'appver': '5.8.9', 'app_ver': '5.8.9', 'device_id': '867600024493404', 'platform-type': '1', 'app-ver': '5.8.9', 'upk': '911877d3c2dd49a8b05ba73d79003511%7C462806171677%7C9d4c96d348b34ff0b5a449800423b977%7C60F6528F2F9ED7EEC0A850582C289827'}}, 'name': 'search.'}, 'name': 'search.'}
    # # Mogo_db().insertcase(data)
    # Mogo_db().update_mg("5a96667caeddbf2c4c51c74f",[],{},1,1,2,"config1","2019")
    # print(Mogo_db().selectbyproject_level("app",'1'))
    # print(Mogo_db().select())
    # print(Mogo_db().select_caseoption("App"))