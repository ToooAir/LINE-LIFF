from config import config
import alchemyFunc
import lineModel

import os
import sys
import re

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
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)

app = Flask(__name__)

# config here
line_bot_api = LineBotApi(config['LINE_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(config['LINE_CHANNEL_SECRET'])
imageSaveDir = 'static/uploadImage/'

# messaging API here
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    if(re.match("^[0-9]*$", event.message.text)):
        # todo 檢查不存在的號碼 檢查完才查詢
        userid = event.message.text
        user = alchemyFunc.searchUser(userid)
        flex = lineModel.flexmessage(user)
        line_bot_api.reply_message(
            event.reply_token, [
                flex,
            ]
        )
    else:
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text=event.message.text+"(VScode)"),
                TextSendMessage(text="(傳送的非數字無法查詢)")
            ]
        )


# website here
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/check")
def check():
    return render_template("check.html")


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

# AJAX POST
@app.route("/signup", methods=["POST"])
def signup():
    data = request.form

    image = request.files["images"]
    filename = image.filename
    if(filename != ""):
        image.save(os.path.join(imageSaveDir, data["user"]))

    if(alchemyFunc.checkRepeat(data["user"])):
        alchemyFunc.editUser(
            data["user"], data["name"], data["email"], data["facebook"], data["selfIntro"])
        resp = make_response("修改")
        resp.status_code = 200
        resp.headers["Access-Control-Allow-Origin"] = "*"
    else:
        alchemyFunc.addUser(
            data["user"], data["name"], data["email"], data["facebook"], data["selfIntro"])
        resp = make_response("報名")
        resp.status_code = 200
        resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp


@app.route("/getNumber", methods=["POST"])
def getNumber():
    data = request.form
    print(data["user"])
    if(alchemyFunc.checkRepeat(data["user"])):
        resp = make_response(json.dumps(
            alchemyFunc.searchUserID(data["user"])))
        resp.status_code = 200
        resp.headers["Access-Control-Allow-Origin"] = "*"
    else:
        resp = make_response("還沒報名啦")
        resp.status_code = 200
        resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp


@app.route("/getStatus", methods=["POST"])
def getStatus():
    data = request.form
    if(alchemyFunc.checkRepeat(data["user"])):
        myself = alchemyFunc.searchMyself(data["user"])
        resp = make_response(myself)
        resp.status_code = 200
        resp.headers["Access-Control-Allow-Origin"] = "*"
    else:
        noUser = {"name":"","email":"","facebook":"","intro":"","status":"報名"}
        resp = make_response(noUser)
        resp.status_code = 200
        resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage="Usage: python " + __file__ + "[--port <port>] [--help]"
    )
    arg_parser.add_argument("-p", "--port", default=8000, help="port")
    arg_parser.add_argument("-d", "--debug", default=False, help="debug")
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
