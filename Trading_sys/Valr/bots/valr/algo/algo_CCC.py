import time

import Valr.libs.utils.toolUtils as utils

import Valr.libs.globals.Global_BackTest as Global_BackTest
import Valr.libs.globals.Global_Live as Global_Live

import Valr.libs.utils.calculations as calculations
import Valr.libs.utils.plot as Plotter

import Valr.libs.valr.valr_api_tools as VALR
import Valr.libs.utils.record_data as record_datas

import Managers_sys.TeleGram_Manager.Bot_Notifier as Bot_Notifier







def buy_n_HOLD(
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

    """ Trading strategy in Development """

    EMA_spread_ask = -300
    EMA_spread_bid = -300
    SMA_spread_long_bid = -1000
    collected_data_amount = 2
    long_regression_len = -100
    limit_reg = 100
    limit_sell = 1
    limit_buy = 0.2
    stop_limit_sell = 0.8

    

    TurtleTurtle_path = config["TurtleTurtle_path"]

    BackTest_Active = config["BackTest_Active"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']

    status = config["VALR_active_bots"][Bot_Name]["status"]
    acount_id = config["VALR_active_bots"][Bot_Name]["account"]

    path = TurtleTurtle_path + '/data/active_stats/general/market_direction/VALR_ETH_market.json'
    valr_data = utils.read_json(path)

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


    DIRECTION_SHRT = valr_data["SHORT_DEGREE"]["direction"]
    DIRECTION_EXT = valr_data["EXTERNAL_DEGREES"]["direction"]



    RED_LINE = Global.data_calc[Bot_Name]["output_value_ask"]
    BLUE_LINE = Global.data_calc[Bot_Name]["output_value_bid"]
    YELLOW_LINE = Global.data_calc[Bot_Name]["long_bid"]

    YELLOW_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_long_range"]
    RED_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_range"]
    BLUE_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["bid_range"]

    SHORT_DEGREE = (Global.data_calc[Bot_Name]["degrees"]) * 1000

    ask_dis = (float(RED_LINE) - float(YELLOW_LINE)) * 1000
    bid_dis = (float(BLUE_LINE) - float(YELLOW_LINE)) * 1000


    if float(SHORT_DEGREE) > 40:
        above_30 = True
    else:
        above_30 = False

    if float(EXTERNAL_DEGREES[0] * 1000) > 10:
        EXT_is_above_30 = True
    else:
        EXT_is_above_30 = False



    if trade_status == 'buy_low':

        capital = wally_json['trade_capital']
        cap = wally_json['trade_status']
        wally_json['trade_status'] = 'sell_high'
        wally_json['limit'] = float(askPrice)
        coi = wally_json['trade_capital_coin'] = (capital) / float(askPrice)


        # BUY
        if BackTest_Active != True:
            if status == 'trade':
                Balances = VALR.Valr_get_balances(acount_id)
                zar_account = Balances['ZAR']['available']
                xrp_account = Balances['XRP']['available']
                coinz = str((float(zar_account) - 200) / float(askPrice))
                VALR.BUY_ZAR_to_XRP(coinz, bot=acount_id)


                time.sleep(10)
                Balances = VALR.Valr_get_balances(acount_id)
                zar_account = Balances['ZAR']['available']
                xrp_account = Balances['XRP']['available']

                wally_json['capital'] = zar_account

                data = {'Bot_Name' : Bot_Name,
                        'account_ID' : acount_id,
                        '------------------------------------------------ ' : None,
                        'trade_type' : 'buy_low',
                        'askPrice' : askPrice,
                        'bidPrice' : bidPrice,
                        '------------------------------------------------ ' : None,
                        'my_zar_balance_in_rands' : zar_account,
                        'my_eth_balance_in_coins' : xrp_account,
                        '-------------------------------------------------' : None,
                        'currencypair' : "XRPZAR",
                        'Date' : utils.get_dates()[8],
                        }

                record_datas.buy_sell_status(data, config)


        utils.write_to_json(data_dir, wally_json)

        print('BUY', askPrice)

        # Telegram Notifier
        Bot_Notifier.send_notification_BUY(config, Bot_Name, askPrice, capital)

        # For plotting
        Global.buy_history_cordinates = count
        Global.buy_history_amount = float(askPrice)


        if BackTest_Active == True:
            Plotter.plot_graph_every_sale(config, count)


    if trade_status == 'sell_high':

        pass



#####



def sell_n_HOLD(
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

    """ Trading strategy in Development """

    EMA_spread_ask = -300
    EMA_spread_bid = -300
    SMA_spread_long_bid = -1000
    collected_data_amount = 2
    long_regression_len = -100
    limit_reg = 100
    limit_sell = 1
    limit_buy = 0.2
    stop_limit_sell = 0.8

    

    TurtleTurtle_path = config["TurtleTurtle_path"]

    BackTest_Active = config["BackTest_Active"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']

    status = config["VALR_active_bots"][Bot_Name]["status"]
    acount_id = config["VALR_active_bots"][Bot_Name]["account"]

    path = TurtleTurtle_path + '/data/active_stats/general/market_direction/VALR_ETH_market.json'
    valr_data = utils.read_json(path)

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


    DIRECTION_SHRT = valr_data["SHORT_DEGREE"]["direction"]
    DIRECTION_EXT = valr_data["EXTERNAL_DEGREES"]["direction"]



    RED_LINE = Global.data_calc[Bot_Name]["output_value_ask"]
    BLUE_LINE = Global.data_calc[Bot_Name]["output_value_bid"]
    YELLOW_LINE = Global.data_calc[Bot_Name]["long_bid"]

    YELLOW_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_long_range"]
    RED_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_range"]
    BLUE_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["bid_range"]

    SHORT_DEGREE = (Global.data_calc[Bot_Name]["degrees"]) * 1000

    ask_dis = (float(RED_LINE) - float(YELLOW_LINE)) * 1000
    bid_dis = (float(BLUE_LINE) - float(YELLOW_LINE)) * 1000


    if float(SHORT_DEGREE) > 40:
        above_30 = True
    else:
        above_30 = False

    if float(EXTERNAL_DEGREES[0] * 1000) > 10:
        EXT_is_above_30 = True
    else:
        EXT_is_above_30 = False



    if trade_status == 'buy_low':

        pass


    if trade_status == 'sell_high':

        stop_limit = utils.percent_decrease(stop_limit_sell, float(limit))
        sell_limit = utils.percent_increase(limit_sell, float(limit))

        sell_limit = utils.percent_increase(limit_sell, float(limit))

        capital = wally_json['trade_capital']                
        coin = wally_json['trade_capital_coin']

        wally_json['trade_status'] = 'buy_low'  
        wally_json['limit'] = float(bidPrice)
        wally_json['trade_capital'] = (coin * float(bidPrice))
        wally_json['trade_capital_coin'] = 0


        # SELL
        if BackTest_Active != True:
            if status == 'trade':
                Balances = VALR.Valr_get_balances(acount_id)
                zar_account = Balances['ZAR']['available']
                xrp_account = Balances['XRP']['available']
                VALR.SELL_XRP_to_ZAR(xrp_account, bot=acount_id)


                time.sleep(10)
                Balances = VALR.Valr_get_balances(acount_id)
                zar_account = Balances['ZAR']['available']
                xrp_account = Balances['XRP']['available']

                wally_json['capital'] = zar_account


                data = {'Bot_Name' : Bot_Name,
                        'account_ID' : acount_id,
                        '------------------------------------------------ ' : None,
                        'trade_type' : 'sell_high|EXIT',
                        'askPrice' : askPrice,
                        'bidPrice' : bidPrice,
                        '------------------------------------------------ ' : None,
                        'my_zar_balance_in_rands' : zar_account,
                        'my_eth_balance_in_coins' : xrp_account,
                        '-------------------------------------------------' : None,
                        'currencypair' : "XRPZAR",
                        'Date' : utils.get_dates()[8],
                        }

                record_datas.buy_sell_status(data, config)


        utils.write_to_json(data_dir, wally_json)        
        print('SELL', bidPrice)

        # Telegram Notifier
        Bot_Notifier.send_notification_SELL(config, Bot_Name, bidPrice, capital)

        # For plotting
        Global.sold_history_cordinates = count
        Global.sold_history_amount = float(bidPrice)


        if BackTest_Active == True:
            Plotter.plot_graph_every_sale(config, count)








#####












def cost_dollar_avrg(
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

    """ Trading strategy in Development """

    EMA_spread_ask = -700
    EMA_spread_bid = -700
    SMA_spread_long_bid = -2500
    collected_data_amount = 2
    long_regression_len = -100
    limit_reg = 100
    limit_sell = 1
    limit_buy = 0.2
    stop_limit_sell = 0.8

    cost_dollar_avrg_count = 5

    

    TurtleTurtle_path = config["TurtleTurtle_path"]

    BackTest_Active = config["BackTest_Active"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']

    status = config["VALR_active_bots"][Bot_Name]["status"]
    acount_id = config["VALR_active_bots"][Bot_Name]["account"]

    path = TurtleTurtle_path + '/data/active_stats/general/market_direction/VALR_ETH_market.json'
    valr_data = utils.read_json(path)

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


    DIRECTION_SHRT = valr_data["SHORT_DEGREE"]["direction"]
    DIRECTION_EXT = valr_data["EXTERNAL_DEGREES"]["direction"]



    RED_LINE = Global.data_calc[Bot_Name]["output_value_ask"]
    BLUE_LINE = Global.data_calc[Bot_Name]["output_value_bid"]
    YELLOW_LINE = Global.data_calc[Bot_Name]["long_bid"]

    YELLOW_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_long_range"]
    RED_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_range"]
    BLUE_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["bid_range"]

    SHORT_DEGREE = (Global.data_calc[Bot_Name]["degrees"]) * 1000

    ask_dis = (float(RED_LINE) - float(YELLOW_LINE)) * 1000
    bid_dis = (float(BLUE_LINE) - float(YELLOW_LINE)) * 1000


    if float(SHORT_DEGREE) > 40:
        above_30 = True
    else:
        above_30 = False

    if float(EXTERNAL_DEGREES[0] * 1000) > 10:
        EXT_is_above_30 = True
    else:
        EXT_is_above_30 = False

    capitaly = wally_json['trade_capital']

    if trade_status == 'buy_low':


        Global.time_delay_buy += 1
        
        CSD_AVG_wallet_count = wally_json['CSD_AVG_count']
        if CSD_AVG_wallet_count == 0:

            wally_json['trade_status'] = 'sell_high'

            wally_json['trade_capital'] = 0
            wally_json['capital_tmp'] = 0
            #### CSD here reset
            Global.time_delay_sell = 0
            wally_json['CSD_AVG_count'] = config["VALR_active_bots"][Bot_Name]["CSD_avrg_2"]

            coin_divide = config["VALR_active_bots"][Bot_Name]["CSD_avrg"]
            coinz = wally_json['trade_capital_coin']

            wally_json['amound_to_CSD_avrg_coin'] = float(coinz) / float(config["VALR_active_bots"][Bot_Name]["CSD_avrg_2"])


            utils.write_to_json(data_dir, wally_json)

        else:

            if float(EXTERNAL_DEGREES[0] * 1000) < float(-5):
                
                buy_limit = utils.percent_decrease(limit_buy, float(limit))

                if float(SHORT_DEGREE) < float(-10):

                    if float(RED_LINE) < float(YELLOW_LINE):

                        if float(ask_dis) > -60 :

                            if float(askPrice) <= float(buy_limit):
                                    

                                
                                if CSD_AVG_wallet_count != 0:

                                    if Global.time_delay_buy > 500:


                                        # Read CSD_AVG COUNT from bot wallet, CSD_avrg is cost dollar avarage

                                            capital = wally_json['trade_capital']
                                            

                                            CSD_avrg_amount = config["VALR_active_bots"][Bot_Name]["CSD_avrg"]
                                            amound_to_CSD_avrg = capital / CSD_avrg_amount


                                            update_capital_tmp = float(capitaly) - float(amound_to_CSD_avrg)

                                            wally_json['capital_tmp'] = update_capital_tmp

                                            to_coin = float(amound_to_CSD_avrg) / float(askPrice)

                                            UPDATED_csd_count = CSD_AVG_wallet_count - 1
                                            wally_json['CSD_AVG_count'] = UPDATED_csd_count


                                            existing_coins = wally_json['trade_capital_coin']
                                            wally_json['trade_capital_coin'] = float(existing_coins) + float(to_coin)





                                            # BUY
                                            if BackTest_Active != True:
                                                if status == 'trade':
                                                    Balances = VALR.Valr_get_balances(acount_id)
                                                    zar_account = Balances['ZAR']['available']
                                                    xrp_account = Balances['XRP']['available']
                                                    coinz = str((float(zar_account) - 200) / float(askPrice))
                                                    VALR.BUY_ZAR_to_XRP(coinz, bot=acount_id)


                                                    time.sleep(10)
                                                    Balances = VALR.Valr_get_balances(acount_id)
                                                    zar_account = Balances['ZAR']['available']
                                                    xrp_account = Balances['XRP']['available']

                                                    # wally_json['capital'] = zar_account


                                                    data = {'Bot_Name' : Bot_Name,
                                                            'account_ID' : acount_id,
                                                            '------------------------------------------------ ' : None,
                                                            'trade_type' : 'buy_low',
                                                            'askPrice' : askPrice,
                                                            'bidPrice' : bidPrice,
                                                            '------------------------------------------------ ' : None,
                                                            'my_zar_balance_in_rands' : zar_account,
                                                            'my_eth_balance_in_coins' : xrp_account,
                                                            '-------------------------------------------------' : None,
                                                            'currencypair' : "XRPZAR",
                                                            'Date' : utils.get_dates()[8],
                                                            }

                                                    record_datas.buy_sell_status(data, config)


                                            utils.write_to_json(data_dir, wally_json)

                                            print('BUY', askPrice)

                                            print(Global.time_delay_buy, trade_status, CSD_AVG_wallet_count, count)
                                            Global.time_delay_buy = 0

                                            # Telegram Notifier
                                            Bot_Notifier.send_notification_BUY(config, Bot_Name, askPrice, capital)

                                            # For plotting
                                            Global.buy_history_cordinates = count
                                            Global.buy_history_amount = float(askPrice)


                                            if BackTest_Active == True:
                                                Plotter.plot_graph_every_sale(config, count)




                                elif CSD_AVG_wallet_count == 0:


                                    wally_json['trade_status'] = 'sell_high'

                                    wally_json['trade_capital'] = 0
                                    wally_json['capital_tmp'] = 0
                                    #### CSD here reset
                                    Global.time_delay_sell = 0
                                    wally_json['CSD_AVG_count'] = config["VALR_active_bots"][Bot_Name]["CSD_avrg_2"]

                                    coin_divide = config["VALR_active_bots"][Bot_Name]["CSD_avrg"]
                                    coinz = wally_json['trade_capital_coin']

                                    wally_json['amound_to_CSD_avrg_coin'] = float(coinz) / float(config["VALR_active_bots"][Bot_Name]["CSD_avrg_2"])


                                    utils.write_to_json(data_dir, wally_json)







                            


    if trade_status == 'sell_high':

        stop_limit = utils.percent_decrease(stop_limit_sell, float(limit))
        sell_limit = utils.percent_increase(limit_sell, float(limit))


        Global.time_delay_sell += 1


        CSD_AVG_wallet_count = wally_json['CSD_AVG_count']
        if CSD_AVG_wallet_count == 0:


            wally_json['trade_status'] = 'buy_low'
            # wally_json['trade_capital_coin'] = 0

            #### CSD here reset
            Global.time_delay_buy = 0
            wally_json['CSD_AVG_count'] = config["VALR_active_bots"][Bot_Name]["CSD_avrg"]

            utils.write_to_json(data_dir, wally_json)



        else:


            if float(SHORT_DEGREE) < float(30):

                # if float(BLUE_LINE) > float(YELLOW_LINE):

                if EXT_is_above_30 != True:

                    if float(bid_dis) > 50:

                        if float(bidPrice) >= float(sell_limit):

                            sell_limit = utils.percent_increase(limit_sell, float(limit))



                            CSD_AVG_wallet_count = wally_json['CSD_AVG_count']
                            if CSD_AVG_wallet_count != 0:



                                if Global.time_delay_sell > 50:


                                    coin_amount_deduct = wally_json["amound_to_CSD_avrg_coin"]
                                    available_coin = wally_json['trade_capital_coin']


                                    wally_json['limit'] = float(bidPrice)

                                    capital_reAdd = wally_json['trade_capital']
                                    coin_calc = float(coin_amount_deduct) * float(bidPrice)
                                    new_capital = float(coin_calc) + float(capital_reAdd)
                                    wally_json['trade_capital'] = new_capital

                                    left_over_coin = available_coin - coin_amount_deduct



                                    wally_json['capital_tmp'] = (coin_amount_deduct * float(bidPrice))
                                    wally_json['trade_capital_coin'] = left_over_coin


                                    UPDATED_csd_count = CSD_AVG_wallet_count - 1
                                    wally_json['CSD_AVG_count'] = UPDATED_csd_count


                                    capital = wally_json['trade_capital']


                                    # SELL
                                    if BackTest_Active != True:
                                        if status == 'trade':
                                            Balances = VALR.Valr_get_balances(acount_id)
                                            zar_account = Balances['ZAR']['available']
                                            xrp_account = Balances['XRP']['available']
                                            VALR.SELL_XRP_to_ZAR(xrp_account, bot=acount_id)


                                            time.sleep(10)
                                            Balances = VALR.Valr_get_balances(acount_id)
                                            zar_account = Balances['ZAR']['available']
                                            xrp_account = Balances['XRP']['available']

                                            wally_json['capital'] = zar_account

                                            data = {'Bot_Name' : Bot_Name,
                                                    'account_ID' : acount_id,
                                                    '------------------------------------------------ ' : None,
                                                    'trade_type' : 'sell_high|EXIT',
                                                    'askPrice' : askPrice,
                                                    'bidPrice' : bidPrice,
                                                    '------------------------------------------------ ' : None,
                                                    'my_zar_balance_in_rands' : zar_account,
                                                    'my_eth_balance_in_coins' : xrp_account,
                                                    '-------------------------------------------------' : None,
                                                    'currencypair' : "XRPZAR",
                                                    'Date' : utils.get_dates()[8],
                                                    }

                                            record_datas.buy_sell_status(data, config)

        

                                    utils.write_to_json(data_dir, wally_json)        
                                    print('SELL', bidPrice)

                                    # Telegram Notifier
                                    Bot_Notifier.send_notification_SELL(config, Bot_Name, bidPrice, capital)

                                    # For plotting
                                    Global.sold_history_cordinates = count
                                    Global.sold_history_amount = float(bidPrice)


                                    if BackTest_Active == True:
                                        Plotter.plot_graph_every_sale(config, count)



                            elif CSD_AVG_wallet_count == 0:

                                wally_json['trade_status'] = 'buy_low'
                                wally_json['trade_capital_coin'] = 0

                                #### CSD here reset
                                Global.time_delay_buy = 0
                                wally_json['CSD_AVG_count'] = config["VALR_active_bots"][Bot_Name]["CSD_avrg"]

                                utils.write_to_json(data_dir, wally_json)






############













def HIGH_RISK(
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

    """ Trading strategy in Development """
    """ perfect for sideways XRP """

    EMA_spread_ask = -100
    EMA_spread_bid = -100
    SMA_spread_long_bid = -1000
    collected_data_amount = 2
    long_regression_len = -1000
    limit_reg = 1000
    limit_sell = 1
    limit_buy = 0.2
    stop_limit_sell = 2

    

    TurtleTurtle_path = config["TurtleTurtle_path"]

    BackTest_Active = config["BackTest_Active"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']

    status = config["VALR_active_bots"][Bot_Name]["status"]
    acount_id = config["VALR_active_bots"][Bot_Name]["account"]

    path = TurtleTurtle_path + '/data/active_stats/general/market_direction/VALR_ETH_market.json'
    valr_data = utils.read_json(path)

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


    DIRECTION_SHRT = valr_data["SHORT_DEGREE"]["direction"]
    DIRECTION_EXT = valr_data["EXTERNAL_DEGREES"]["direction"]



    RED_LINE = Global.data_calc[Bot_Name]["output_value_ask"]
    BLUE_LINE = Global.data_calc[Bot_Name]["output_value_bid"]
    YELLOW_LINE = Global.data_calc[Bot_Name]["long_bid"]

    YELLOW_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_long_range"]
    RED_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["ask_range"]
    BLUE_DISTANCE_FROM_LINE = Global.data_calc[Bot_Name]["bid_range"]

    SHORT_DEGREE = (Global.data_calc[Bot_Name]["degrees"]) * 1000

    ask_dis = (float(RED_LINE) - float(YELLOW_LINE)) * 1000
    bid_dis = (float(BLUE_LINE) - float(YELLOW_LINE)) * 1000


    if float(SHORT_DEGREE) >= 0:
        above_30 = True
    else:
        above_30 = False

    if float(EXTERNAL_DEGREES[0] * 1000) >= 0:
        EXT_is_above_30 = True
    else:
        EXT_is_above_30 = False



    if trade_status == 'buy_low':

        buy_limit = utils.percent_decrease(limit_buy, float(limit))

        if EXT_is_above_30 != False:
            if above_30 != False:

                if float(RED_LINE) < float(YELLOW_LINE):

                
                    capital = wally_json['trade_capital']
                    cap = wally_json['trade_status']
                    wally_json['trade_status'] = 'sell_high'
                    wally_json['limit'] = float(askPrice)
                    coi = wally_json['trade_capital_coin'] = (capital) / float(askPrice)


                    # BUY
                    if BackTest_Active != True:
                        if status == 'trade':
                            Balances = VALR.Valr_get_balances(acount_id)
                            zar_account = Balances['ZAR']['available']
                            xrp_account = Balances['XRP']['available']
                            coinz = str((float(zar_account) - 200) / float(askPrice))
                            VALR.BUY_ZAR_to_XRP(coinz, bot=acount_id)


                            time.sleep(10)
                            Balances = VALR.Valr_get_balances(acount_id)
                            zar_account = Balances['ZAR']['available']
                            xrp_account = Balances['XRP']['available']

                            wally_json['capital'] = zar_account


                            data = {'Bot_Name' : Bot_Name,
                                    'account_ID' : acount_id,
                                    '------------------------------------------------ ' : None,
                                    'trade_type' : 'buy_low',
                                    'askPrice' : askPrice,
                                    'bidPrice' : bidPrice,
                                    '------------------------------------------------ ' : None,
                                    'my_zar_balance_in_rands' : zar_account,
                                    'my_eth_balance_in_coins' : xrp_account,
                                    '-------------------------------------------------' : None,
                                    'currencypair' : "XRPZAR",
                                    'Date' : utils.get_dates()[8],
                                    }

                            record_datas.buy_sell_status(data, config)


                    utils.write_to_json(data_dir, wally_json)

                    print('BUY', askPrice)


                    # Telegram Notifier
                    Bot_Notifier.send_notification_BUY(config, Bot_Name, askPrice, capital)

                    # For plotting
                    Global.buy_history_cordinates = count
                    Global.buy_history_amount = float(askPrice)


                    if BackTest_Active == True:
                        Plotter.plot_graph_every_sale(config, count)






    if float(SHORT_DEGREE) >= 20:
        above_30_test = True
    else:
        above_30_test = False

    if float(EXTERNAL_DEGREES[0] * 1000) >= 40:
        EXT_is_above_30_test = True
    else:
        EXT_is_above_30_test = False



    if trade_status == 'sell_high':

        stop_limit = utils.percent_decrease(stop_limit_sell, float(limit))


        if float(YELLOW_LINE) < float(stop_limit):

            capital = wally_json['trade_capital']
            # Telegram Notifier
            # Bot_Notifier.send_notification_Warning(config, Bot_Name, bidPrice, capital)



        else:



            stop_limit = utils.percent_decrease(stop_limit_sell, float(limit))
            sell_limit = utils.percent_increase(limit_sell, float(limit))


            if EXT_is_above_30_test != True:
                if above_30_test != True:

                    if float(BLUE_LINE) > float(YELLOW_LINE):

                        if float(bid_dis) > float(50):

                            capital = wally_json['trade_capital']                
                            coin = wally_json['trade_capital_coin']

                            wally_json['trade_status'] = 'buy_low'  
                            wally_json['limit'] = float(bidPrice)
                            wally_json['trade_capital'] = (coin * float(bidPrice))
                            wally_json['trade_capital_coin'] = 0


                            # SELL
                            if BackTest_Active != True:
                                if status == 'trade':
                                    Balances = VALR.Valr_get_balances(acount_id)
                                    zar_account = Balances['ZAR']['available']
                                    xrp_account = Balances['XRP']['available']
                                    VALR.SELL_XRP_to_ZAR(xrp_account, bot=acount_id)


                                    time.sleep(10)
                                    Balances = VALR.Valr_get_balances(acount_id)
                                    zar_account = Balances['ZAR']['available']
                                    xrp_account = Balances['XRP']['available']

                                    wally_json['capital'] = zar_account


                                    data = {'Bot_Name' : Bot_Name,
                                            'account_ID' : acount_id,
                                            '------------------------------------------------ ' : None,
                                            'trade_type' : 'sell_high|EXIT',
                                            'askPrice' : askPrice,
                                            'bidPrice' : bidPrice,
                                            '------------------------------------------------ ' : None,
                                            'my_zar_balance_in_rands' : zar_account,
                                            'my_eth_balance_in_coins' : xrp_account,
                                            '-------------------------------------------------' : None,
                                            'currencypair' : "XRPZAR",
                                            'Date' : utils.get_dates()[8],
                                            }

                                    record_datas.buy_sell_status(data, config)


                            utils.write_to_json(data_dir, wally_json)        
                            print('SELL', bidPrice)

                            # Telegram Notifier
                            Bot_Notifier.send_notification_SELL(config, Bot_Name, bidPrice, capital)

                            # For plotting
                            Global.sold_history_cordinates = count
                            Global.sold_history_amount = float(bidPrice)


                            if BackTest_Active == True:
                                Plotter.plot_graph_every_sale(config, count)












