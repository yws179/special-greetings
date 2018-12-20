# -*- coding: utf-8 -*-

import itchat
import factory


def is_self():
    pass


@itchat.msg_register([itchat.content.TEXT], True, False, False)
def receive_msg(msg):
    user_id = msg['FromUserName']
    user_name = msg['User']['NickName']
    head_img = itchat.get_head_img(user_id)
    file = open("./img/%s.jpg" % user_name, 'wb')
    file.write(head_img)
    file.close()
    factory.create_card(user_name, 'christmas.jpg')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=False)

    itchat.run()
