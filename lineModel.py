from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)


def flexmessage(user):
    message = FlexSendMessage(
        alt_text='hello',
        contents={

            "type": "bubble",
            "hero": {
                    "type": "image",
                "url": "https://d17fnq9dkz9hgj.cloudfront.net/uploads/2012/11/152964589-welcome-home-new-cat-632x475.jpg",
                "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "action": {
                            "type": "uri",
                            "uri": "http://linecorp.com/"
                        }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                        {
                            "type": "text",
                            "text": user.name,
                            "weight": "bold",
                            "size": "xxl"
                        },
                    {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "email",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 2
                                            },
                                            {
                                                "type": "text",
                                                "text": user.email,
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "sm",
                                                "flex": 5
                                            }
                                        ]
                                    },
                                {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "facebook",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 2
                                            },
                                            {
                                                "type": "text",
                                                "text": user.facebook,
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "sm",
                                                "flex": 5
                                            }
                                        ]
                                    },
                                {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Intro",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "flex": 2
                                            },
                                            {
                                                "type": "text",
                                                "text": user.intro,
                                                "wrap": True,
                                                "color": "#666666",
                                                "size": "sm",
                                                "flex": 5
                                            }
                                        ]
                                    }
                            ]
                    }
                ]
            }
        }
    )
    return message
