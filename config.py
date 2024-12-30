# config.py 自定义配置
import os
import re

"""
github action部署或本地部署
从环境变量获取值,如果不存在使用默认本地值
每一次代表30秒，比如你想刷1个小时这里填120，你只需要签到这里填2次
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM', '120'))
# pushplus or telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# push-plus
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# 复制的curl_bath命令
curl_str = os.getenv('WXREAD_CURL')

# 对应替换
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
    'wr_skey': '1yl_zsK9',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=f1186722c484403691efb6fb7a87ab01',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'pac_uid=0_0c7dc76933357; iip=0; _qimei_uuid42=184170f260a100c761caea05ee40b0962cabc59681; _qimei_q36=; _qimei_h38=24b1969561caea05ee40b09602000004d18417; wr_gid=296444248; wr_pf=0; wr_localvid=b49320808106fa6a8b49ca6; wr_name=%E6%B8%B8%E9%BE%99; wr_gender=1; _clck=zq4pnj|1|fmw|0; suid=user_0_0c7dc76933357; pgv_pvid=3904711160; RK=Y28p1Uo3nZ; ptcz=d4ae0de5f7e34c0fa739c35b47638e7b8ad33e13c32964233b66ebff78b7abc1; wr_vid=275752616; wr_rt=web%40qAC2602vcB8SNydPTZs_AL; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FZ6uRYmvbnrqpDmwAlnkWBDQOvic7M3M93ykvbiaTA70XzSDXulm1xMMudyoHPb5hruMA7p7bgkYOaiaG3JZaDQLQH2X82uteTsHEVUD6Ib5GmE%2F132; wr_fp=1296956703; _qimei_fingerprint=f070808fc45d2ba9d06a87b3707fb583; wr_theme=white; wr_skey=1yl_zsK9',
    'dnt': '1',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/ce032b305a9bc1ce0b0dd2ak8f132430178f14e45fce0f7',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': 'f1186722c484403691efb6fb7a87ab01-b0438caee6196b73',
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
