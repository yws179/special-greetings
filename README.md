# Special Greetings
[![](https://img.shields.io/github/release/yws179/special-greetings.svg)](https://github.com/yws179/special-greetings/releases)
[![](https://img.shields.io/github/license/yws179/special-greetings.svg)](https://github.com/yws179/special-greetings/blob/master/LICENSE)
> 将会持续增加新功能..未完待续  
author: yws

:christmas_tree::santa:圣诞节就要到啦！

在wechat给每个前来送祝福的人一张圣诞贺卡:gift:吧！

## 功能介绍
当好友发来节日问候时，自动生成节日贺卡发送给对方。

目前暂时仅支持圣诞节单类型祝福..

更多功能即将龟速加入...

## 效果图
![](./screenshots/effect.png)

## 使用说明
```bash
# 图片二维码登录
python ./setup.py
# 命令行显示二维码登录
python ./setup.py --cmd_qr 1
# 或者
python ./setup.py -q 1
# 如部分的linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2
python ./setup.py --cmd_qr 2
```

## 申明
素材文件来源于网络，未授权商用