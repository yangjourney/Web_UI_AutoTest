from Util.normalTool.TestSuiteInit import *

# 执行用例
if __name__ == '__main__':

    discover = create_suite()
    print ('=====AutoTest Start======')
    now=time.strftime('%Y-%m-%d_%H_%M_%S_')
    title = u'UI自动化测试报告'
    filename = test_result_path+'\\' + now + 'UI_Result.html'
    fp=open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'Test Report', description=u'Case Execution Details:')
    runner.run(discover)
    fp.close()
    mail_content = 'Hi,Attachments Is Test Report,Please Refer .'
    attachments = new_file()
    #print (attachments)
    #SendMail_SMTP(mail_config, attachments)
    print ('=====AutoTest Finished======')
