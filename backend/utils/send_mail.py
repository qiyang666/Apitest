# -*- coding: utf-8 -*-

from  Ultraman import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
def sendemail(title,message,receiver):
       #发送方
       sender=settings.EMAIL_HOST_USER
       #接收方
       # receiver="390999543@qq.com"
       #发送的内容：标题，正文
       msgRoot = MIMEMultipart()
       msgRoot['Subject'] = title
       msgRoot['From'] = sender
       msgRoot['To'] = receiver
       msgRoot.attach(MIMEText(message))
       # #构造附件
       # att = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')  #读取附件的内容
       # filename1=re.split("[/,\\\\]",path)
       # att["Content-Disposition"] = 'attachment; filename='+filename1[len(filename1)-1]  #附件名称
       # msgRoot.attach(att)  #装载附件
       try:
       #建立连接
          s = smtplib.SMTP()
          s.connect(settings.EMAIL_HOST)
       #认证
          s.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
       #发送邮件
          s.sendmail(sender,receiver.split(","), msgRoot.as_string())
          s.quit()
       except Exception as e:
              print(str(e))





if __name__ == "__main__":
    sendemail("测试报告","此处为测试报告","390999543@qq.com")

