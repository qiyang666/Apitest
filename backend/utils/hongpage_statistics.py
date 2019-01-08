from backend.utils import mgdb
from backend.utils import mganalysis
from backend.utils import mysqldb,mg_callcounts

def statistics():
    interface_count=0
    for i in mgdb.Mogo_db().select():
        interface_count=interface_count+len(i['testcases'])
    call_numbers=mg_callcounts.Mogo_dbcount().select()[0]['count']
    project_count=mysqldb.selectprojectcount()

    data={"interface_count":interface_count,"call_numbers":call_numbers,"project_count":project_count}
    return data
