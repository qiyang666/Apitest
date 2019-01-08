from pymongo import MongoClient
from backend.utils import config

class Mogo_dbscfg:
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
    def selectconfig(self,confname):
        tbcase=self.connectmongodb()
        result=tbcase.find({"name": confname})
        l=[]
        for i in result:
            i['_id']=str(i['_id'])
            l.append(i)
        return l
if __name__=="__main__":
    Mogo_dbscfg().selectconfig("config1")