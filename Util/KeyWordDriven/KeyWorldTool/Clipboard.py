import win32clipboard as w
import win32con

class Clipboard(object):

    @staticmethod
    def get_text():
        """获取剪切板的内容"""
        try:
            # 打开剪切板
            w.OpenClipboard()
            # 读取数据
            value = w.GetClipboardData(win32con.CF_TEXT)
            # 关闭剪切板
            w.CloseClipboard()
        except Exception as e:
            raise e
        else:
            return value.decode('gbk')

    @staticmethod
    def set_text(value):
        """设置剪切板内容"""
        try:
            w.OpenClipboard()  # 打开剪切板
            w.EmptyClipboard()  # 清空剪切板
            w.SetClipboardData(win32con.CF_UNICODETEXT, value)  # 设置内容
            w.CloseClipboard()  # 关闭
        except Exception as e:
            raise e


