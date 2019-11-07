#encoding=utf-8
from selenium import webdriver
from config.CommonConfig import *
from Util.KeyWordDriven.KeyWorldTool.FormatTime import *
from selenium.webdriver.support.ui import WebDriverWait
from Util.KeyWordDriven.KeyWorldTool import ResultFolder
from Util.KeyWordDriven.KeyWorldTool.Clipboard import *
from Util.KeyWordDriven.KeyWorldTool.KeyBoardUtil import *
import time
import logging

driver=None
#打开浏览器操作
def open_browser(browsername='chrome',*args):
    log_info('open_browser')
    global driver
    try:
        if browsername.lower()=='ie':
            driver=webdriver.Ie(executable_path=ieDriverFilePath)
            driver.maximize_window()
        elif browsername.lower()=='chrome':
            option=webdriver.ChromeOptions()
            option.add_argument('--headless')
            option.add_argument("--disable-infobars")
            driver=webdriver.Chrome(executable_path=chromeDriverFilePath,chrome_options=option,desired_capabilities=None)
            #driver.maximize_window()
        elif browsername.lower()=='firefox':
            option=webdriver.FirefoxOptions()
            option.add_argument('--headless')
            driver=webdriver.Firefox(executable_path=firefoxDriverFilePath,firefox_options=option)
            #driver.maximize_window()
        elif browsername.lower()=='edge':
            # 驱动下载地址
            # https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
            driver=webdriver.Edge(executable_path=edgeDriverFilePath)
            driver.maximize_window()
    except Exception as e:
        logging.error('open_browser  err='+str(e))
        raise e
#访问网址操作
def visit_url(url,*args):
    log_info('visit_url')
    global driver
    try:
        driver.get(url)
    except Exception as e:
        logging.error('visit_url  err='+str(e))
        raise e
#等待操作
def pause(seconds):
    log_info('pause  ')
    seconds=float(seconds)
    time.sleep(seconds)
#进入frame结构操作
def enter_frame(locatormethod,locatorexpression,*args):
    log_info('enter_frame')
    global driver
    try:
        driver.switch_to.frame(getElement(driver,locatormethod,locatorexpression))
    except Exception as e:
        logging.error('enter_frame  err='+str(e))
        raise e
#从frame中切回主文档
def out_frame(*args):
    log_info('out_frame')
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        logging.error('out_frame  err='+str(e))

#输入操作
def input_string(locatormethod,locatorexpression,content,*args):
    log_info('input_string  ')
    global driver
    try:
        element=getElement(driver,locatormethod,locatorexpression)
        element.clear()
        element.send_keys(content)
    except Exception as e:
        log_error('input_string   err='+str(e))
        raise e
#点击操作
def click(locatormethod,locatorexpression,*args):
    log_info('click  ')
    global driver
    try:
        #driver.implicitly_wait(10)
        element=getElement(driver,locatormethod,locatorexpression)
        element.click()
    except Exception as e:
        logging.error('click    err='+str(e))
        raise e

#input类型的下拉框，定位下拉框，然后选择content，然后点击
#仅仅适用于ul/li/span
def input_select_click(locatormethod,locatorexpression,content,*args):
    log_info('input_select_click  ')
    global driver
    try:
        element = getElement(driver, locatormethod, locatorexpression)
        items = element.find_elements_by_xpath("//li/span[contains(text(),'" + content + "')]")
        clickItemFromItems(items,content)
    except Exception as e:
        log_error('input_select_click   err=' + str(e))
        raise e

def clickItemFromItems(items,text):
    if items is not None and len(items) > 0:
        if len(items) > 1:
            for item in items:
                if item.text == text:
                    item.click()
                    break
        else:
            items[0].click()
    else:
        raise ValueError("元素没找到：" + text)

#关闭浏览器操作
def close_browser(*args):
    log_info('close_browser  ')
    global driver
    try:
        driver.quit()
    except Exception as e:
        logging.error('close_browser  err=' + str(e))
        raise e

def get_screen_error_shot(filename):
    log_info('get_screen_error_shot  ')
    global driver
    path1 = os.path.join(ResultFolder.GetRunDirectory(), 'ErrorPicture')
    try:
        if not os.path.exists(path1):
            os.mkdir(path1)
        driver.get_screenshot_as_file(os.path.join(path1,filename)+'.png')
    except Exception as e:
        logging.error('get_screen_error_shot  err=' + str(e))
        raise e
    #返回图片地址
    return os.path.join(path1,filename)+'.png'

def get_screen_shot(filename):
    log_info('get_screen_shot  ')
    global driver
    path1 = os.path.join(ResultFolder.GetRunDirectory(), 'CapturePicture')
    try:
        if not os.path.exists(path1):
            os.mkdir(path1)
        driver.get_screenshot_as_file(os.path.join(path1,filename)+'.png')
    except Exception as e:
        logging.error('get_screen_shot  err=' + str(e))
        raise e
    #返回图片地址
    return os.path.join(path1,filename)+'.png'

#断言操作，判断某个内容是否在页面源码中
def assert_word(word,*args):
    log_info('assert_word  ')
    global driver
    try:
        assert word in driver.page_source
        #print '断言成功！'
        #get_screen_shot(capturepicturepath,dates(),times())
    except Exception as e:
        #断言失败，将页面截图保存，截图存放在当前年月日的目录里，截图名称以当前时分秒命名
        get_screen_error_shot(times())
        logging.error('assert_word  err=' + str(e))
        raise AssertionError('断言失败')

#断言操作，判断某个内容是否在页面源码中
def assert_wholeurl(url,*args):
    log_info('assert_wholeurl  ')
    global driver
    try:
        assert url== driver.current_url
        #print '断言成功！'
        #get_screen_shot(capturepicturepath,dates(),times())
    except Exception as e:
        #断言失败，将页面截图保存，截图存放在当前年月日的目录里，截图名称以当前时分秒命名
        get_screen_error_shot(times())
        logging.error('assert_wholeurl  err=' + str(e))
        raise AssertionError('断言失败')

#断言操作，判断某个内容是否在页面源码中
def assert_parturl(parturl,*args):
    log_info('assert_parturl  ')
    global driver
    try:
        assert parturl in driver.current_url
        #print '断言成功！'
        #get_screen_shot(capturepicturepath,dates(),times())
    except Exception as e:
        #断言失败，将页面截图保存
        get_screen_error_shot(times())
        logging.error('assert_parturl  err='+str(e))
        raise AssertionError('断言失败')

# 获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until\
            (lambda x: x.find_element(by = locateType, value = locatorExpression))
        return element
    except Exception as e:
        logging.error('getElement  err=' +str(e))
        raise Exception('获取元素失败')

# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until\
            (lambda x:x.find_elements(by = locateType, value = locatorExpression))
        return elements
    except Exception as e:
        logging.error('getElements  err='+str(e))
        raise Exception('获取元素失败')

def log_info(info):
    # logging.info(str(info))
    # print(str(info))
    pass

def log_error(info):
    logging.error(str(info))
    print(str(info))

# 模拟ctrl+v键
def ctrl_v(value):
    try:
        Clipboard.set_text(value)
        time.sleep(2)
        KeyBoardKeys.two_keys('ctrl', 'v')
    except Exception as e:
        raise e

# 模拟tab键
def tab_key():
    try:
        KeyBoardKeys.one_key('tab')
    except Exception as e:
        raise e

# 模拟enter键
def enter_key():
    try:
        KeyBoardKeys.one_key('enter')
    except Exception as e:
        raise e
