from pymongo import MongoClient
from bson import ObjectId
from backend.mgdb.config import mgdb_ip, mgdb_port

class Mgdb_case():
    def __init__(self):
        self.database = 'testcase'
        self.table = 'case'
        self.ip = mgdb_ip
        self.port = int(mgdb_port)

    def connect(self):
        client = MongoClient(self.ip, self.port)
        db = client[self.database]
        table = db[self.table]
        return table

    def insert_case(self, data):
        mg_case = self.connect()
        mg_case.save(data)

    def select_all(self):
        mg_case = self.connect()
        records = mg_case.find()
        result = []
        for i in records:
            i['_id'] = str(i['_id'])
            result.append(i)

        return result

    def select_by_id(self, _id):
        mg_case = self.connect()
        record = mg_case.find_one({'_id': ObjectId(_id)})
        record['_id'] = str(record['_id'])

        return record

    def delete_one(self, _id):
        mg_case = self.connect()
        mg_case.delete_one({'_id': ObjectId(_id)})


if __name__ == '__main__':

    Mgdb_case().connect()
    # print(connt)
    # Mgdb_case().insertcase({'name': 'qy'})
    # print(Mgdb_case().select_all())
    id = '5c384fc78ffaed062b246ac9'
    # print(Mgdb_case().select_by_id(id))
    Mgdb_case().delete_one(id)
