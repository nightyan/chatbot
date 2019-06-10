
# 聊天机器人main入口

import config
import itchat

# import tuling_chatbot as robot
# robot = robot.tuling_chatbot(config.TULING_KEY)
# import simsimi_chatbot as robot
# robot = robot.simsimi_chatbot(config.SIMSIMI_KEY)
import qingyun_chatbot as robot
robot = robot.qingyun_chatbot(config.QINGYUN_KEY)


# 注册文本消息，如果收到会调用下面的方法
@itchat.msg_register(itchat.content.TEXT)
def ai_reply(msg):  # 回复微信消息
    reply = robot.reply(msg)
    return reply


itchat.auto_login(hotReload=True)
itchat.run()