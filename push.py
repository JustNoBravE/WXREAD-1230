import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD, EMAIL_RECIPIENT

logger = logging.getLogger(__name__)

class EmailNotification:
    def __init__(self):
        self.email_host = EMAIL_HOST
        self.email_port = EMAIL_PORT
        self.email_user = EMAIL_USER
        self.email_password = EMAIL_PASSWORD
        self.email_recipient = EMAIL_RECIPIENT

    def send_email(self, subject, content):
        """发送邮件通知"""
        try:
            # 创建邮件对象
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['From'] = Header(EMAIL_USER)
            msg['To'] = Header(EMAIL_RECIPIENT)
            msg['Subject'] = Header(subject)

            # 连接SMTP服务器并发送邮件
            with smtplib.SMTP_SSL(self.email_host, self.email_port) as server:
                server.login(self.email_user, self.email_password)
                server.sendmail(self.email_user, [self.email_recipient], msg.as_string())
            logger.info("✅ 邮件发送成功")
        except Exception as e:
            logger.error("❌ 邮件发送失败: %s", e)

def push(content):
    """统一推送接口，支持邮件发送"""
    notifier = EmailNotification()
    subject = "微信阅读推送通知"
    notifier.send_email(subject, content)