# 初始化日志配置的函数
import logging
import os
from logging import handlers

HEADERS = {"Content-Type": "application/json"}
EMP_ID = ""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    # os.path.dirname(os.path.abspath(__file__))定位当前执行的python文件的父级目录
    filename = BASE_DIR + "./log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when="M",
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding="utf-8"
                                                   )
    # 创建格式处理器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器中（2个）
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器中（2ge）
    logger.addHandler(sh)
    logger.addHandler(fh)

if __name__ == '__main__':
    # 调用初始化日志器函数
    init_logging()
    # 初始化日志之后，利用logging打印日志
    logging.info("Test测试日志打印")