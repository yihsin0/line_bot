from transitions.extensions import GraphMachine
from linebot.models import *
from utils import send_text_message
from utils import send_image_url
from utils import send_button_message
#from utils import movie
from linebot.models import TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

class TocMachine(GraphMachine):
    count=0

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"
    def on_enter_start(self, event):
        reply_token = event.reply_token
        buttons_template1 = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
            title='無聊的話就來找我吧！',
            text='選一個你想做的事！',
            thumbnail_image_url='https://images.pexels.com/photos/3043798/pexels-photo-3043798.jpeg?cs=srgb&dl=person-holding-ball-night-lamp-while-sitting-3043798.jpg&fm=jpg',
            actions=[
                MessageTemplateAction(
                    label='心理測驗',
                    text='心理測驗'
                ),
                MessageTemplateAction(
                    label='金頭腦',
                    text='金頭腦'
                )
            ]    
            )
        )
        send_button_message(reply_token, buttons_template1)
    
    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "心理測驗"
    
    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        #send_text_message(reply_token, "enter state1")
        
        buttons_template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
            title='測試一下你的幼稚程度吧!!',
            text='如果你是童話故事中，想吃掉三隻小豬的大野狼，你認為使用哪一種方法可以容易吃掉他們？',
            thumbnail_image_url='https://images.pexels.com/photos/3043798/pexels-photo-3043798.jpeg?cs=srgb&dl=person-holding-ball-night-lamp-while-sitting-3043798.jpg&fm=jpg',
            actions=[
                MessageTemplateAction(
                    label='用煙把小豬勳到昏倒',
                    text='用煙把小豬勳到昏倒'
                ),
                MessageTemplateAction(
                    label='從煙囪或其他入口偷偷爬進屋',
                    text='從煙囪或其他入口偷偷爬進屋'
                ),
                MessageTemplateAction(
                    label='用槌子把門破壞闖入屋內',
                    text='用槌子把門破壞闖入屋內'
                ),
                MessageTemplateAction(
                    label='模仿豬媽媽的聲音騙小豬開門',
                    text='模仿豬媽媽的聲音騙小豬開門'
                )
            ]    
            )
        )
        send_button_message(reply_token, buttons_template)

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"
    
    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_image_url(reply_token, "https://images.pexels.com/photos/2691784/pexels-photo-2691784.jpeg?cs=srgb&dl=white-and-red-petaled-flowers-close-up-photography-2691784.jpg&fm=jpg")
        self.go_back()
    
    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "用煙把小豬勳到昏倒"
    def on_enter_state3(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "你的幼稚指數99％：你簡直是活在童話世界中，幼稚到了極點 ! 成熟點好嗎~")
        self.go_back()
    
    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "從煙囪或其他入口偷偷爬進屋"
    def on_enter_state4(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "幼稚指數55％：你自知已經半大不小，必須學習獨立自主，了解社會環境有善有惡，並非像童話世界一樣單純。你會在人生的路途中會慢慢的讓自己學習成長。")
        self.go_back()
    
    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "用槌子把門破壞闖入屋內"
    def on_enter_state5(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "你的幼稚指數80％：看來你比較大男人或大女人，表面上很成熟，其實內心是非常幼稚的")
        self.go_back()
    
    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "模仿豬媽媽的聲音騙小豬開門"
    def on_enter_state6(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "你的幼稚指數35％：你心智成熟！好棒棒！")
        self.go_back()

    def is_going_to_chat(self, event):
        text = event.message.text
        return text.lower() == "金頭腦"
    def on_enter_chat(self, event):
        reply_token = event.reply_token
        buttons_template2 = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
            text='題目',
            thumbnail_image_url='https://static.newmobilelife.com/wp-content/uploads/2014/12/LINE03.png',
            actions=[
                MessageTemplateAction(
                    label='Q1',
                    text='q1'
                ),
                MessageTemplateAction(
                    label='Q2',
                    text='q2'
                )
            ]    
            )
        )
        send_button_message(reply_token, buttons_template2)

    def is_going_to_question1(self, event):
        text = event.message.text
        return text.lower() == "q1"
    
    def on_enter_question1(self, event):
        reply_token = event.reply_token
        buttons_template2 = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
            text='Q1',
            thumbnail_image_url='https://i.ibb.co/3RhP6jB/q1.jpg',
            actions=[
                MessageTemplateAction(
                    label='1',
                    text='q1.1'
                ),
                MessageTemplateAction(
                    label='2',
                    text='q1.2'
                ),
                MessageTemplateAction(
                    label='3',
                    text='q1.3'
                ),
                MessageTemplateAction(
                    label='4',
                    text='q1.4'
                )
            ]    
            )
        )
        send_button_message(reply_token, buttons_template2)


    def is_going_to_one1(self, event):
        text = event.message.text
        return text.lower() == "q1.1"
    def on_enter_one1(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "答錯了～若要繼續挑戰請輸入：金頭腦")
        self.go_back2()
    def is_going_to_one2(self, event):
        text = event.message.text
        return text.lower() == "q1.2"
    def on_enter_one2(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "答錯了～若要繼續挑戰請輸入：金頭腦")
        self.go_back2()
    def is_going_to_one3(self, event):
        text = event.message.text
        return text.lower() == "q1.3"
    def on_enter_one3(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "答錯了～ 若要繼續挑戰請輸入：金頭腦")
        self.go_back2()
    def is_going_to_one4(self, event):
        text = event.message.text
        return text.lower() == "q1.4"
    def on_enter_one4(self, event):
        reply_token = event.reply_token
        #count = count + 10
        send_text_message(reply_token, "恭喜答對!! 若要繼續挑戰請輸入：金頭腦")
        self.go_back2()


    def is_going_to_question2(self, event):
        text = event.message.text
        return text.lower() == "q2"
    
    def on_enter_question2(self, event):
        reply_token = event.reply_token
        buttons_template3 = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
            text='Q2',
            thumbnail_image_url='https://i.ibb.co/SrPF2QV/61680001o72r9o05op2o.jpg',
            actions=[
                MessageTemplateAction(
                    label='2',
                    text='q2.1'
                ),
                MessageTemplateAction(
                    label='3',
                    text='q2.2'
                ),
                MessageTemplateAction(
                    label='5',
                    text='q2.3'
                ),
                MessageTemplateAction(
                    label='7',
                    text='q2.4'
                )
            ]    
            )
        )
        send_button_message(reply_token, buttons_template3)

    def is_going_to_two1(self, event):
        text = event.message.text
        return text.lower() == "q2.1"
    def on_enter_two1(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "答錯了～若要繼續挑戰請輸入：金頭腦")
        self.go_back2()
    def is_going_to_two2(self, event):
        text = event.message.text
        return text.lower() == "q2.2"
    def on_enter_two2(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "恭喜答對!! 若要繼續挑戰請輸入：金頭腦")
        self.go_back2()
    def is_going_to_two3(self, event):
        text = event.message.text
        return text.lower() == "q2.3"
    def on_enter_two3(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "答錯了～ 若要繼續挑戰請輸入：金頭腦")
        self.go_back2()
    def is_going_to_two4(self, event):
        text = event.message.text
        return text.lower() == "q2.4"
    def on_enter_two4(self, event):
        reply_token = event.reply_token
        #count = count + 10
        send_text_message(reply_token, "答錯了～ 若要繼續挑戰請輸入：金頭腦")
        self.go_back2()
    
    def is_going_to_back(self, event):
        text = event.message.text
        return text.lower() == "back"
    
    def on_enter_back(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "要輸入start喔！")
        self.go_back()
    