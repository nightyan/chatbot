
# 聊天机器人，基类
import config


class chatbot(object):
    def __init__(self, key):
        self.key = key

    # 回复
    def reply(self, msg):
        response = self.get_response(msg['Text'])
        return response or config.DEFAULT_REPLY

    # 获取机器人的回复
    def get_response(self, msg):
        return ""
