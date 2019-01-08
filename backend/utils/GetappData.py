#coding=utf_8
import json
import os
import random
import re
import requests
from bs4 import BeautifulSoup


class Get_appData(object):
    def __init__(self):
     self.header={'Host': 'las.secoo.com', 'Cookie': 'Sid=a12cf9822cab43d1a1040271033e2805|249674844287|D76911A3A7764E85CE3B28D4B4B182F8|17BEED46B969743F80D9B500DB85622F; __jsluid=0abc60657296b0140bdea7cb703106a5; SUN=18510336921; Sid=a12cf9822cab43d1a1040271033e2805|249674844287|67B10D9733D14208C2B91196A71F1643|B8E61C55ACF4234B8D66A53242507E46', 'upk': 'a12cf9822cab43d1a1040271033e2805|249674844287|D76911A3A7764E85CE3B28D4B4B182F8|17BEED46B969743F80D9B500DB85622F', 'User-Agent': 'Secoo-iPhone/6.0.0 (iPhone; iOS 10.3.2; Scale/3.00)', 'app-id': '1096539101', 'X-Tingyun-Id': 'IYSvMxBahhI;c=2;r=597377294;u=48e9f41f41c38a6d261f286ab8e07e57', 'channel': 'AppStore', 'screen-width': '1242', 'device-id': '304E33C4-0A3F-405A-A8D9-B1C3998C5F04', 'platform-type': '0', 'screen-height': '2208', 'platform': 'iPhone8,2', 'Connection': 'keep-alive', 'Accept-Language': 'zh-Hans-CN;q=1', 'idfv': '43F527AB-8EF7-4932-9324-6E4E50808B66', 'app-ver': '6.0.0', 'product': '0', 'platform-ver': '10.30', 'Accept': '*/*', 'Accept-Encoding': 'gzip', 'idfa': '62C80ED3-6E2D-435F-93B1-F37D2435BBD4'}
     self.url='https://las.secoo.com/api/home/home_page_head'
    def session_get(self,url1):
        self.url=url1
        s=requests.session()
        try:
            result=s.get(url=url1,headers=self.header,verify=False)
        except Exception as e:
            pass
        else:
            return result

    def data_dirs(self,folder_name):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        DATA_DIRS = (os.path.join(BASE_DIR,folder_name),)
        d='/'.join(DATA_DIRS)
        return d
    def get_page_head(self):
        result=Get_appData().session_get(self.url)
        try:
            taps=result.json()['tabs']
        except Exception as e:
            print(e)
        urls=[i['url']for i in taps]
        titles=[i['title']for i in taps]
        hd=zip(urls,titles)
        hd=dict(hd)
        return urls,hd
    def sign_404(self,url,message):

            r = requests.get(url,verify=False)
            blog = r.content
            soup = BeautifulSoup(blog, "lxml")
            m='pcDate":"%s"'%message
            h1userSoupList = soup.findAll(eventdata=re.compile(m))
            for o in h1userSoupList:
                 o['style']='border: solid 9px red'

            if 'db' in h1userSoupList[0]['class'] and 'more'in h1userSoupList[0]['class']:
                d=soup.prettify("utf-8")
                if message=='':
                    name='defalut'+str(random.randrange(1,100))+".html"
                else:
                    name=''.join(message.split('/'))+".html"

                with open(self.data_dirs('frontend/static')+'/'+name,'wb')as f:
                    f.write(d)
                return {"url":url[8:],'error':name}
            elif 'db'not in h1userSoupList[0]['class'] and 'more'not in h1userSoupList[0]['class']:
                d=soup.prettify("utf-8")
                if message=='':
                    name='defalut'+str(random.randrange(1,100))+".html"
                else:
                    name=''.join(message.split('/'))+".html"

                with open(self.data_dirs('frontend/static')+'/'+name,'wb')as f:
                    f.write(d)

                return {"url":url[8:],'error':name}
    def find_topic(self,url):
        list=[]
        result=[]
        r = requests.get(url,verify=False)
        blog = r.content
        soup = BeautifulSoup(blog, "lxml")
        h1userSoupList = soup.findAll(eventdata=True)
        for i in h1userSoupList:
            c=i.attrs['eventdata']
            try:
                c=json.loads(c)
            except Exception as e:
                continue
            if c['type']=='0':
                if 'topic'in c['pcDate']:
                    message=c['pcDate']
                    topicid=int(c["pcDate"][9:14])
                    newtopicurl="https://las.secoo.com/api/topic/topic_list_new?id=%d&pageid=topicNew/%d"%(topicid,topicid)
                    r1=requests.get(newtopicurl,verify=False)
                    if r1.status_code==200:
                        list.append(newtopicurl)
                    if r1.status_code==404:
                        f=self.sign_404(url,message)
                        if isinstance(f,dict):
                            result.append(f)
                elif '20163——ac' in c['pcDate']:
                    pass
                else:
                    message=c['pcDate']
                    apptopic="https://m.secoo.com/appActivity/%s.shtml"%c['pcDate']

                    r2=requests.get(apptopic,verify=False)
                    if r2.status_code==200:
                       list.append(apptopic)
                    if r2.status_code==404:
                        f=self.sign_404(url,message)
                        if isinstance(f,dict):
                            result.append(f)

            elif c['type']=='100':
                message=c['pcDate']
                appactivity=c['pcDate']

                r3=requests.get(appactivity,verify=False)
                if r3.status_code==200:
                    list.append(appactivity)
                if r3.status_code==404:
                    f=self.sign_404(url,message)
                    if isinstance(f,dict):
                            result.append(f)
            else:
                pass

        return result,list
    def get_pagedata1(self):#首页一级接口测试404
        d=[]
        l=[]
        for url in Get_appData().get_page_head()[0]:
            try:
                result=Get_appData().session_get(url).json()
            except Exception as e:
                pass

            for i in result['floors']:

                        if i['type']!='13':
                           try:
                                list1=i['list']
                           except KeyError as e:
                               print(e)

                           for j in list1:
                                if j['urlType']=='5':

                                    try:
                                        title=j['title']
                                        index=i['index']
                                    except KeyError as e:
                                        title=''

                                    tap=Get_appData().get_page_head()[1][url]
                                    r=requests.get(j['url'],verify=False)

                                    a={"tap":tap,'index':index,'title':title,'url':j['url']}
                                    if r.status_code!=200:
                                        d.append(a)
                                elif j['urlType']=='1':#普通专题
                                    try:
                                        title=j['title']
                                    except KeyError as e:
                                        title=''
                                        pass
                                    if 'topic'in j['url']:

                                        topicid=int(j['url'][9:])
                                        newtopicurl="https://las.secoo.com/api/topic/topic_list_new?id=%d&pageid=topicNew/%d"%(topicid,topicid)
                                        l.append(newtopicurl)
                                        r1=requests.get(newtopicurl,verify=False)
                                        b={"tap":tap,'index':index,'title':title,'url':j['url']}
                                        if r1.status_code!=200:
                                            d.append(b)
                                    else:
                                        apptopic="https://m.secoo.com/appActivity/%s.shtml"%j['url']
                                        l.append(apptopic)
                                        r2=requests.get(apptopic,verify=False)
                                        c={"tap":tap,'index':index,'title':title,'url':j['url']}
                                        if r2.status_code!=200:
                                            d.append(c)


        return d,l
    def get_pagedata2_3(self):#首页二、三级页面测试
        urls=Get_appData().get_pagedata1()[1]
        urls=list(set(urls))
        datalist=[]
        datalist1=[]
        result=[]
        for i in urls:
                try:
                    f=self.find_topic(i)
                    if len(f[1])>0:
                        datalist.extend(f[1])
                    if len(f[0])>0:
                        result.extend(f[0])
                except Exception as e:
                    print(e)
        datalist=list(set(datalist))
        for i in datalist:
                try:
                    f=self.find_topic(i)
                    if len(f[1])>0:
                        datalist1.extend(f[1])
                    if len(f[0])>0:
                        result.extend(f[0])
                except Exception as e:
                    print(e)

        datalist1=list(set(datalist1))
        for i in datalist1:
                try:
                    f=self.find_topic(i)
                    # if len(f[1])>0:
                    #     datalist1.extend(f[1])
                    if len(f[0])>0:
                        result.extend(f[0])
                except Exception as e:
                    print(e)
        print(result)
    def test_url(self,url):
        datalist=[]
        datalist1=[]
        datalist2=[]
        result=[]
        #一级页面404
        f=self.find_topic(url)
        if len(f[1])>0:
            datalist.extend(f[1])
        if len(f[0])>0:
            result.extend(f[0])
        #二级页面404
        for i in datalist:
            f=self.find_topic(i)
            if len(f[1])>0:
               datalist1.extend(f[1])
            if len(f[0])>0:
               result.extend(f[0])
        #三级页面
        for j in datalist1:
            f=self.find_topic(j)
            if len(f[1])>0:
               datalist2.extend(f[1])
            if len(f[0])>0:
               result.extend(f[0])
        #四级页面
        for m in datalist2:
            f=self.find_topic(m)
            if len(f[0])>0:
               result.extend(f[0])
        return result


if __name__=="__main__":
    # print(Get_appData().find_topic("https://las.secoo.com/api/topic/topic_list_new?id=27467&pageid=topicNew/27467"))
    # print(Get_appData().session_get("https://las.secoo.com/api/home/home_page?code=1").json())
    # print(Get_appData().get_page_head())
    # print(Get_appData().get_pagedata2())
    url='https://las.secoo.com/api/topic/topic_list_new?id=24919&pageid=topicNew/24919'
    message='topicNew/24920'
    # Get_appData().sign_404(url,message)
    # Get_appData().get_pagedata2_3()
    # print(Get_appData().get_page_head())

    # print(Get_appData().find_topic(url))
    print(Get_appData().data_dirs('frontend/static'))