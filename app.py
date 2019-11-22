from config import config

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort, render_template, send_from_directory, make_response
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# ~ get channel_secret and channel_access_token from config.py~
line_bot_api = LineBotApi(config['LINE_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(config['LINE_CHANNEL_SECRET'])

# ~sample code'callback'~
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
def message_text(event):
    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text=event.message.text+'(VScode)'),
            TextSendMessage(text='(測試ing)')
        ]
    )


# ~website~
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# ~AJAX POST~
@app.route('/ajax', methods=['POST'])
def get_ajax():
    data = request.form
    print(data)
    resp = make_response(json.dumps(data))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'



    return resp


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
