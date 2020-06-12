import time
import logging.handlers
import os
BASE_ARITCAL_TITLE = "天气很好_{}".format(time.strftime("%d%H%M%S"))
BASE_PATH = os.path.dirname(os.path.abspath("__file__"))


def base_logger_config():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    ls = logging.StreamHandler()
    lh = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + "/log/test.log",when="midnight",interval=1,backupCount=2)
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    ls.setFormatter(formatter)
    lh.setFormatter(formatter)
    logger.addHandler(ls)
    logger.addHandler(lh)