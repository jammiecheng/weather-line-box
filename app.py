from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['e0TENETxrxlIFa1PjqdwN5uiLkmmLllLvKQj+uCK5fEgbJ0CuM/hOOYbshkAArgJ5ANTqS+5Zbng5VuqJnqH1lnvB3E2/M8S6//+ou99DHpie+y/9YOklJ7BVKgEmJ8ONfssYVrrlgsUHxoTh/1I9QdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['8fa6febd36a4efc5d2ea3aa63456abd8'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)