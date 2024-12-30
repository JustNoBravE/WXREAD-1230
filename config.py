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

PUSH_METHOD = os.getenv('PUSH_METHOD', 'email')  # 默认使用 email 推送方法


# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM', '2'))

# 复制的curl_bath命令
curl_str = os.getenv('WXREAD_CURL')

# 初始化headers和cookies字典
cookies = {
    'pac_uid': '0_0c7dc76933357',
    'iip': '0',
    '_qimei_uuid42': '184170f260a100c761caea05ee40b0962cabc59681',
    '_qimei_q36': '',
    '_qimei_h38': '24b1969561caea05ee40b09602000004d18417',
    'wr_gid': '296444248',
    'wr_pf': '0',
    'wr_localvid': 'b49320808106fa6a8b49ca6',
    'wr_name': '%E6%B8%B8%E9%BE%99',
    'wr_gender': '1',
    '_clck': 'zq4pnj|1|fmw|0',
    'suid': 'user_0_0c7dc76933357',
    'pgv_pvid': '3904711160',
    'RK': 'Y28p1Uo3nZ',
    'ptcz': 'd4ae0de5f7e34c0fa739c35b47638e7b8ad33e13c32964233b66ebff78b7abc1',
    'wr_vid': '275752616',
    'wr_rt': 'web%40qAC2602vcB8SNydPTZs_AL',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FZ6uRYmvbnrqpDmwAlnkWBDQOvic7M3M93ykvbiaTA70XzSDXulm1xMMudyoHPb5hruMA7p7bgkYOaiaG3JZaDQLQH2X82uteTsHEVUD6Ib5GmE%2F132',
    'wr_fp': '1296956703',
    '_qimei_fingerprint': 'f070808fc45d2ba9d06a87b3707fb583',
    'wr_theme': 'white',
    'wr_skey': 'Z7HcF7gz',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=fe24dd1dc4de48158773d7eb798d2bf0',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'pac_uid=0_0c7dc76933357; iip=0; _qimei_uuid42=184170f260a100c761caea05ee40b0962cabc59681; _qimei_q36=; _qimei_h38=24b1969561caea05ee40b09602000004d18417; wr_gid=296444248; wr_pf=0; wr_localvid=b49320808106fa6a8b49ca6; wr_name=%E6%B8%B8%E9%BE%99; wr_gender=1; _clck=zq4pnj|1|fmw|0; suid=user_0_0c7dc76933357; pgv_pvid=3904711160; RK=Y28p1Uo3nZ; ptcz=d4ae0de5f7e34c0fa739c35b47638e7b8ad33e13c32964233b66ebff78b7abc1; wr_vid=275752616; wr_rt=web%40qAC2602vcB8SNydPTZs_AL; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FZ6uRYmvbnrqpDmwAlnkWBDQOvic7M3M93ykvbiaTA70XzSDXulm1xMMudyoHPb5hruMA7p7bgkYOaiaG3JZaDQLQH2X82uteTsHEVUD6Ib5GmE%2F132; wr_fp=1296956703; _qimei_fingerprint=f070808fc45d2ba9d06a87b3707fb583; wr_theme=white; wr_skey=Z7HcF7gz',
    'dnt': '1',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/ce032b305a9bc1ce0b0dd2ake2c32140247e2c420d92577',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': 'fe24dd1dc4de48158773d7eb798d2bf0-98cb4de511e214e7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}


# 保留| 默认读三体，其它书籍自行测试时间是否增加
data = {
    "appId": "wb182564874663h152492176",
    "b": "ce032b305a9bc1ce0b0dd2a",
    "c": "7cb321502467cbbc409e62d",
    "ci": 70,
    "co": 0,
    "sm": "[插图]第三部广播纪元7年，程心艾AA说",
    "pr": 74,
    "rt": 30,
    "ts": 1727660516749,
    "rn": 31,
    "sg": "991118cc229871a5442993ecb08b5d2844d7f001dbad9a9bc7b2ecf73dc8db7e",
    "ct": 1727660516,
    "ps": "b1d32a307a4c3259g016b67",
    "pc": "080327b07a4c3259g018787",
}

def convert(curl_command):
    """提取headers与cookies"""
    # 提取 headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    cookie_string = headers.pop('cookie', '')
    for cookie in cookie_string.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
