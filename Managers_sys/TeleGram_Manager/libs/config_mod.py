import os
import yaml
import pprint
import random

import Managers_sys.TeleGram_Manager.utils.general_utils as general_utils
import utils.ToolUtils as toolUtils
import Trading_sys.Valr.libs.utils.collect_historical_data as collect_data

import Trading_sys.Valr.libs.utils.sales as SALES




TurtleTurtle_path = str(os.getenv("Turtle"))
config_path = TurtleTurtle_path + '/config.yaml'



fun_list = ['🧸','🧟‍♂️','🧟‍♀️','🧛‍♂️','🧛‍♀️','🧝‍♂️','🧙‍♂️','🦹‍♂️','🦸‍♂️','👤', '👻','💀','☠️','👽','👾','🤖','🎃','🤠','😈','💩','🕵️‍♀️','💂‍♂️','🙃','🤑🖕','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐸','🐲']




def bot_change_status(input, bot, message):
    """ This changes the bots trading mode /hold/play/trade , cmd = /change_status bot_AAA hold """

    config = general_utils.yaml_config(config_path)

    bot_name = input.split(' ')[1]
    status = input.split(' ')[2]

    bot_list = config["VALR_active_bots"]

    emoticon_choice = random.choice(fun_list)

    if bot_name in bot_list:

        bot_list[bot_name]["status"] = str(status.lower())

        with open(config_path, 'w') as outfile:
            yaml.dump(config, outfile, default_flow_style=False)

        text = emoticon_choice + bot_name + ' | changed status to : ' + status.lower()
        bot.send_message(message.chat.id, text)

    else:
        text_error = bot_name + ' | Does not exist'
        bot.send_message(message.chat.id, text_error)





def bot_change_risk(input, bot, message):
    """ This changes the bots trading mode /hold/play/trade , cmd = /change_status bot_AAA hold """

    config = general_utils.yaml_config(config_path)

    bot_name = input.split(' ')[1]
    risk = input.split(' ')[2]

    bot_list = config["VALR_active_bots"]

    if bot_name in bot_list:

        emoticon_choice = random.choice(fun_list)

        bot_list[bot_name]["Risk_mode"] = str(risk.lower())

        with open(config_path, 'w') as outfile:
            yaml.dump(config, outfile, default_flow_style=False)


        text = emoticon_choice + bot_name + ' | changed status to : ' + risk.lower()
        bot.send_message(message.chat.id, text)

    else:
        text_error = bot_name + ' | Does not exist'
        bot.send_message(message.chat.id, text_error)



def get_bots(input, bot, message):
    """ This changes the bots trading mode /hold/play/trade , cmd = /change_status bot_AAA hold """

    config = general_utils.yaml_config(config_path)
    
    bot_list = config["VALR_active_bots"]
    pprint.pprint(bot_list)

    for i in bot_list:




        bot_name = i
        status = bot_list[bot_name]["status"]
        currency_pair = bot_list[bot_name]["currency_pair"]
        account = bot_list[bot_name]["account"]
        Risk_mode = bot_list[bot_name]["Risk_mode"]
        Plot_graph = bot_list[bot_name]["Plot_graph"]

        emoticon_choice = random.choice(fun_list)

        text_01 = emoticon_choice + bot_name + ' Data:' + '\n\nStatus: ' + status + '\nCurrency Pair: ' + currency_pair + '\nAccount: ' + str(account)
        text_02 = '\nRisk Mode: ' + Risk_mode + '\nPlot Graph: ' + str(Plot_graph) + '\n '



        bot.send_message(message.chat.id, str(text_01 + text_02))




def get_wallet(input, bot, message):
    """ This changes the bots trading mode /hold/play/trade , cmd = /change_status bot_AAA hold """

    config = general_utils.yaml_config(config_path)
    wallet_path = config["TurtleTurtle_wallets_path"]

    bot_name = input.split(' ')[1]

    data = toolUtils.read_json(wallet_path + '/' + bot_name + '_wallet.json')
    pprint.pprint(data)

    trade_capital = data["trade_capital"]
    trade_capital_coin = data["trade_capital_coin"]
    limit = data["limit"]
    trade_status = data["trade_status"]
    market_degrees = data["market_degrees"]

    emoticon_choice = random.choice(fun_list)

    text_01 = emoticon_choice + bot_name + ' Wallet:' + '\n\nTrade Capital: ' + str(round(trade_capital,2)) + '\nTrade Capital Coin: ' + str(round(trade_capital_coin,2))
    text_02 = '\nLimit: ' + str(round(limit,2)) + '\nTrade Status: ' +  trade_status + '\nMarket Direction: ' + str(round(market_degrees,2))

    bot.send_message(message.chat.id, str(text_01 + text_02))



def get_direction(input, bot, message):
    """ This changes the bots trading mode /hold/play/trade , cmd = /change_status bot_AAA hold """

    config = general_utils.yaml_config(config_path)
    TurtleTurtle_path = config["TurtleTurtle_path"]

    data = toolUtils.read_json(TurtleTurtle_path + '/data/active_stats/general/market_direction/VALR_ETH_market.json')
    pprint.pprint(data)

    day_description = data["SHORT_DEGREE"]["description"]
    day_deg = data["SHORT_DEGREE"]["degree"]

    two_day_description = data["EXTERNAL_DEGREES"]["description"]
    two_day_deg = data["EXTERNAL_DEGREES"]["degree"]

    emoticon_choice = random.choice(fun_list)

    text_01 = emoticon_choice + 'Day_Linear_Regression : ' + '\n\n' + day_description + '\n' + str(round(day_deg, 2))
    text_02 = emoticon_choice + 'Two_Day_Linear_Regression : ' + '\n\n' + two_day_description + '\n' + str(round(two_day_deg, 2))

    text = text_01 + '\n\n' + text_02

    bot.send_message(message.chat.id, str(text_01))
    bot.send_message(message.chat.id, str(text_02))



def bot_change_limit(input, bot, message):
    """ This sets the bots wallet limit that it will buy or sell at """

    config = general_utils.yaml_config(config_path)
    wallet_path = config["TurtleTurtle_wallets_path"]

    bot_name = input.split(' ')[1]
    limit = input.split(' ')[2]

    data = toolUtils.read_json(wallet_path + '/' + bot_name + '_wallet.json')
    pprint.pprint(data)

    data["limit"] = float(limit)
    toolUtils.write_to_json(wallet_path + '/' + bot_name + '_wallet.json', data)

    emoticon_choice = random.choice(fun_list)

    text = emoticon_choice + bot_name + ' | changed limit to : ' + str(limit)

    bot.send_message(message.chat.id, str(text))



def get_market(input, bot, message):
    """ This returns the current market data """

    config = general_utils.yaml_config(config_path)  

    collected_days = collect_data.collect_historical_data(config, 'valr', year_input=['2022'])[2]
    collected_days.sort()
    day = collected_days[-1:][0]

    data = toolUtils.read_json(day)
    for i in data:

        for d in data[i]:

            coin = 'XRPZAR'
            ask = data[i]['XRPZAR']["askPrice"]
            bid = data[i]['XRPZAR']["bidPrice"]

            XRPZAR = coin + ' | Ask: ' + str(ask).ljust(2) + ' | Bid: ' + str(bid).ljust(2)

            coin = 'BTCZAR'
            ask = data[i]['BTCZAR']["askPrice"]
            bid = data[i]['BTCZAR']["bidPrice"]

            BTCZAR = coin + ' | Ask: ' + str(ask).ljust(2) + ' | Bid: ' + str(bid).ljust(2)

            coin = 'ETHZAR'
            ask = data[i]['ETHZAR']["askPrice"]
            bid = data[i]['ETHZAR']["bidPrice"]

            ETHZAR = coin + ' | Ask: ' + str(ask).ljust(2) + ' | Bid: ' + str(bid).ljust(2)


    text_01 = 'Current_Prices - ' + str(i).split('.')[0]
    text_02 = '\n\n'+XRPZAR + '\n\n'+BTCZAR +  '\n\n'+ETHZAR

    msg = text_01 + str(text_02)

    print(msg)
    bot.send_message(message.chat.id, str(msg))






def get_profits(input, bot, message):
    """ Gets all current profits/losses from bots """

    data = SALES.get_profits()

    print(data)

    bot.send_message(message.chat.id, str(data))

















if __name__ == '__main__':


    # input = '/change_status bot_AAA hOld'
    # get_bots(input)
    
    input = ''
    bot = ''
    message = ''

    get_market(input, bot, message)

