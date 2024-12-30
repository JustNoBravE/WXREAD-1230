# config.py 自定义配置

import os
import re
import logging

# 设置日志配置
logging.basicConfig(level=logging.INFO)

"""
GitHub Action部署或本地部署
从环境变量获取值,如果不存在使用默认本地值
"""

# 邮件推送配置
EMAIL_HOST = 'pop.88.com'  # SMTP服务器地址
EMAIL_PORT = 995  # SSL端口
EMAIL_USER = 'jyh8888@88.com'  # 发件人邮箱地址
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # 从环境变量获取密码
EMAIL_RECIPIENT = 'jyh8888@88.com'  # 收件人邮箱地址

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM', '120'))

# 复制的curl_bath命令
curl_str = os.getenv('WXREAD_CURL')

# 初始化headers和cookies字典
headers = {}
cookies = {}

# 如果curl_str存在，则提取headers和cookies
if curl_str:
    headers, cookies = convert(curl_str)

def convert(curl_command):
    """提取headers与cookies"""
    global headers, cookies
    # 提取 headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0]] = match[1]

    # 提取 cookies
    cookie_string = headers.pop('cookie', '')
    for cookie in cookie_string.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value

    return headers, cookies

# 其他配置（如data等）保持不变
data = {
    # ... 数据保持不变
}