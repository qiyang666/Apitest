import requests
import json


# def dec(func):
#     print(func.__name__)
#     return func
#
# @dec
# def hello():
#     print("hello")
#
#
# hello()


# r = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx602a27938a58efa6&secret=fe3a9e6786c0dfdb7db33a02c317e4c8')
#
# print(r.status_code)
# print(r.json())

# 获取token
def get_access_token(appid,secret):
    # r = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx602a27938a58efa6&'
    #                  'secret=fe3a9e6786c0dfdb7db33a02c317e4c8').json()
    r = requests.get(
            url='https://api.weixin.qq.com/cgi-bin/token',
            params={
                'grant_type': 'client_credential',
                'appid': appid,
                'secret': secret
            }
    ).json()
    if r.get("access_token"):
        access_token = r.get('access_token')
    else:
        access_token = None
    return access_token


# 获取openid
def get_openid(appid,secret):
    access_token = get_access_token(appid,secret)
    print(access_token)
    r = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/user/get",
        params={
            'access_token': access_token
        }
    ).json()

    print(type(r))
    openid = r['data']['openid']
    print(openid)
    return openid


# 发送微信公众号文本信息
def send_wx(msg,appid,secret):
    access_token = get_access_token(appid,secret)
    openid = get_openid(appid,secret)
    for i in range(len(openid)):

        body = {
            "touser": openid[i],
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }

        response = requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
            params={
                'access_token': access_token
            },
            data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
        )

        result = response.json()
        print(result)
        return result


# 发送短信
def send_sms(msg,appKey,secretKey):
    r = requests.get(
        url="http://gw.api.taobao.com/router/rest",
        params={
            'method': 'alibaba.aliqin.fc.sms.num.send',
            'extend': '12345',
            'sms_type': 'normal',
            'sms_free_sign_name': '',
            'sms_param': '',
            'rec_num': '15889386666,15889386666',
            'sms_template_code': 'SMS_75835210'
        }
    ).json()






send_wx("hello,yangyunfei",'wx96e146aad611cff9','f5a25cf949cd9c2173b3b36df8ff954b')