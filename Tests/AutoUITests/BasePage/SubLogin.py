# coding=utf-8
from Tests.AutoUITests.BasePage import BasePage
from Util.seleniumTool.Selenium_Webdriver import get_dic_xls_xpath
from pykeyboard import PyKeyboard

class SubLogin(BasePage.BasePage):
    def __init__(self, driver, baseUrl):
        """
        :param driver:
        :param baseUrl:
        """
        # 调用其 基类 BasePage的 构造函数
        # 实现 基类 的构造函数的功能
        BasePage.BasePage.__init__(self, driver, baseUrl)
        self.loginPageUrl = "login"
        self.driver.clearCookies()

    def login(self, userName, password, VerificationCode):
        self.openPage(self.loginPageUrl)
        # self.driver.clearCookies()
        self.driver.wait(5)
        self.driver.send_keys(get_dic_xls_xpath(1,1,'用户名'),userName)
        self.driver.send_keys(get_dic_xls_xpath(1,2,'密码'),password)
        self.driver.send_keys(get_dic_xls_xpath(1,3,'验证码'),VerificationCode)
        self.driver.click(get_dic_xls_xpath(1,4,'登录'))
        #self.driver.send_keys("xpath|.//*[@placeholder='请输入用户名']",userName)
        #self.driver.send_keys("xpath|.//*[@placeholder='请输入密码']",password)
        #self.driver.send_keys("xpath|.//*[@placeholder='请输入验证码']",VerificationCode)
        #self.driver.click("xpath|//div[@class='flex-x-center flex-y-center btn-login']")

    def getMainPage(self):
        return self.baseUrl
