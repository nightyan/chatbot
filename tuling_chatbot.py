
# 图灵聊天机器人

import requests
import chatbot


class tuling_chatbot(chatbot.chatbot):
    # 获取机器人的回复
    def get_response(self, msg):
        apiurl = 'http://www.tuling123.com/openapi/api'
        data = {
            'key': self.key,
            'info': msg,
            'userid': 'wechat-robot',
        }

        # try-except, 防止服务器没有正常响应
        try:
            r = requests.post(apiurl, data=data).json()
            return r.get('text')
        except Exception as ex:
            print(ex)
            return
