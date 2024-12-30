

***
## 操作步骤（v3.0） 🛠️

### 1. 抓包准备（适合本地运行）

脚本逻辑还是比较简单的，`main.py`与`push.py`代码不需要改动。在微信阅读官网 [微信读书](https://weread.qq.com/) 搜索【三体】点开阅读点击下一页进行抓包，抓到`read`接口 `https://weread.qq.com/web/book/read`，如果返回格式正常（如：

```json
{
  "succ": 1,
  "synckey": 564589834
}
```

右键复制为Bash格式（Action部署到这里即可）；然后在 [Convert](https://curlconverter.com/python/) 转化为Python脚本，复制需要的headers与cookies字段替换到`config.py`（data字段保留），运行`main.py`即可，依赖自行安装。

### 2. GitHub Action部署运行（GitHub运行）


- Fork这个仓库，在仓库 **Settings** -> 左侧列表中的 **Secrets and variables** -> **Actions**，然后在右侧的 **Repository secrets** 中添加如下值：
  - `WXREAD_CURL`：复制read接口转换为bath的数据。
  - `PUSH_METHOD`：推送方法，可以填写你想使用的推送方式（pushplus或telegram）。
  - `PUSHPLUS_TOKEN`/`TELEGRAM_BOT_TOKEN`&`TELEGRAM_CHAT_ID`: 推送key值。
  
- 在 **Variables** 部分，最下方添加变量：
  - `READ_NUM`：设定每次阅读的目标次数。

- 释义如下：

| Key                   | Value                                  | 说明                    |
|-----------------------|----------------------------------------|-----------------------|
| `WXREAD_CURL`           | 抓到的read接口的curl_bash命令 (必填)             | 必须提供有效的指令             |
| `READ_NUM`            | 阅读时长，每次代表30秒(可选)                       | 控制阅读时长，默认60分钟         |
| `PUSH_METHOD`         | 推送方式，可选值为 `pushplus` 或 `telegram` (可选) | 选择推送方式，默认不推送          |
| `PUSHPLUS_TOKEN`      | pushplus token (可选)                    | 仅在选择 `pushplus` 时需要填写 |
| `TELEGRAM_BOT_TOKEN`&`TELEGRAM_CHAT_ID` | telegram bot token&telegram chat id (可选)               | 仅在选择 `telegram` 时需要填写 |


<img src="https://github.com/user-attachments/assets/69694f8a-e6be-4c3a-820a-ac79ec2a22e5" alt="微信截图_17309442135616" width="800px"/>

### 3. 服务器运行（可选）

在你的服务器上有Python运行环境即可，使用`cron`定义自动运行。（如：

```bash
0 2 * * * /www/server/pyproject_env/wxread_venv/bin/python3 /root/wxread/main.py >> /root/wxread/logs/$(date +\%y-\%m.\%d)_sout.log 2>&1
```

意思为：【在每天两点时刻使用python所在位置编译器运行某个路径下的`main.py`脚本，同时将输出按每天的日期格式输出到对应日志中】可供参考）。


***
## 代理配置说明 🌐

如果你需要使用代理来确保消息推送的可靠性（特别是使用 Telegram 推送时），可以通过以下方式配置：

### 本地运行时：
在系统中设置环境变量：
```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

### 使用 crontab 运行时：
在 crontab 命令前添加代理设置：
```bash
30 0 * * * http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 /usr/bin/python3 /path/to/your/main.py >> /path/to/logs/$(date +\%y-\%m.\%d)_sout.log 2>&1
```

### GitHub Actions 中：
在仓库的 Secrets 中添加：
- `http_proxy`: 你的 HTTP 代理地址
- `https_proxy`: 你的 HTTPS 代理地址

然后在 workflow 文件中使用这些环境变量。

***
## 字段解释 🔍

| 字段 | 示例值 | 解释 |
| --- | --- | --- |
| `appId` | `"wbxxxxxxxxxxxxxxxxxxxxxxxx"` | 应用的唯一标识符。 |
| `b` | `"ce032b305a9bc1ce0b0dd2a"` | 书籍或章节的唯一标识符。 |
| `c` | `"0723244023c072b030ba601"` | 内容的唯一标识符，可能是页面或具体段落。 |
| `ci` | `60` | 章节或部分的索引。 |
| `co` | `336` | 内容的具体位置或页码。 |
| `sm` | `"[插图]威慑纪元61年，执剑人在一棵巨树"` | 当前阅读的内容描述或摘要。 |
| `pr` | `65` | 页码或段落索引。 |
| `rt` | `88` | 阅读时长或阅读进度。 |
| `ts` | `1727580815581` | 时间戳，表示请求发送的具体时间（毫秒级）。 |
| `rn` | `114` | 随机数或请求编号，用于标识唯一的请求。 |
| `sg` | `"bfdf7de2fe1673546ca079e2f02b79b937901ef789ed5ae16e7b43fb9e22e724"` | 安全签名，用于验证请求的合法性和完整性。 |
| `ct` | `1727580815` | 时间戳，表示请求发送的具体时间（秒级）。 |
| `ps` | `"xxxxxxxxxxxxxxxxxxxxxxxx"` | 用户标识符或会话标识符，用于追踪用户或会话。 |
| `pc` | `"xxxxxxxxxxxxxxxxxxxxxxxx"` | 设备标识符或客户端标识符，用于标识用户的设备或客户端。 |
| `s` | `"fadcb9de"` | 校验和或哈希值，用于验证请求数据的完整性。 |

![Video Title](https://www.youtube.com/watch?v=FGO5VfkK3pI)
