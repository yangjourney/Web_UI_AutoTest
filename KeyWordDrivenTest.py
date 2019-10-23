from Util.KeyWordDriven.KeyWorldTool.Control import *

#可以直接在windows CMD窗口中执行测试
#python xxxx/KeyWordDrivenTest.py
#xxxx为KeyWordDrivenTest.py文件的所在路径，如C:/Web_UI_AutoTest

if __name__ == "__main__":#这个类直接被运行的时候，以下的代码会被执行
    newrun = RunTests()
    newrun.setUpKeyword()
    #发送邮件：LoadAndRunTestCases_Keyword(1)，不发送邮件：LoadAndRunTestCases_Keyword(0)
    newrun.LoadAndRunTestCases_Keyword(0)