import os

import Luno.libs.utils.toolUtils as utils

import Luno.libs.globals.Global_Live as Global_Live
import Luno.libs.globals.Global_BackTest as Global_BackTest




def print_status(           
                config, 
                Bot_Name, 
                askPrice, 
                bidPrice, 
                trade_status, 
                capital, 
                Risk_mode, 
                BackTest_Active, 
                BackTest_Active_print_statement, 
                EXTERNAL_DEGREES
                ):

    """ 10 print status to console """



    BackTest_Active = config["BackTest_Active"]

    currency_pair = config["LUNO_active_bots"][Bot_Name]["currency_pair"]

    EXTER = EXTERNAL_DEGREES

    if BackTest_Active == True:



        if currency_pair == 'ETHZAR':

            ask_range_split = Global_BackTest.data_calc[Bot_Name]["ask_range"]
            bid_range_split = Global_BackTest.data_calc[Bot_Name]["bid_range"]
            degrees = Global_BackTest.data_calc[Bot_Name]["degrees"]
            time = Global_BackTest.time
            day = Global_BackTest.day

        elif currency_pair == 'XRPZAR':

            ask_range_split = float(Global_BackTest.data_calc[Bot_Name]["ask_range"]) * float(1000)
            bid_range_split = float(Global_BackTest.data_calc[Bot_Name]["bid_range"]) * float(1000)
            degrees = float(Global_BackTest.data_calc[Bot_Name]["degrees"]) * float(1000)
            EXTERNAL_DEGREES = float(EXTER) * float(1000)
            time = Global_BackTest.time
            day = Global_BackTest.day





        if BackTest_Active_print_statement != False:

            text_1 = str(day) + ' | ' +  str(time) + ' |||| Active_Trading : ' + Bot_Name + ' || Risk: ' + Risk_mode + ' || ask: ' + str(askPrice)
            text_2 = ' -- bid: ' + str(bidPrice) + ' || ask_range: ' + str(ask_range_split) + ' -- bid_range: ' + str(bid_range_split) + ' || Bot_status: ' + str(trade_status)
            text_3 = ' || LONG_Lin_Deg: ' + str(EXTERNAL_DEGREES).split('.')[0] + ' || SHORT_Lin_Deg: ' + str(degrees).split('.')[0] + ' capital: R' + str(capital).split('.')[0]

            update_text = text_1 + text_2 + text_3

            print('\r' + update_text, end="            ", flush=True)

    else:

        ask_range_split = Global_Live.data_calc[Bot_Name]["ask_range"]
        bid_range_split = Global_Live.data_calc[Bot_Name]["bid_range"]
        degrees = Global_Live.data_calc[Bot_Name]["degrees"]
        time = Global_Live.time
        day = Global_Live.day



        text_1 = day + ' | ' +  time + ' |||| Active_Trading : ' + Bot_Name + ' || Risk: ' + Risk_mode + ' || ask: ' + str(askPrice)
        text_2 = ' -- bid: ' + str(bidPrice) + ' || ask_range: ' + str(ask_range_split) + ' -- bid_range: ' + str(bid_range_split) + ' || Bot_status: ' + str(trade_status)
        text_3 = ' || LONG_Lin_Deg: ' + str(EXTERNAL_DEGREES).split('.')[0] + ' || SHORT_Lin_Deg: ' + str(degrees).split('.')[0] + ' capital: R' + str(capital).split('.')[0]

        update_text = text_1 + text_2 + text_3

        print(update_text)


















def startup_wallet(config, bot_name, currencyPair):
    """ checks and writes to wallet at first time startup """

    TurtleTurtle_path = config["TurtleTurtle_path"]
    BackTest_start_money = float(config["BackTest_start_money"])

    data_dir = TurtleTurtle_path + '/data/bot_data/wallets/' + str(bot_name) + '_wallet.json'

    if currencyPair == 'ETHZAR':

        if os.path.exists(data_dir) != True:

            wally_data = {}
            wally_data['trade_capital'] = BackTest_start_money
            wally_data['trade_capital_coin'] = 0
            wally_data['limit'] = 42500
            wally_data['trade_status'] = 'buy_low'
            wally_data['market_degrees'] = 0

            utils.write_to_json(data_dir, wally_data)

    elif currencyPair == 'XRPZAR':

        if os.path.exists(data_dir) != True:

            wally_data = {}
            wally_data['trade_capital'] = BackTest_start_money
            wally_data['trade_capital_coin'] = 0
            wally_data['limit'] = 12.1
            wally_data['trade_status'] = 'buy_low'
            wally_data['market_degrees'] = 0

            utils.write_to_json(data_dir, wally_data)


    elif currencyPair == 'USDCZAR':

        if os.path.exists(data_dir) != True:

            wally_data = {}
            wally_data['trade_capital'] = BackTest_start_money
            wally_data['trade_capital_coin'] = 0
            wally_data['limit'] = 15.30
            wally_data['trade_status'] = 'buy_low'
            wally_data['market_degrees'] = 0

            utils.write_to_json(data_dir, wally_data)


    elif currencyPair == 'SOLZAR':

        if os.path.exists(data_dir) != True:

            wally_data = {}
            wally_data['trade_capital'] = BackTest_start_money
            wally_data['trade_capital_coin'] = 0
            wally_data['limit'] = 1400
            wally_data['trade_status'] = 'buy_low'
            wally_data['market_degrees'] = 0

            utils.write_to_json(data_dir, wally_data)





    wally_data = utils.read_json(data_dir)

    return(wally_data)











if __name__ == '__main__':

    # linear regression test

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
    y = [12.73, 5.73, 10.73, 12.73, 14.73, 12.73, 16.73, 12.73, 12.73, 15.73,] 

