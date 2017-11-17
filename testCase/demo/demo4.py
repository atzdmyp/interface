import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime


# send to
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subject = (u'python邮件发送测试' + ' ' + date)
# 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
# subject = '中文标题'
# subject=Header(subject, 'utf-8').encode()

# defined sender
config = {
    'mail_host': 'smtp.163.com',
    'mail_user': 'hw5zyq@163.com',
    'mail_pass': '930721chennan',
    'mail_port': '25',
    'sender': 'hw5zyq@163.com',
    'receiver': ['1461642306@qq.com'],
    'cc': ['1332850274@qq.com']
}

# defined MIMEMultipart
# 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed')
msg['subject'] = subject
msg['from'] = config['sender']
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['to'] = ";".join(config['receiver'])
msg['Cc'] = ";".join(config['cc'])

# 构造文字内容
text = u"你好:\n    This is the test email for python.\n happy new year."
text_plain = MIMEText(text, 'plain', 'utf-8')
msg.attach(text_plain)

# 构造图片链接
sendimagefile = open(r'E:\其他\桌面壁纸\20.jpg', 'rb').read()
image = MIMEImage(sendimagefile)
image.add_header('Content-ID', '<image1>')
image['Content-Disposition'] = 'attachment; filename="20.jpg"'
msg.attach(image)

# 构造html
html = """
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Happy New Year!<br>
       Here is the <a href="http://www.baidu.com">link</a>. <br>
       Open it, you will watch something that I want you to know.<br>
    </p>
  </body>
</html>
"""
text_html = MIMEText(html, 'html', 'utf-8')
text_html['Content-Disposition'] = 'attachment; filename="testhtml.html"'
msg.attach(text_html)

# 构造附件
sendfile = open(r'F:\study\python\IWantToTallYou.docx')
# sendfile = open(r'F:\AppTest\Test\interfaceTest\result\test.zip', 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att['Content-Type'] = 'Application/octet-stream'
text_att['Content-Disposition'] = 'attachment; filename="test.zip"'
msg.attach(text_att)

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(config['mail_host'])
# smtp.set_debuglevel(1)
smtp.login(config['mail_user'], config['mail_pass'])
smtp.sendmail(config['sender'], config['receiver'], msg.as_string())
smtp.quit()

