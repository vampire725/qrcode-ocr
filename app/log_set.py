#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: Gpp
@File:   log.py
@Time:   2021/6/29 3:16 下午


loguru配置，用自定义InterceptHandler替换默认python的logging的handler

InterceptHandler修改请参照loguru官方文档。

"""

import logging
import sys

from loguru import logger


def set_logger(level: str = "INFO", store: bool = True, serialize: bool = False):
    """

    - sink          日志输出方式
    - level         日志等级
    - backtrace     是否开启回溯，额外显示异常抛出的过程，基本没用
    - diagnose      是否开启诊断，显示具体报错位置和方法
    - serialize     是否序列化，如果需要直接以json格式输出则开启
    - enqueue       是否异步写入
    - compression   压缩方式
    - rotation      日志文件切分条件，可以为时间“00:00”或者大小"100 MB"
    - retention     日志最大保存时限

    配置输出到别处再logger.add一个config就好。

    :param level:
    :param store:
    :param serialize:
    :return:
    """
    std_log_config = {
        "sink": sys.stderr,
        "level": level,
        "backtrace": False,
        "diagnose": True if level == "DEBUG" else False,
        "serialize": serialize,
        "enqueue": True,
    }

    logger.remove()
    logger.add(**std_log_config)
    if store:
        file_log_config = {
            **std_log_config,
            "sink": "logs/{time}.log",
            "compression": "zip",
            "rotation": "100 MB",
            "retention": "7 days",
        }
        logger.add(**file_log_config)

    logging.getLogger("uvicorn").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.error").handlers = []


class InterceptHandler(logging.Handler):
    """
    实现接管默认Logger
    """

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )
