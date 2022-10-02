
import time

import Luno.libs.utils.toolUtils as utils

import Luno.libs.globals.Global_BackTest as Global_BackTest
import Luno.libs.globals.Global_Live as Global_Live

import Luno.libs.utils.calculations as calculations
import Luno.libs.utils.plot as Plotter


import Luno.libs.utils.record_data as record_datas

import Managers_sys.TeleGram_Manager.Bot_Notifier as Bot_Notifier

   

## LOW RISK MODE


def LOW_RISK_TRADING(
                Bot_Name,
                askPrice, 
                bidPrice,
                collect_ask, 
                collect_bid, 
                x_collect_plot,
                count,
                config,
                trade_status,
                wally_json,
                EXTERNAL_DEGREES
                ):

    """ 7 Trading strategy in Development """

    EMA_spread_ask = -10
    EMA_spread_bid = -10
    SMA_spread_long_bid = -10
    collected_data_amount = 2
    long_regression_len = -10
    limit_reg = 10
    limit_sell = 0.5
    limit_buy = 0.5

    
    BackTest_Active = config["BackTest_Active"]
    status = config["LUNO_active_bots"][Bot_Name]["status"]
    acount_id = config["LUNO_active_bots"][Bot_Name]["account"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']
    Bot_Notifications = config["Bot_Notifications"]

    data_dir = config["TurtleTurtle_wallets_path"] + '/' + str(Bot_Name) + '_wallet.json'

    calculated_data = calculations.extra_calculations(
                                                        Bot_Name,
                                                        askPrice, 
                                                        bidPrice,
                                                        collect_ask, 
                                                        collect_bid, 
                                                        x_collect_plot,
                                                        EMA_spread_ask,
                                                        EMA_spread_bid,
                                                        SMA_spread_long_bid,
                                                        collected_data_amount,
                                                        long_regression_len,
                                                        limit_reg,
                                                        limit_sell,
                                                        limit_buy,
                                                        count,
                                                        config,
                                                        EXTERNAL_DEGREES
                                                        )

    if BackTest_Active == True:

        Global = Global_BackTest

    elif BackTest_Active == False:

        Global = Global_Live





    RED_LINE = Global.data_calc[Bot_Name]["output_value_ask"]
    BLUE_LINE = Global.data_calc[Bot_Name]["output_value_bid"]
    YELLOW_LINE = Global.data_calc[Bot_Name]["long_bid"]

    YELLOW_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_long_range"]
    RED_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_range"]
    BLUE_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["bid_range"]

    SHORT_DEGREE = Global.data_calc[Bot_Name]["degrees"]

    ask_dis = float(RED_LINE) - float(YELLOW_LINE)
    bid_dis = float(BLUE_LINE) - float(YELLOW_LINE)


    if float(SHORT_DEGREE) > 50:
        above_30 = True
    else:
        above_30 = False


    # print(RED_LINE, BLUE_LINE, YELLOW_LINE, BLUE_DISTANCE_FROM_LINE)



    if trade_status == 'buy_low':

        if float(RED_LINE) < float(YELLOW_LINE):

            if float(ask_dis) > float(-1000) :

                buy_limit = utils.percent_decrease(limit_buy, float(limit))

                if float(askPrice) <= float(buy_limit):
                                
                    capital = wally_json['trade_capital']
                    # cap = wally_json['trade_status']
                    # wally_json['trade_status'] = 'sell_high'
                    # wally_json['limit'] = float(askPrice)
                    # coi = wally_json['trade_capital_coin'] = (capital) / float(askPrice)

                    # # BUY
                    # if BackTest_Active != True:
                    #     if status == 'trade':
                    #         Balances = VALR.Valr_get_balances(acount_id)
                    #         zar_account = Balances['ZAR']['available']
                    #         eth_account = Balances['ETH']['available']
                    #         coinz = str((float(zar_account) - 500) / float(askPrice))
                    #         VALR.BUY_ZAR_to_ETH(coinz, bot=acount_id)


                    #         time.sleep(10)
                    #         Balances = VALR.Valr_get_balances(acount_id)
                    #         zar_account = Balances['ZAR']['available']
                    #         xrp_account = Balances['XRP']['available']

                    #         wally_json['capital'] = zar_account


                    #         data = {'Bot_Name' : Bot_Name,
                    #                 'account_ID' : acount_id,
                    #                 '------------------------------------------------ ' : None,
                    #                 'trade_type' : 'buy_low',
                    #                 'askPrice' : askPrice,
                    #                 'bidPrice' : bidPrice,
                    #                 '------------------------------------------------ ' : None,
                    #                 'my_zar_balance_in_rands' : zar_account,
                    #                 'my_eth_balance_in_coins' : eth_account,
                    #                 '-------------------------------------------------' : None,
                    #                 'currencypair' : "ETHZAR",
                    #                 'Date' : utils.get_dates()[8],
                    #                 }

                    #         record_datas.buy_sell_status(data, config)


                    # utils.write_to_json(data_dir, wally_json)
                    # print('BUY : ', Bot_Name, askPrice, capital)

                    # # playsound(TurtleTurtle_audio_path + '/tiky_01.wav')

                    # # For plotting
                    # Global.buy_history_cordinates = count
                    # Global.buy_history_amount = float(askPrice)

                    # # Telegram Notifier
                    # Bot_Notifier.send_notification_BUY(config, Bot_Name, askPrice, capital)

                    if BackTest_Active == True:
                        Plotter.plot_graph_every_sale(config, count)




    if trade_status == 'sell_high':

        if float(BLUE_LINE) > float(YELLOW_LINE):

            if float(bid_dis) > float(500):

                if above_30 == False:

                    sell_limit = utils.percent_increase(limit_sell, float(limit))

                    if float(bidPrice) >= float(sell_limit):

                        capital = wally_json['trade_capital']
                        # coin = wally_json['trade_capital_coin']

                        # wally_json['trade_status'] = 'buy_low'  
                        # wally_json['limit'] = float(bidPrice)
                        # wally_json['trade_capital'] = (coin * float(bidPrice))
                        # wally_json['trade_capital_coin'] = 0


                        # # SELL
                        # if BackTest_Active != True:
                        #     if status == 'trade':
                        #         Balances = VALR.Valr_get_balances(acount_id)
                        #         zar_account = Balances['ZAR']['available']
                        #         eth_account = Balances['ETH']['available']
                        #         VALR.SELL_ETH_to_ZAR(eth_account, bot=acount_id)


                        #         time.sleep(10)
                        #         Balances = VALR.Valr_get_balances(acount_id)
                        #         zar_account = Balances['ZAR']['available']
                        #         xrp_account = Balances['XRP']['available']

                        #         wally_json['capital'] = zar_account


                        #         data = {'Bot_Name' : Bot_Name,
                        #                 'account_ID' : acount_id,
                        #                 '------------------------------------------------ ' : None,
                        #                 'trade_type' : 'sell_high|EXIT',
                        #                 'askPrice' : askPrice,
                        #                 'bidPrice' : bidPrice,
                        #                 '------------------------------------------------ ' : None,
                        #                 'my_zar_balance_in_rands' : zar_account,
                        #                 'my_eth_balance_in_coins' : eth_account,
                        #                 '-------------------------------------------------' : None,
                        #                 'currencypair' : "ETHZAR",
                        #                 'Date' : utils.get_dates()[8],
                        #                 }

                        #         record_datas.buy_sell_status(data, config)




                        # utils.write_to_json(data_dir, wally_json)
                        # print('SELL', Bot_Name, askPrice, capital)

                        # # playsound(TurtleTurtle_audio_path + '/tiky_04.wav')
                        
                        # # For plotting
                        # Global.sold_history_cordinates = count
                        # Global.sold_history_amount = float(bidPrice)

                        # Bot_Notifier.send_notification_SELL(config, Bot_Name, bidPrice, capital)


                        if BackTest_Active == True:
                            Plotter.plot_graph_every_sale(config, count)












######## Buy




def BUY_N_HOLD(
                Bot_Name,
                askPrice, 
                bidPrice,
                collect_ask, 
                collect_bid, 
                x_collect_plot,
                count,
                config,
                trade_status,
                wally_json,
                EXTERNAL_DEGREES
                ):

    """ 7 Trading strategy in Development """

    EMA_spread_ask = -250
    EMA_spread_bid = -250
    SMA_spread_long_bid = -1000
    collected_data_amount = 2
    long_regression_len = -500
    limit_reg = 500
    limit_sell = 0.5
    limit_buy = 0.5

    
    BackTest_Active = config["BackTest_Active"]
    status = config["VALR_active_bots"][Bot_Name]["status"]
    acount_id = config["VALR_active_bots"][Bot_Name]["account"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']
    Bot_Notifications = config["Bot_Notifications"]

    data_dir = config["TurtleTurtle_wallets_path"] + '/' + str(Bot_Name) + '_wallet.json'

    calculated_data = calculations.extra_calculations(
                                                        Bot_Name,
                                                        askPrice, 
                                                        bidPrice,
                                                        collect_ask, 
                                                        collect_bid, 
                                                        x_collect_plot,
                                                        EMA_spread_ask,
                                                        EMA_spread_bid,
                                                        SMA_spread_long_bid,
                                                        collected_data_amount,
                                                        long_regression_len,
                                                        limit_reg,
                                                        limit_sell,
                                                        limit_buy,
                                                        count,
                                                        config,
                                                        EXTERNAL_DEGREES
                                                        )

    if BackTest_Active == True:

        Global = Global_BackTest

    elif BackTest_Active == False:

        Global = Global_Live





    RED_LINE = Global.data_calc[Bot_Name]["output_value_ask"]
    BLUE_LINE = Global.data_calc[Bot_Name]["output_value_bid"]
    YELLOW_LINE = Global.data_calc[Bot_Name]["long_bid"]

    YELLOW_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_long_range"]
    RED_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_range"]
    BLUE_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["bid_range"]

    SHORT_DEGREE = Global.data_calc[Bot_Name]["degrees"]

    ask_dis = float(RED_LINE) - float(YELLOW_LINE)
    bid_dis = float(BLUE_LINE) - float(YELLOW_LINE)


    if float(SHORT_DEGREE) > 50:
        above_30 = True
    else:
        above_30 = False



    if trade_status == 'buy_low':

        capital = wally_json['trade_capital']
        # cap = wally_json['trade_status']
        # wally_json['trade_status'] = 'sell_high'
        # wally_json['limit'] = float(askPrice)
        # coi = wally_json['trade_capital_coin'] = (capital) / float(askPrice)

        # # BUY
        # if BackTest_Active != True:
        #     if status == 'trade':
        #         Balances = VALR.Valr_get_balances(acount_id)
        #         zar_account = Balances['ZAR']['available']
        #         eth_account = Balances['ETH']['available']
        #         coinz = str((float(zar_account) - 500) / float(askPrice))
        #         VALR.BUY_ZAR_to_ETH(coinz, bot=acount_id)


        #         time.sleep(10)
        #         Balances = VALR.Valr_get_balances(acount_id)
        #         zar_account = Balances['ZAR']['available']
        #         xrp_account = Balances['XRP']['available']

        #         wally_json['capital'] = zar_account


        #         data = {'Bot_Name' : Bot_Name,
        #                 'account_ID' : acount_id,
        #                 '------------------------------------------------ ' : None,
        #                 'trade_type' : 'buy_low',
        #                 'askPrice' : askPrice,
        #                 'bidPrice' : bidPrice,
        #                 '------------------------------------------------ ' : None,
        #                 'my_zar_balance_in_rands' : zar_account,
        #                 'my_eth_balance_in_coins' : eth_account,
        #                 '-------------------------------------------------' : None,
        #                 'currencypair' : "ETHZAR",
        #                 'Date' : utils.get_dates()[8],
        #                 }

        #         record_datas.buy_sell_status(data, config)


        # utils.write_to_json(data_dir, wally_json)
        # print('BUY : ', Bot_Name, askPrice, capital)

        # # playsound(TurtleTurtle_audio_path + '/tiky_01.wav')

        # # For plotting
        # Global.buy_history_cordinates = count
        # Global.buy_history_amount = float(askPrice)

        # # Telegram Notifier
        # Bot_Notifier.send_notification_BUY(config, Bot_Name, askPrice, capital)

        if BackTest_Active == True:
            Plotter.plot_graph_every_sale(config, count)




    if trade_status == 'sell_high':

        pass







###### Sell





######## Buy




def SELL_N_HOLD(
                Bot_Name,
                askPrice, 
                bidPrice,
                collect_ask, 
                collect_bid, 
                x_collect_plot,
                count,
                config,
                trade_status,
                wally_json,
                EXTERNAL_DEGREES
                ):

    """ 7 Trading strategy in Development """

    EMA_spread_ask = -250
    EMA_spread_bid = -250
    SMA_spread_long_bid = -1000
    collected_data_amount = 2
    long_regression_len = -500
    limit_reg = 500
    limit_sell = 0.5
    limit_buy = 0.5

    
    BackTest_Active = config["BackTest_Active"]
    status = config["VALR_active_bots"][Bot_Name]["status"]
    acount_id = config["VALR_active_bots"][Bot_Name]["account"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']
    Bot_Notifications = config["Bot_Notifications"]

    data_dir = config["TurtleTurtle_wallets_path"] + '/' + str(Bot_Name) + '_wallet.json'

    calculated_data = calculations.extra_calculations(
                                                        Bot_Name,
                                                        askPrice, 
                                                        bidPrice,
                                                        collect_ask, 
                                                        collect_bid, 
                                                        x_collect_plot,
                                                        EMA_spread_ask,
                                                        EMA_spread_bid,
                                                        SMA_spread_long_bid,
                                                        collected_data_amount,
                                                        long_regression_len,
                                                        limit_reg,
                                                        limit_sell,
                                                        limit_buy,
                                                        count,
                                                        config,
                                                        EXTERNAL_DEGREES
                                                        )

    if BackTest_Active == True:

        Global = Global_BackTest

    elif BackTest_Active == False:

        Global = Global_Live



    RED_LINE = Global.data_calc[Bot_Name]["output_value_ask"]
    BLUE_LINE = Global.data_calc[Bot_Name]["output_value_bid"]
    YELLOW_LINE = Global.data_calc[Bot_Name]["long_bid"]

    YELLOW_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_long_range"]
    RED_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_range"]
    BLUE_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["bid_range"]

    SHORT_DEGREE = Global.data_calc[Bot_Name]["degrees"]

    ask_dis = float(RED_LINE) - float(YELLOW_LINE)
    bid_dis = float(BLUE_LINE) - float(YELLOW_LINE)


    if float(SHORT_DEGREE) > 50:
        above_30 = True
    else:
        above_30 = False



    if trade_status == 'buy_low':
        pass


    if trade_status == 'sell_high':


        capital = wally_json['trade_capital']
        # coin = wally_json['trade_capital_coin']

        # wally_json['trade_status'] = 'buy_low'  
        # wally_json['limit'] = float(bidPrice)
        # wally_json['trade_capital'] = (coin * float(bidPrice))
        # wally_json['trade_capital_coin'] = 0


        # # SELL
        # if BackTest_Active != True:
        #     if status == 'trade':
        #         Balances = VALR.Valr_get_balances(acount_id)
        #         zar_account = Balances['ZAR']['available']
        #         eth_account = Balances['ETH']['available']
        #         VALR.SELL_ETH_to_ZAR(eth_account, bot=acount_id)


        #         time.sleep(10)
        #         Balances = VALR.Valr_get_balances(acount_id)
        #         zar_account = Balances['ZAR']['available']
        #         xrp_account = Balances['XRP']['available']

        #         wally_json['capital'] = zar_account


        #         data = {'Bot_Name' : Bot_Name,
        #                 'account_ID' : acount_id,
        #                 '------------------------------------------------ ' : None,
        #                 'trade_type' : 'sell_high|EXIT',
        #                 'askPrice' : askPrice,
        #                 'bidPrice' : bidPrice,
        #                 '------------------------------------------------ ' : None,
        #                 'my_zar_balance_in_rands' : zar_account,
        #                 'my_eth_balance_in_coins' : eth_account,
        #                 '-------------------------------------------------' : None,
        #                 'currencypair' : "ETHZAR",
        #                 'Date' : utils.get_dates()[8],
        #                 }

        #         record_datas.buy_sell_status(data, config)




        # utils.write_to_json(data_dir, wally_json)
        # print('SELL', Bot_Name, askPrice, capital)

        # # playsound(TurtleTurtle_audio_path + '/tiky_04.wav')

        # # For plotting
        # Global.sold_history_cordinates = count
        # Global.sold_history_amount = float(bidPrice)

        # Bot_Notifier.send_notification_SELL(config, Bot_Name, bidPrice, capital)


        if BackTest_Active == True:
            Plotter.plot_graph_every_sale(config, count)
