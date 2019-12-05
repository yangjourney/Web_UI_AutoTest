#  -*- coding: utf-8 -*-
# from Util.HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from Util.normalTool.sendmail import SendMail_SMTP
from Util.normalTool.TestSuiteInit import *
from config.CommonConfig import *
from BeautifulReport import BeautifulReport

# 执行用例
if __name__ == '__main__':
    discover = create_suite()
    print ('=====AutoTest Start======')
    now=time.strftime('%Y-%m-%d_%H_%M_%S_')
    BeautifulReport(discover).report(filename=now + 'UI_Result', description='小源送菜自动化测试', log_path=test_result_path)    #log_path='.'把report放到当前目录下
    # title = u'UI自动化测试报告'
    # filename = test_result_path+'\\' + now + 'UI_Result.html'
    # fp=open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title=u'Test Report', description=u'Case Execution Details:')
    # runner.run(discover)
    # fp.close()
    # 发送邮件
    # SendMail_SMTP()
    print ('\n=====AutoTest Over======')
