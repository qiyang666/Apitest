import datetime
from bson import ObjectId
from pymongo import MongoClient
from backend.utils import config
class Mogo_dbcount:
    def __init__(self):
       self.database='testcase'
       self.table='callcount'
       self.ip=config.mg_ip
       self.port=config.mg_port
    def connectmongodb(self):
        client = MongoClient(self.ip,self.port)
        db = client[self.database]
        table=db[self.table]
        return table
    #insert
    def insertcase(self,count):
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data={'count':count,'time':time}
        caseconfig=self.connectmongodb()
        caseconfig.save(data)
    def select(self):
        tbcase=self.connectmongodb()
        result=tbcase.find().sort([("time",-1)]).limit(1)
        l=[]
        for i in result:

            i['_id']=str(i['_id'])
            l.append(i)
        return l

def sorttime(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]<list[j]:
               a=list[i]
               list[i]=list[j]
               list[j]=a

    return list
if __name__=="__main__":
    print(Mogo_dbcount().select())