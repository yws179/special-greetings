# -*- coding: utf-8 -*-

"""
    贺卡工厂
"""

from PIL import Image, ImageDraw, ImageFont
import tempfile

from config import TMP_DIR, FONT_DIR

HEAD_IMG_WIDTH = 100
HEAD_IMG_HEIGHT = 100

OFFSET_HEIGHT = 20

GREETING_TXT = u'Jingle bells, Jingle bells Jingle all the way.\n\n'\
               u'铃儿响叮当，驯鹿在欢跑；歌声传四方，圣诞节来到。\n\n'\
               u'雪花飘飘洒，带来祥瑞兆；人寿年又丰，人人都欢笑。\n\n'\
               u'圣诞节到了,\n'\
               u'祝 {nick_name} 身体健康，事业成功，家庭美满，快乐围绕！'


def create_card(nick_name, head_img, temp_name):
    """
    创建贺卡
    :param nick_name:   用户昵称
    :param head_img:    用户头像bytes
    :param temp_name:   贺卡模板名
    :return:
    """
    file = tempfile.TemporaryFile()
    file.write(head_img)
    card = render_img(Image.open(file), Image.open(TMP_DIR + temp_name))
    draw = ImageDraw.Draw(card)
    font = ImageFont.truetype(FONT_DIR + 'christmas.ttf', 20)
    draw.text((10, 320), GREETING_TXT.replace('{nick_name}', nick_name), fill=(255, 255, 255), font=font)
    file.close()
    return card


def render_img(head_img, template):
    """
    在模板上绘制头像
    :param head_img:    头像Image
    :param template:    模板Image
    :return:
    """
    head_img = head_img.resize((HEAD_IMG_WIDTH, HEAD_IMG_HEIGHT))
    box = (
        int((template.size[0] - HEAD_IMG_WIDTH) / 2),
        int(template.size[1] - HEAD_IMG_HEIGHT - OFFSET_HEIGHT)
    )
    template.paste(head_img, box)
    return template
