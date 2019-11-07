# -*- coding: utf-8 -*-
"""
FuncName: webutils.py
Desc: committed to a simpler automated testing,based on the original selenium.
Date:
Home:
Author:
CurrentFile = os.path.abspath(os.path.dirname(__file__))
BASE_DIR=os.path.abspath(os.path.dirname(CurrentFile)+os.path.sep+".")
"""
import xlrd
from pykeyboard import PyKeyboard
import os, datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pyperclip
from Util.ExcelUtil.ExcelUtil import getCellValue
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))

class webutils(object):
    """
        webutils framework are committed to a simpler automated testing,
    based on the original selenium.
    """

    def __init__(self, browser="chrome"):
        """
        说明：

        初始化方法，默认使用firefox，当然，在使用过程中也可以使用chrome、ie

        用法：
        webutils("chrome")
        注意事项：
        驱动下载地址：http://npm.taobao.org/mirrors/chromedriver/，根据本地chrome实际版本下载对应的chromedriver
        """
        # global driver
        global driver
        if browser == "firefox" :
            driver = webdriver.Firefox(executable_path=BASE_DIR+'\\DataResourse\\geckodriver')
        elif browser == "chrome":
            driver = webdriver.Chrome(executable_path=BASE_DIR+'\\DataResourse\\chromedriver')
        elif browser == "ie" :
            driver = webdriver.Ie(executable_path=BASE_DIR+'\\DataResourse\\IEDriverServer')
        elif browser == "edge":
            driver = webdriver.Edge(executable_path=BASE_DIR+'\\DataResourse\\msedgedriver')
        try:
            self.driver = driver
        #    self.driver=getattr(webdriver,browser.capitalize())()
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie', 'edge' .")

    def get(self, url):
        """
        说明：打开 url
        用法：driver.get("http://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        说明：设置浏览器最大化
        用法：driver.max_window()
        """
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        说明：设置浏览器宽度和高度
        用法:：driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, secsonds):
        """
        说明：智能等待（隐式等待），全局
        用法：driver.wait(10)
        """
        self.driver.implicitly_wait(secsonds)

    def find_element(self,element):
        """
        说明：设置元素定位方式，如：id、css、xpath、class
        用法：driver.find_element("id|kw")
        """
        if "|" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '|'.")

        by = element.split("|")[0]
        value = element.split("|")[1]

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def wait_element(self, element, seconds=5):
        """
        说明：等待元素加载
        使用场景：在编码过程中根据实际情况选择使用，一般运用于页面加载较慢，网络不畅等一些特殊场景
        用法：driver.wait_element("id|kw",10)
        """
        if "|" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '|'.")

        by = element.split("|")[0]
        value = element.split("|")[1]

        if by == "id":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "text":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def send_keys(self, element, text):
        """
        说明：清除元素内容后执行输入操作
        用法：driver.send_keys("id|kw","selenium")
        """
        self.wait_element(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(text)

    def click(self, element):
        """
        说明：点击任何文字/图片可以点击，连接，复选框，单选按钮，甚至下拉框等。
        用法：driver.click("id|kw")
        """
        self.wait_element(element)
        self.find_element(element).click()

    def right_click(self, element):
        """
        说明：右键点击页面元素
        用法：driver.right_click("class|right")
        """
        self.wait_element(element)
        ActionChains(self.driver).context_click(self.find_element(element)).perform()

    def move_to_element(self, element):
        '''
        说明：将鼠标移动到元素上方
        用法：driver.move_to_element("css|choose")
        '''
        self.wait_element(element)
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    def double_click(self, element):
        """
        说明：双击选定的页面元素
        用法：driver.double_click("name|baidu")
        """
        self.wait_element(element)
        ActionChains(self.driver).double_click(self.find_element(element)).perform()

    def drag_and_drop(self, source_element, target_element):
        """
        说明：拖动一个元素一定的位置后放开。
        用法：driver.drag_and_drop("id|s","id|t")
        """
        self.wait_element(source_element)
        self.wait_element(target_element)
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element), self.find_element(target_element)).perform()

    def back(self):
        """
        说明：返回上一层窗口
        用法：driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        说明：跳转到上一层窗口
        用法：driver.forward()
        """
        self.driver.forward()

    def get_attribute(self, element, attribute):
        """
        说明：获取页面元素的属性值。
        用法：driver.get_attribute("id|kw","attribute")
        """
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """
        说明：获取页面元素的文本信息。
        用法：driver.get_text("name|johnny")
        """
        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        """
        说明：获取要显示的元素，返回结果为true或false。
        用法：driver.get_display("id|ppp")
        """
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        说明：获取窗口标题。
        用法：driver.get_title()
        """
        time.sleep(2)
        return self.driver.title

    def get_url(self):
        """
        说明：获取当前页的URL地址。
        用法：driver.get_url()
        """
        return self.driver.current_url

    def get_screenshot(self, file_path):
        """
        说明：获取当前窗口截图。
        用法：driver.get_screenshot("./pic.png")
        """
        self.driver.get_screenshot_as_file(file_path)

    def submit(self, element):
        """
        说明：提交指定表格。
        用法：driver.submit("id|mainFrame")
        """
        self.wait_element(element)
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        """
        说明：切换到特定的frame。
        用法：driver.switch_to_frame("id|mainFrame")
        """
        self.wait_element(element)
        self.driver.switch_to.frame(self.find_element(element))

    def clearCookies(self):
        """
        说明：在初始化浏览器的时候清除所有的cookies
        用法：self.driver.clearCookies()
        """
        self.driver.delete_all_cookies()


    def switch_to_frame_out(self):
        """
        说明：切换默认的上下文。
        用法：driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, element):
        """
        说明：打开新窗口并将句柄切换到新打开的窗口。
        用法：driver.open_new_window(id|johnny)
        """
        current_windows = self.driver.current_window_handle
        self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)
    def F5(self):
        '''
        说明：刷新当前页面。
        用法：driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        """
        说明：执行JavaScript脚本。
        用法：driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alert(self):
        """
        说明：确认按钮
        用法：driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        说明：取消对话框
        用法：driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        说明：关闭当前窗体。
        用法：driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        说明：退出该驱动程序并关闭所有窗口。
        用法：driver.quit()
        """
        self.driver.quit()
    def upload(self,element,file):
        """
        说明：上传文件,将文件放在DataResourse\img中，传文件名即可。
        用法：driver.upload("id|kw","demo1.jpg")
        """
        # 获取目录
        #BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
        self.wait_element(element)
        self.find_element(element).click()
        pyperclip.copy(BASE_DIR+"\\DataResourse\\img\\"+file)
        time.sleep(2)
        k = PyKeyboard()
        #SendKeys(str(pyperclip.paste()))
        k.tab_key(k.enter_key)
        #SendKeys("{ENTER}")

    def set_js_write(self):
        """
        说明：输入框可以编辑
        用法：driver.set_js_write()
        """
        js = "$('input[class=el-input__inner]').removeAttr('readonly')"
        self.js(js)

    def  set_js_abled(self):
        """
        说明：输入框可以使用
        用法：driver.set_js_abled()
        """
        js1="$('input[class=el-input__inner]').attr('disabled',false)"
        self.js(js1)


def get_dic_xls_xpath(sheet, row, new_name):
    """
    返回xpath
    :return: xls_path
    示例：
    self.autoDriver.click("xpath|.//span[contains(text(),'新增')]/parent::button") ====>self.autoDriver.click(get_dic_xls_xpath(1,21,'基础数据'))
    """
    xls_path=BASE_DIR+'\\DataResourse\\WebDictionary.xls'
    # noinspection PyBroadException
    try:
        #xls_xpath_split = unicode(getCellValue(sheet, row, 2, xls_path)).split("$") ---Python2[unicode],Python3[str]
        xls_xpath_split = str(getCellValue(sheet, row, 2, xls_path)).split("$")
        xls_xpath_split.append(xls_xpath_split[-1])
        xls_xpath_split[2] = eval("new_name")
        xls_xpath = ''.join(map(str, xls_xpath_split))
    except:
        #xls_xpath = unicode(getCellValue(sheet, row, 2, xls_path))
        xls_xpath = str(getCellValue(sheet, row, 2, xls_path))

    return xls_xpath


def get_xls_data(sheet, row, col, date_type):
    """
    返回数据
    :return: xls_path
    示例：
    self.autoDriver.send_keys("xpath|.//*[@for='code']/following-sibling::*//input",unicode(cropType,"utf-8")) ========>
    self.autoDriver.send_keys(get_dic_xls_xpath(1,21),get_xls_data(0,49,""))
    """
    xls_path=BASE_DIR+'\\DataResourse\\TestDataDictionary.xls'
    if date_type == "int":
        xls_data = int(getCellValue(sheet, row, col, xls_path))
    elif date_type == "data":
        date = xlrd.xldate_as_tuple(getCellValue(sheet, row, col, xls_path),0)
        xls_data = datetime.datetime(*date)
    else:
        xls_data = getCellValue(sheet, row, col, xls_path)

    return xls_data
