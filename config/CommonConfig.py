#-*- coding:utf-8 -*-
import pymysql
import os

#文件所在目录
file_path=os.path.dirname(__file__)

#工程所在目录
project_path=os.path.dirname(os.path.dirname(__file__))

#测试数据路径
general_test_path=os.path.join(project_path,'Tests\\AutoUITests\\XiaoYuanDeliversVegetables')
keyword_excel_path=os.path.join(project_path,'Tests\\KeyWordDricenTests',u"关键字驱动测试用例.xlsx")

#测试结果文件夹路径
mail_config=os.path.join(project_path,'config',u"mail.conf")
log_config=os.path.join(project_path,'config',u"mlogconfig.yml")
test_result_path=os.path.join(project_path,'Report')

#浏览器驱动路径
ieDriverFilePath=os.path.join(project_path,'DataResourse','IEDriverServer')#chromedriver，对应IE浏览器版本为11
chromeDriverFilePath=os.path.join(project_path,'DataResourse','chromedriver')#chromedriver,对应谷歌浏览器版本为78.0.3904.70
firefoxDriverFilePath=os.path.join(project_path,'DataResourse','geckodriver')#geckodriver，对应火狐浏览器版本为60+
edgeDriverFilePath=os.path.join(project_path,'DataResourse','msedgedriver.exe')#msedgedriver，对应EDGE浏览器版本为79.0.309.14

if __name__=='__main__':
    print ('file_path='+file_path)
    print ('project_path='+project_path)
    #print ('keyword_excel_path='+keyword_excel_path)
    print(test_result_path)
    print(mail_config)
