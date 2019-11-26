#  -*- coding: utf-8 -*-

import unittest, time, os
from config.CommonConfig import *

# 1.产生测试套件
def create_suite():
    #global discover, filename
    test_unit = unittest.TestSuite()
    # 使用discover找出用例文件夹下test_case的所有用例
    # 测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none
    discover = unittest.defaultTestLoader.discover(general_test_path,pattern='test_*.py', top_level_dir=None)
    #print (discover)
    # 使用for循环出suite,再循环出case
    for suite in discover:
        for case in suite:
            test_unit.addTests(case)
    return test_unit

# 2.定义：取最新测试报告
def new_file():
    #  读取测试报告路径
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_result_path)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(test_result_path+'\\'+fn))
    # 获取最新文件的绝对路径
    file_path=os.path.join(test_result_path,lists[-1])
    return file_path
