import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "state1", "state2","state3","state4","state5","state6","start","chat","question1","back","one1","one2","one3","one4","two1","two2","two3","two4","question2"],
    transitions=[
        {"trigger": "advance","source": "start","dest": "state1","conditions": "is_going_to_state1",},
        {"trigger": "advance","source": "user","dest": "start","conditions": "is_going_to_start",},
        {"trigger": "advance","source": "start","dest": "state2","conditions": "is_going_to_state2",},
        {"trigger": "advance","source": "state1","dest": "state3","conditions": "is_going_to_state3",},
        {"trigger": "advance","source": "state1","dest": "state4","conditions": "is_going_to_state4",},
        {"trigger": "advance","source": "state1","dest": "state5","conditions": "is_going_to_state5",},
        {"trigger": "advance","source": "state1","dest": "state6","conditions": "is_going_to_state6",},
        {"trigger": "advance","source": "start","dest": "chat","conditions": "is_going_to_chat",},
        {"trigger": "advance","source": "chat","dest": "question1","conditions": "is_going_to_question1",},
        {"trigger": "advance","source": "chat","dest": "question2","conditions": "is_going_to_question2",},
        {"trigger": "advance","source": "chat","dest": "back","conditions": "is_going_to_back",},
        {"trigger": "advance","source": "question1","dest": "one1","conditions": "is_going_to_one1",},
        {"trigger": "advance","source": "question1","dest": "one2","conditions": "is_going_to_one2",},
        {"trigger": "advance","source": "question1","dest": "one3","conditions": "is_going_to_one3",},
        {"trigger": "advance","source": "question1","dest": "one4","conditions": "is_going_to_one4",},
        {"trigger": "advance","source": "question2","dest": "two1","conditions": "is_going_to_two1",},
        {"trigger": "advance","source": "question2","dest": "two2","conditions": "is_going_to_two2",},
        {"trigger": "advance","source": "question2","dest": "two3","conditions": "is_going_to_two3",},
        {"trigger": "advance","source": "question2","dest": "two4","conditions": "is_going_to_two4",},
        {"trigger": "go_back2","source": ["one1","one2","one3","one4","two1","two2","two3","two4"],"dest": "start"},
        {"trigger": "go_back", "source": ["state1", "state2", "state3","state4","state5","state6","back","one1","question1","chat"], "dest": "user"},
        

    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():

    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
