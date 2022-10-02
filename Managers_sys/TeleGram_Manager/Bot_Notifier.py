import os
import telebot

TOKEN_API_KEY = os.getenv("TELEGRAM_TURTLETURTLE_API_KEY")
bot = telebot.TeleBot(TOKEN_API_KEY)
my_id = 1403408899




def send_notification_BUY(config, Bot_Name, askPrice, capital):

    if config["Bot_Notifications"] == True:

        amount = float(askPrice)
        amount_clean = str(round(amount,2))

        capitalfloat = float(capital)
        capital_clean = str(round(capitalfloat,2))

        text_message = '$ Executed BUY : ' + Bot_Name + ' | @ R' + amount_clean + ' | R' + capital_clean
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=text_message)


def send_notification_SELL(config, Bot_Name, bidPrice, capital):

    if config["Bot_Notifications"] == True:

        amount = float(bidPrice)
        amount_clean = str(round(amount,2))

        capitalfloat = float(capital)
        capital_clean = str(round(capitalfloat,2))

        text_message = '$ Executed SELL : ' + Bot_Name + ' | @ R' + amount_clean + ' | R' + capital_clean
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=text_message)




def send_notification_Warning(config, Bot_Name, bidPrice, capital):

    if config["Bot_Notifications"] == True:

        amount = float(bidPrice)
        amount_clean = str(round(amount,2))

        capitalfloat = float(capital)
        capital_clean = str(round(capitalfloat,2))

        text_message = '$ WARNING - Bellow stop loss : ' + Bot_Name + ' | @ R' + amount_clean + ' | R' + capital_clean
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=text_message)




def send_notification_EmergencyExit(config, Bot_Name, bidPrice, capital):

    if config["Bot_Notifications"] == True:

        amount = float(bidPrice)
        amount_clean = str(round(amount,2))

        capitalfloat = float(capital)
        capital_clean = str(round(capitalfloat,2))

        text_message = '$ Executed EMERGENCY EXIT : ' + Bot_Name + ' | @ R' + amount_clean + ' | R' + capital_clean
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=text_message)



def SHORT_direction(config, askPrice, bidPrice, data):

    if config["Bot_Notifications"] == True:

        description = data["SHORT_DEGREE"]["description"]
        degree = data["SHORT_DEGREE"]["degree"]

        text_message = 'Day_Linear_Regression : ' + '\n\n' + description + '\n\nDeg: ' + str(round(degree,2))
        text_02 = '\n\nASK : ' + str(askPrice) + '\nBID : ' + str(bidPrice)
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=text_message + text_02)


def LONG_direction(config, askPrice, bidPrice, data):

    if config["Bot_Notifications"] == True:

        description = data["EXTERNAL_DEGREES"]["description"]
        degree = data["EXTERNAL_DEGREES"]["degree"]

        text_message = 'Two_Day_Linear_Regression : ' + '\n\n' + description + '\n\nDeg: ' + str(round(degree,2))
        text_02 = '\n\nASK : ' + str(askPrice) + '\nBID : ' + str(bidPrice)
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=text_message + text_02)


def Whale_alert(config, notification, quick_details):
    """ sends Notification for whales """

    if config["Bot_Notifications"] == True:

        msg = quick_details
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=msg)



def Arbitrage_Alert_CoinBase(config, text):
    """ Sends Notification for Arbitrage oppertunity """

    if config["Bot_Notifications"] == True:

        msg = text
        bot.send_message(chat_id=my_id, allow_sending_without_reply=True, text=msg)




if __name__ == '__main__':

    Bot_Name = 'Bot_AAA'
    askPrice = 48500
    capital = 10500


    send_notification_BUY( Bot_Name, askPrice, capital)