# coding:utf-8
import smtplib, configparser, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import win32com.client as win32

def SendMail_SMTP(mail_config_file,file):
    # 第三方 SMTP 服务
    # 构造 MIMEMultipart 对象做为根容器
    config = configparser.ConfigParser()
    config.read(mail_config_file)
    # 设置服务器
    mail_host = config.get('SMTP', 'host')
    # 构造一个MIMEMultipart对象代表邮件本身
    message= MIMEMultipart()
    mail_content = 'Hi,Attachments Is Test Report,Please Refer .'
    message.attach(MIMEText(mail_content, 'html', 'utf-8'))# 正文内容
    message['From'] =config.get('SMTP', 'from_addr')
    message['To'] = ','.join(config.get('SMTP', 'to_addrs')) #收件人地址

    subject = 'AutoUI_TestReport-%s' % time.ctime()
    message['Subject'] = subject  #邮件标题

    #添加文件到附件
    with open(file,'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('text', 'txt', filename=file)
        # filename是显示附件名字
        mime.add_header('Content-Disposition', 'attachment', filename=file)
        # 获取附件内容
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        message.attach(mime)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(config.get('SMTP', 'from_addr'), config.get('SMTP', 'login_pwd'))
        smtpObj.sendmail(config.get('SMTP', 'from_addr'), config.get('SMTP', 'to_addrs'), str(message))  #message.as_string()
        smtpObj.quit()
        print (u"邮件发送成功")
    except smtplib.SMTPException as e:
        print (e)

def SendMail_OutLook(mail_config_file,file):
    # 构造 MIMEMultipart 对象做为根容器
    config = configparser.ConfigParser()
    config.read(mail_config_file)
    olook = win32.Dispatch("outlook.Application")#固定写法
    mail = olook.CreateItem(win32.constants.olMailItem)#固定写法
    mail.To = config.get('SMTP', 'to_addrs')#收件人
    # mail.Recipients.Add(addressee)
    mail.Subject = 'AutoUI_TestReport-%s' % time.ctime() #邮件主题
    mail.Attachments.Add(file, 1, 1, "myFile")
    read = open(file, encoding='utf-8')#打开需要发送的测试报告附件文件
    content = read.read()#读取测试报告文件中的内容
    read.close()
    mail.Body = content#将从报告中读取的内容，作为邮件正文中的内容
    mail.Send()#发送

