#coding=utf_8
'''
Created on 2018-2-23
@author:jht
'''
import datetime
import time
from backend.utils import config
from bson import ObjectId
from pymongo import MongoClient
class Mogo_dbreport:
    def __init__(self):
       self.database='report'
       self.table='cronreport'
       self.ip=config.mg_ip
       self.port=config.mg_port
    def connectmongodb(self):
        client = MongoClient(self.ip,self.port)
        db = client[self.database]
        table=db[self.table]
        return table
    #insert
    def insertreport(self,data):
        tbcase=self.connectmongodb()
        tbcase.save(data)
    def select(self):
        tbcase=self.connectmongodb()
        result=tbcase.find().sort([("time",-1)]).limit(20)
        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)
        return l
    def selectbycid(self,cid):
        tbcase=self.connectmongodb()
        result=tbcase.find({"cid":int(cid)}).sort([("time",-1)]).limit(1)
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
    def selectbyprolev(self,name,level):

        if len(level)==0:
            tbcase=self.connectmongodb()

            level=['1','2','3']
            resu=[]
            total=0
            sucess=0
            fail=0
            times=[]
            for j in level:
                result=tbcase.find({"pro_name":name,"api_level":j}).sort([("time",-1)]).limit(1)
                l=[]

                for i in result:

                    times.append(datetime.datetime.strptime(i['time'], "%Y-%m-%d %H:%M:%S"))
                    total=total+i['total']
                    sucess=sucess+i['pass']
                    fail=fail+i['fail']
                    for m in i['result']:
                        m['api_level']=i['api_level']
                    i['_id']=str(i['_id'])
                    l.extend(i['result'])

                resu.extend(l)
            if len(resu)==0:
                return {"result":resu}
            else:
                maxtime=sorttime(times)[0]
                mintime=sorttime(times)[-1]
                t=str(mintime)+" - "+str(maxtime)


                return {"pro_name":name,"total":total,"pass":sucess,"fail":fail,"time":t,"result":resu}
        else:
            tbcase=self.connectmongodb()
            resu=[]
            for j in level:
                result=tbcase.find({"pro_name":name,"api_level":j}).sort([("time",-1)]).limit(1)
                l=[]
                for i in result:
                    for m in i['result']:
                        m['api_level']=i['api_level']
                    i['_id']=str(i['_id'])
                    l.append(i)
                resu.extend(l)
            if len(resu)==0:

                return {"result":resu}
            else:
                casereport=resu[0]
                return {"pro_name":casereport['pro_name'],"total":casereport["total"],"pass":casereport["pass"],"fail":casereport["fail"],"time":casereport["time"],"result":casereport["result"]}

def sorttime(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]<list[j]:
               a=list[i]
               list[i]=list[j]
               list[j]=a

    return list

if __name__=="__main__":
        print(Mogo_dbreport().selectbycid("37"))
