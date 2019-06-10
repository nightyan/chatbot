
# qingyun聊天机器人

import requests
# from urllib import parse
import chatbot


class qingyun_chatbot(chatbot.chatbot):
    # 获取机器人的回复
    def get_response(self, msg):
        apiurl = 'http://api.qingyunke.com/api.php?'
        data = {
            'key': 'free',
            'appid': 0,
            'msg': msg
        }
        # parse.urlencode(data)

        # try-except, 防止服务器没有正常响应
        try:
            r = requests.get(apiurl, params=data).json()
            if r.get('result') == 0:
                return r.get('content')
            else:
                raise Exception(r.get('content'))
        except Exception as ex:
            print(ex)
            return
