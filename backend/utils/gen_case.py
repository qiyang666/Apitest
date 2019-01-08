#coding=utf_8
from backend.utils import mgdb
from backend.utils import mg_ipconfig
def ge_case(data,url,ip,proname):
    data['proname']=proname
    for i in data['testcases']:
        if url in i['request']['url']:
           i['name']=i["name"]+'-'+ip
        i['request']['url']=i['request']['url'].replace(url,ip)

    data['testsuitname']=data['testsuitname']+'-'+ip
    d2=data['reqdata']['reqdata2']['data2']
    d1=data['reqdata']['reqdata1']['data1']
    for n in range(0,len(data['reqdata']['reqdata2']['data2'])) :
        if url in d2[n]['url']:
            d1[n]['formItem']['name']=d1[n]['formItem']['name']+'-'+ip
        d2[n]['url']=d2[n]['url'].replace(url,ip)
    data.pop('_id')
    return data
def ge_case_main(idlist,configid,proname):
    try:
        ipconfig=mg_ipconfig.Mogo_db().selectbyid(configid)

        for i in ipconfig['iplist']:
            for j in idlist:
               data=mgdb.Mogo_db().selectbyid(j)
               d=ge_case(data,ipconfig['url'],i,proname)
               mgdb.Mogo_db().insertcase(d)
        return True
    except Exception as e:
        print(e)
        return False
if __name__=="__main__":
    idlist="5ab4ab7366f6187536e672a0"
    l=idlist.split(",")
    print(l)

    ge_case_main(l,"5ad9b332c3666e096eb464ac","App")
