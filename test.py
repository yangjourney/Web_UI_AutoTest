# coding:utf-8
import smtplib,configparser,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

def SendMail(mail_config_file,content,file):
    # 第三方 SMTP 服务
    # 构造 MIMEMultipart 对象做为根容器
    config = configparser.ConfigParser()
    config.read(mail_config_file)
    # 设置服务器
    mail_host = config.get('SMTP', 'host')
    #message = MIMEText(content, 'plain', 'utf-8')#正文内容   plain代表纯文本

    # 构造一个MIMEMultipart对象代表邮件本身
    message= MIMEMultipart()
    message.attach(MIMEText(content, 'html', 'utf-8'))# 正文内容   plain代表纯文本,html代表支持html文本

    message['From'] =config.get('SMTP', 'from_addr')
    message['To'] = ','.join(config.get('SMTP', 'to_addrs')) #与真正的收件人的邮箱不是一回事

    subject = 'Python自动邮件-%s' % time.ctime()
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

if __name__ == "__main__":
    mailpath = "D:\Web_UI_AutoTest\config\mail.conf"
    content='''
            <h1>测试</h1>
            <h2 style="color:red">仅用于测试</h1>
            <a">ces</a><br>
            <p>图片演示：</p>
            <p><img src="cid:image1"></p>
          '''
    file=r"D:\\Web_UI_AutoTest\\Report\\2019-10-14_10_28_30_UI_Result.html"
    SendMail(mailpath,content,file)
