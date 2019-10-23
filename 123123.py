
from Util.KeyWordDriven.KeyWorldTool.ResultFolder import *

def zipDir():
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    dirpath = GetRunDirectory()
    lists = os.listdir(test_result_path)

    outFullName = lists[-1]+r".zip"
    print("outFullName:="+outFullName)

zipDir()