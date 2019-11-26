import zipfile,shutil,smtplib,configparser
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase #附件
from email.mime.text import MIMEText
from email import encoders #转码
from datetime import date
from Util.KeyWordDriven.KeyWorldTool.ResultFolder import *

def getToday():
    '''获得今天的日期，并把名字改成0901这样的格式'''
    today = date.today()
    date_today = today.strftime("%Y/%m/%d")
    return date_today

def zipDir():
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    lists = os.listdir(test_result_path)
    outFullName = lists[-1]+r".zip"
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(GetRunDirectory()):
        fpath = dirpath.replace(GetRunDirectory(),'') #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            zip.write(os.path.join(dirpath, filename),fpath+filename)
    zip.close()
    shutil.move(outFullName,test_result_path)
    return outFullName

def SendMail_SMTP():
    # 第三方 SMTP 服务
    # 构造 MIMEMultipart 对象做为根容器
    config = configparser.ConfigParser()
    config.read(mail_config)
    # 设置服务器
    mail_host = config.get('SMTP', 'host')
    # 构造一个MIMEMultipart对象代表邮件本身
    message= MIMEMultipart()
    mail_content = '您好，附件内容为本次自动化测试的结果，请注意查收，谢谢。<br>'+getToday()
    message.attach(MIMEText(mail_content, 'html', 'utf-8'))# 正文内容

    message['From'] =config.get('SMTP', 'from_addr')
    message['To'] = config.get('SMTP', 'to_addrs') #收件人地址

    subject = '自动化测试报告' + getToday()
    message['Subject'] = subject  #邮件标题
    filename = zipDir()
    file=GetRunDirectory()
    #添加文件到附件
    with open(file,'rb') as f:
        #这里附件的MIME和文件名
        mime = MIMEBase('zip','zip',filename=filename)
        #加上必要的头信息
        mime.add_header('Content-Disposition','attachment',filename=('gb2312', '', filename))
        mime.add_header('Content-ID','<0>')
        mime.add_header('X-Attachment-Id','0')
        #把附件的内容读进来
        mime.set_payload(f.read())
        #用Base64编码
        encoders.encode_base64(mime)
        message.attach(mime)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(config.get('SMTP', 'from_addr'), config.get('SMTP', 'login_pwd'))
        smtpObj.sendmail(message['From'], message['To'], str(message))  #message.as_string()
        smtpObj.quit()
        #print (u">>>发送邮件成功！")
        #删除生成的zip文件
        os.remove(file)
        #print (u">>>删除文件成功！")
    except smtplib.SMTPException as e:
        print (e)

