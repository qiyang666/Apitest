import datetime
import hashlib
import json


def gen_md5(*str_args):
    return hashlib.md5("".join(str_args).encode('utf-8')).hexdigest().upper()

def get_sign(d,secret):
    _json1=d['items']
    _json2={}
    for j in _json1:
        if j['key']=='':
            pass
        else:
            _json2[j['key']]=j['value']
    dict_args=json.dumps(_json2)
    # 测试环境
    # secret = "1c303b0eed3133200cf715285011b4e4"
    # 生产环境

    tmp = json.loads(dict_args)
    key_sort = sorted(tmp.keys())
    sign_content = secret
    for i in key_sort:
        sign_content += i + tmp[i]

    new_sign_content = sign_content + secret
    # print(new_sign_content)
    md5 = gen_md5(new_sign_content)
    # print(md5)
    return  md5




if __name__=="__main__":
     pararms={
           #common
        "v":'1.0',
        "timestamp":'2018-06-26 16:39:47',
       "format":"JSON",
       "siteId":"10078",
       "method":"templar.secoo.pictureTask.push",
       "signMethod":"md5",
        #request patameters
        "products":'[{"brand":"Gucci","category":"Shoes","gender":"Men","marketP rice":"240","price":"120","productNum":"423559DKHBU","season":"18SS","skuInfo": [{"color":"black","outerSkuId":"2389112","size":"36","stock":"12"},{"color":"black","outerSkuId":"2389113","size":"37","stock":"12"}],"texture":"100% leather"}]'}
     sign=get_sign(pararms,'123456abcd')


