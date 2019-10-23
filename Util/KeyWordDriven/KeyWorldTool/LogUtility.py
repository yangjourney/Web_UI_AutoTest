#encoding=utf-8

import logging
from Util.KeyWordDriven.KeyWorldTool import ResultFolder

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def CreateLoggerFile(filename):
    try:
        fulllogname = ResultFolder.GetRunDirectory() + "\\" + filename + ".log"
        fh = logging.FileHandler(filename=fulllogname, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        format_now = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        format_pre = '%(asctime)s [line:%(lineno)d] %(message)s'
        formatter = logging.Formatter(format_now)
        fh.setFormatter(formatter)
        console_filter = ContextFilter()
        fh.addFilter(console_filter)
        logger.addHandler(fh)

    except Exception as err:
        logger.debug("Error when creating log file, error message: {}".format(str(err)))


class ContextFilter(logging.Filter):
    """
    这是一个控制日志记录的过滤器。
    """
    def filter(self, record):
        try:
            # 把remote_connection.py下的log过滤掉
            if 'remote_connection' in record.filename:
                return False
            # if 'connectionpool' in record.filename:
            #     return False
        except AttributeError:
            return False
        return True

