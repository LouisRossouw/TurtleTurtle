import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import telebot
import random

import time
import Managers_sys.TeleGram_Manager.libs.config_mod as BOT

TOKEN_API_KEY = os.getenv("TELEGRAM_TURTLETURTLE_API_KEY")
bot = telebot.TeleBot(TOKEN_API_KEY, parse_mode=None)

admin_name = "Louis"
admin_username = "Kpow_636"
admin_last_name = "Rossouw"
my_id = 1403408899

fun_list = ['🧸','🧟‍♂️','🧟‍♀️','🧛‍♂️','🧛‍♀️','🧝‍♂️','🧙‍♂️','🦹‍♂️','🦸‍♂️','👤', '👻','💀','☠️','👽','👾','🤖','🎃','🤠','😈','💩','🕵️‍♀️','💂‍♂️','🙃','🤑🖕','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐸','🐲']


def check_usr(message):

    usr_name = message.from_user.first_name
    usr_surname = message.from_user.last_name
    usr_user_name = message.from_user.username     

    usr_id = message.from_user.id
    usr_is_bot = message.from_user.is_bot

    usr_language = message.from_user.language_code
    usr_content_type = message.content_type
    usr_text = message.text

    if usr_name != admin_name:
        if usr_surname != admin_last_name:
            if usr_user_name != admin_username:
                if usr_id != my_id:
                    IS_ADMIN = False

    if usr_name == admin_name:
        if usr_surname == admin_last_name:
            if usr_user_name == admin_username:
                if usr_id == my_id:
                    IS_ADMIN = True

    if IS_ADMIN != True:

        emoticon_choice = random.choice(fun_list)

        text_line_1 = emoticon_choice + 'WARNING: \n\n* Unrecognized user interacted with TurtleTurtle *'
        text_line_2 = '\n\nUSR Details:'
        text_line_3 = '\n\nusr_name: ' + str(usr_name) + '\nusr_surname: ' + str(usr_surname) + '\nusr_nickname: ' + str(usr_user_name)
        text_line_4 = '\n\nusr_id: ' + str(usr_id) + '\nusr_is_bot: ' + str(usr_is_bot) + '\nusr_language: ' + str(usr_language) + '\n\nusr_content_type: ' + str(usr_content_type) + '\nText: ' + str(usr_text)

        # To Admin / Owner of TurtleTurtle
        text_msg = text_line_1 + text_line_2 + text_line_3 + text_line_4
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=text_msg)

        # To Un-Authorized USER
        text_warning = emoticon_choice + str(usr_name) + '_' + str(usr_surname) + '\n\n .. \n\nYou are not authorized to use this Bot'
        bot.send_message(chat_id=usr_id, allow_sending_without_reply=True, text=text_warning)

    elif IS_ADMIN == True:
        pass


    return IS_ADMIN

    



def Bot_Manager_Run():
    """ Telegram Bot Manager for TurtleTurtle crypto trader """



    @bot.message_handler(commands=['start'])
    def start_chat(message):

        emoticon_choice = random.choice(fun_list)

        # Check if Admin 
        is_admin = check_usr(message)
        if is_admin != True:
            pass
        else:
            bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=emoticon_choice + "TurtleTurtle_bot v2.0.0 - crypto trader")
        


    @bot.message_handler(commands=['cmds'])
    def cmds(message):

        # Check if Admin
        is_admin = check_usr(message)
        if is_admin != True:
            pass
        else:
            text_01 = "/start\n\n/set_status : 'trade','hold','play' \n\n/set_risk : 'low','mid','HIGH','buy','sell \n\n/get_bots : gets all bots config info"
            text_02 = "\n\n/get_wallet : get bot wallet info | /get_wallet bot_BBB' \n\n/get_direction : get markets direction, both 1 day and 2days '\n\n/market"
            msg = text_01 + text_02
            bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=msg)










# Auto response to all none command messages
    @bot.message_handler(func=lambda m: True)
    def echo_all(message):

        # Check if Admin
        is_admin = check_usr(message)
        if is_admin != True:
            pass
        else:

            content_type = message.content_type
            usr_text = message.text

            if content_type == 'text':

                if "/set_status" in usr_text:
                    BOT.bot_change_status(usr_text, bot, message)

                elif "/set_risk" in usr_text:
                    BOT.bot_change_risk(usr_text, bot, message)

                elif "/set_limit" in usr_text:
                    BOT.bot_change_limit(usr_text, bot, message)

                elif "/get_bots" in usr_text:
                    BOT.get_bots(usr_text, bot, message)

                elif "/get_wallet" in usr_text:
                    BOT.get_wallet(usr_text, bot, message)

                elif "/get_direction" in usr_text:
                    BOT.get_direction(usr_text, bot, message)

                elif "/market" in usr_text:
                    BOT.get_market(usr_text, bot, message)

                elif "/profits" in usr_text:
                    BOT.get_profits(usr_text, bot, message)


    bot.infinity_polling()



while True:
    try:

        # bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text='starting up')
        Bot_Manager_Run()
        
    except Exception as e:
        print(e)
    time.sleep(5)




# if __name__ == '__main__':

#     while True:
#         try:
#             run_bot()
            
#         except Exception:
#             pass
#         time.sleep(5)




