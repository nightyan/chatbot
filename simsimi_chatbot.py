
# simsimi聊天机器人

import requests
import chatbot


class simsimi_chatbot(chatbot.chatbot):
    # 获取机器人的回复
    def get_response(self, msg):
        apiurl = 'https://wsapi.simsimi.com/190410/talk'
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.key
        }
        data = {
            'utext': msg,
            'lang': 'ch'  # 'en'
        }

        # try-except, 防止服务器没有正常响应
        try:
            r = requests.post(apiurl, headers=headers, json=data).json()
            if r.get('status') == 200:
                return r.get('atext')
            else:
                raise Exception(r.get('statusMessage'))
        except Exception as ex:
            print(ex)
            return
