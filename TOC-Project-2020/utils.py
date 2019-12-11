import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
"""import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve"""


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)



def send_text_message(reply_token,text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"



def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
def send_button_message(reply_token, buttons):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, buttons)

"""def movie():
    target_url = 'https://movies.yahoo.com.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.movielist_info h1 a')):
        if index == 20:
            return content       
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
    return content"""

