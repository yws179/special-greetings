# -*- coding: utf-8 -*-

"""
    Special Greetings

    author      : yws
    create_date : 2018/12/20
"""
import argparse

import core


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--cmd_qr', type=int, default=False, help='通过终端显示二维码')
    args = parser.parse_args()
    core.setup(args.cmd_qr)
