# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-31 16:02

import logging

# 日志级别等级：critical > error > warning > info > debug > notset
# 默认的日志级别：warning
# 默认的日志格式：日志级别、日志输出方式、

# 设置日志信息及格式
# logging.basicConfig(
#     # 设置日志级别
#     level = logging.DEBUG,
#     # 设置日志输出方式[文件方式、控制台方式]
#     filename = "logger.log", # 文件方式，默认是追加的方式
#     # 设置文件日志的打开方式[w:覆盖]
#     filemode = "w",
#     # 设置日志的信息格式化样式
#     format = "%(asctime)s [%(lineno)d] %(message)s"
#
# )
#
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

### 使用logger对象，把日志信息即输出到控制台又输出到文件
logger = logging.getLogger()

# 设置向文件和控制台输出信息
fh = logging.FileHandler("logger.log")
ch = logging.StreamHandler()

# 设置定义日志输出格式
fm = logging.Formatter("%(asctime)s %(message)s")

fh.setFormatter(fm)
ch.setFormatter(fm)

logger.addHandler(fh)
logger.addHandler(ch)

# 设置logger日志的输出级别
logger.setLevel("DEBUG")

logger.debug("logger debug message")
logger.info("logger info message")
logger.warning("logger warning message")
logger.error("logger error message")
logger.critical("logger critical message")


