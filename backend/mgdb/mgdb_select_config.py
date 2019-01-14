from pymongo import MongoClient
from bson import ObjectId
from backend.mgdb.config import mgdb_ip, mgdb_port

class Mgdb_by_config():
    def __init__(self):
        self.database = 'config'
        self.table = 'caseconfig'
        self.ip = mgdb_ip
        self.port = int(mgdb_port)

    def connect(self):
        client = MongoClient(self.ip, self.port)
        db = client[self.database]
        table = db[self.table]

        return table

    def select_by_configname(self, configname):
        mg_config = self.connect()
        records = mg_config.find({'name': configname})
        result = []
        for i in records:
            i['_id'] = str(i['_id'])
            result.append(i)

        return result



if __name__ == '__main__':
    # print(Mgdb_by_config().connect())
    print(Mgdb_by_config().select_by_configname('配置1'))
