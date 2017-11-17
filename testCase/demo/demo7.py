import requests
import json


#钉钉机器人测试
def doPost():
    url="https://oapi.dingtalk.com/robot/send?access_token=f28e760720f46c64f80c01b22c345f6049c386fd607cc0cf8582f02623b917e6"
    postdata={
        "msgtype": "text",
        "text": {
            "content": "(｡･∀･)ﾉﾞ嗨，我来找你玩了！"
        },
        "at": {
            "atMobiles": [

             ],
            "isAtAll": True
        }
     }
    postdata = json.dumps(postdata)
    head = {
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.post(url, headers=head, data=postdata)
    print(response.text)

if __name__ == "__main__":
    doPost()
