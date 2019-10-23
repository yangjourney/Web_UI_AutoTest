#encoding=utf-8

from config.CommonConfig import *
from datetime import datetime


def CreateRunFolder():
    try:
        time = datetime.now()
        foldername = os.path.join(test_result_path, 'TestReport_' + time.strftime("%Y_%m_%d_%H_%M_%S"))
        if not os.path.exists(foldername):
            os.mkdir(foldername)
    except Exception as err:
        print('CreateRunFolder  err=' + str(err))

def GetRunDirectory():
    lists = os.listdir(test_result_path)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_result_path + "\\" + fn))  # 按创建时间排序
    file_new = os.path.join(test_result_path, lists[-1])  # 获取最新的文件保存到file_new
    #print (lists[-1])
    return file_new

