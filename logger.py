# -*- coding: utf-8 -*-

import logging


def get_logger():
    """
    创建日志实例
    """
    logger = logging.getLogger('logger')
    formatter = logging.Formatter("%(asctime)s - %(message)s")

    # fh = logging.FileHandler('./logs/sg.log')
    # fh.setFormatter(formatter)
    # fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.DEBUG)

    # logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)
    return logger


logger = get_logger()
