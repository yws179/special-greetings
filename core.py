# -*- coding: utf-8 -*-
import re

import itchat

import factory
from logger import logger

__MatchRegex = r'(圣诞)|(聖誕)|(Christmas)'


def is_greeting(msg_text):
    """
    判断是否为圣诞问候语
    :param msg_text:    消息文本
    :return:
    """
    return re.search(__MatchRegex, msg_text, re.I) is not None


@itchat.msg_register([itchat.content.TEXT], True, False, False)
def receive_msg(msg):
    if is_greeting(msg['Text']):
        user_name = msg['User']['UserName']
        nick_name = msg['User']['NickName']
        head_img = itchat.get_head_img(user_name)
        card = factory.create_card(nick_name, head_img, 'christmas.png')
        card.save('./temp.png')
        itchat.send_image('./temp.png', toUserName=user_name)
    logger.debug(msg)


def setup():
    itchat.auto_login(hotReload=True, enableCmdQR=False)
    itchat.run()


if __name__ == '__main__':
    setup()
