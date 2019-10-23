# coding=utf-8
from Util.seleniumTool.Selenium_Webdriver import get_dic_xls_xpath
from Tests.AutoUITests.Login.test_Login import *
import logging
import unittest,random,time,re

"""
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例 方法以  开头
4. 考虑使用 setUp() 和 tearDown()
"""
# BASE_DIR = re.match('(.*\{sep}AutoTests-master)\{sep}'.format(sep=os.sep), __file__).group(1)
# logsignleton = LogSignleton(BASE_DIR+'\\config\\logconfig.yml')
# logger = logsignleton.get_logger()
# name="测试部门wgy"+str(random.randint(0,9999))
# newName="测试部门ding"+str(random.randint(0,9999))
# firstMenu="基础信息"
# secondMenu="部门管理"
# name='634'+str(random.randint(0,9999))
phone = '133'+str(random.randint(1000,5555))+str(random.randint(6666,9999))
class test_depart(unittest.TestCase):

    def setUp(self):

        """
        开始每个测试前的准备事项
        :return:
        """
        self.autoDriver = webutils()
        self.autoDriver.max_window()
        self.baseUrl="http://10.2.5.35:8040/merchant/#/login"
        self.autoDriver.wait(30)
        #调用登录方法
        TestLogin.login(self)

    def tearDown(self):
        """
        结束每个测试后的清理工作
         :return:
        """
        self.autoDriver.quit()

    def test_1addUser(self):
        logging.info(u'addDepartment（新增用户） UI test start')
        time.sleep(3)
        self.autoDriver.click("xpath|.//h3[contains(text(),'设置')]")
        time.sleep(3)
        self.autoDriver.click("xpath|.//li[contains(text(),'员工管理')]")
        time.sleep(3)
        self.autoDriver.click("xpath|//button[@class='el-button ops-btn el-button--primary el-button--mini']")
        time.sleep(3)
        self.autoDriver.send_keys(get_dic_xls_xpath(1,8,'登录帐号'),phone)
        #self.autoDriver.send_keys("xpath|.//*[@for='loginName']/following-sibling::*//input",phone)
        self.autoDriver.click("xpath|//input[@placeholder='请选择']")
        time.sleep(3)
        self.autoDriver.click("xpath|.//span[contains(text(),'店长')]")
        self.autoDriver.send_keys("xpath|.//*[@for='nickName']/following-sibling::*//input","t1"+str(random.randint(0,9999)))
        self.autoDriver.send_keys("xpath|.//*[@for='password']/following-sibling::*//input","123456")
        self.autoDriver.send_keys("xpath|.//*[@for='confirmPassword']/following-sibling::*//input","123456")
        self.autoDriver.send_keys("xpath|.//*[@for='mobile']/following-sibling::*//input",phone)
        self.autoDriver.send_keys("xpath|.//*[@for='identityCard']/following-sibling::*//input","5112001"+phone)
        self.autoDriver.click("xpath|.//span[contains(text(),'是')]")
        time.sleep(3)
        self.autoDriver.click("xpath|.//span[contains(text(),'确认')]/parent::button")
        #self.autoDriver.click(get_dic_xls_xpath(0,16,"确认"))
        time.sleep(3)
        self.autoDriver.click("xpath|.//li[contains(text(),'员工管理')]")
  #  def test_2editUser(self):

