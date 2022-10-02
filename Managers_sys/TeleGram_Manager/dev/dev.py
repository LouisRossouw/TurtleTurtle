import os
import json
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


API_KEY = "5142483492:AAHIYVn2NbnzWeO6aXTfUiLIaCjodElikuQ"
test = "D:/Dropbox/Roblox/deliverables/25_03_2022/anim/rbx_020_terra_anim_v004.mp4"
path = "C:/Work/Projects/bot/test.json"
usr_id = 1403408899
bot = telebot.TeleBot(API_KEY)


text = "HELLO THERE: \nD:/Dropbox/Roblox/deliverables/25_03_2022/anim/rbx_020_terra_anim_v004.mp4 \nthis is a long piece of text"



def send_msg(text, call):
    bot.send_message(call.id, text)


def get_bots():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    buttons = markup.add(
                InlineKeyboardButton("bot_AAA", callback_data="bot_AAA"),
                InlineKeyboardButton("bot_BBB", callback_data="bot_BBB"),
                InlineKeyboardButton("bot_CCC", callback_data="bot_CCC"),
                )
    return markup



def bot_settings():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    buttons = markup.add(
                InlineKeyboardButton("wallet", callback_data="wallet"),
                InlineKeyboardButton("settings", callback_data="settings"),
                )
    return markup



def cmds():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    buttons = markup.add(
                InlineKeyboardButton("My_Bots", callback_data="My_Bots"),
                InlineKeyboardButton("Get_Direction", callback_data="Get_Direction"),
                InlineKeyboardButton("TurtleTurtle", callback_data="TurtleTurtle"),
                )
    return markup



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):



    # Main
    if call.data == "My_Bots":
        bot.send_message(usr_id, "Bots:", reply_markup=get_bots())
    elif call.data == "Get_Direction":
        bot.answer_callback_query(call.id, "This is bot_BBB")
    elif call.data == "TurtleTurtle":
        bot.send_message(usr_id, text)



    # My_Bots
    elif call.data == "bot_AAA":
        bot.send_message(usr_id, "bot_AAA Settings:", reply_markup=bot_settings())
    elif call.data == "bot_BBB":
        bot.send_message(usr_id, "bot_BBB Settings:", reply_markup=bot_settings())
    elif call.data == "bot_CCC":
        bot.send_message(usr_id, "bot_CCC Settings:", reply_markup=bot_settings())



    # Bot_Settings
    elif call.data == "wallet":
        bot.answer_callback_query(call.id, "wally")
    elif call.data == "settings":
        bot.answer_callback_query(call.id, "settings")



@bot.message_handler(func=lambda message: True)
def message_handler(message):
    print(message)
    bot.send_message(message.chat.id, "Select Bot to Modify:", reply_markup=cmds())



bot.infinity_polling()