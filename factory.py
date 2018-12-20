"""
    贺卡工厂
"""

from PIL import Image, ImageDraw, ImageFont

HEAD_IMG_WIDTH = 50
HEAD_IMG_HEIGHT = 50

OFFSET_HEIGHT = 20

TMP_DIR = './img/'
GREETING_TXT = u'Jingle bells, Jingle bells Jingle all the way.'\
               u'铃儿响叮当，驯鹿在欢跑；歌声传四方，圣诞节来到。雪花飘飘洒，带来祥瑞兆；'\
               u'人寿年又丰，人人都欢笑。圣诞节到了，祝{user_name}身体健康，事业成功，家庭美满，快乐围绕！'


def create_card(user_name, temp_name):
    head_img = Image.open(TMP_DIR + user_name + ".jpg")
    temp = render_img(head_img, Image.open(TMP_DIR + temp_name))
    draw = ImageDraw.Draw(temp)
    font = ImageFont.truetype('./font/christmas.ttf', 20)
    print(font.font_bytes)
    draw.text((10, 10), GREETING_TXT.replace('{user_name}', user_name), fill=(255, 255, 255), ttf=font)
    temp.show()


def render_img(head_img, template):
    head_img = head_img.resize((HEAD_IMG_WIDTH, HEAD_IMG_HEIGHT))
    box = (
        int((template.size[0] - HEAD_IMG_WIDTH) / 2),
        int(template.size[1] - HEAD_IMG_HEIGHT - OFFSET_HEIGHT)
    )
    template.paste(head_img, box)
    return template
