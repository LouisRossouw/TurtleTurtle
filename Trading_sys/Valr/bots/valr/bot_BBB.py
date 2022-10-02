""" BOT_BBB """


import Valr.libs.globals.Global_Live as Globals_Live
import Valr.libs.globals.Global_BackTest as Global_BackTest

import Valr.libs.utils.bot_utils as bot_utils
import Valr.libs.utils.toolUtils as toolUtils
import Valr.libs.utils.calculations as calculations

import Valr.bots.valr.algo.algo_BBB as ALGO





def run_bot(config, Bot_Name, LIVE_MARKET_DATA, collected_data, count):
    """ 5 Run the Bot, This is the default setup for all bots """

# Config info
    TurtleTurtle_path = config['TurtleTurtle_path']
    BackTest_Active = config['BackTest_Active']
    BackTest_Active_print_statement = config["BackTest_Active_print_statement"]

# Bot Config info
    Status = config['VALR_active_bots'][Bot_Name]['status']
    Risk_mode = config['VALR_active_bots'][Bot_Name]['Risk_mode']
    currency_pair = config['VALR_active_bots'][Bot_Name]['currency_pair']


    askPrice = LIVE_MARKET_DATA[currency_pair]['askPrice']
    bidPrice = LIVE_MARKET_DATA[currency_pair]['bidPrice']


# Setup Wallet if it does not exists
    wally_json = bot_utils.startup_wallet(config, Bot_Name, currency_pair)

    capital = wally_json['trade_capital']
    limit = wally_json['limit']
    trade_status = wally_json['trade_status']
    coin = wally_json['trade_capital_coin']
    market_degrees = wally_json['market_degrees']

    ask_capital_coins = capital / float(askPrice)
    bid_capital_rands = ask_capital_coins * float(bidPrice)


    if BackTest_Active == True:
        # BACKTEST_Globals data
        data = Global_BackTest.data
        collect_ask = data[Bot_Name]["collect_ask"]
        collect_bid = data[Bot_Name]["collect_bid"]

        x_collect_plot = Global_BackTest.data_calc[Bot_Name]["x_collect_plot"]
        EXTERNAL_x_collect = Global_BackTest.data_calc[Bot_Name]["EXTERNAL_x_collect"]
        


    elif BackTest_Active == False:
        # LIVE_Globals data
        data = Globals_Live.data
        get_date = toolUtils.get_dates()
        collect_ask = data[Bot_Name]["collect_ask"]
        collect_bid = data[Bot_Name]["collect_bid"]
        collect_ask.append(float(askPrice))
        collect_bid.append(float(bidPrice))

        x_collect_plot = Globals_Live.data_calc[Bot_Name]["x_collect_plot"]
        EXTERNAL_x_collect = Globals_Live.data_calc[Bot_Name]["EXTERNAL_x_collect"]

        Globals_Live.day = get_date[3]
        Globals_Live.time = str(get_date[1]).split('.')[0]


            # EXTERNAL Linear Regression
    long_regression_len_new = -100
    limit_reg_new = 100
    EXTERNAL_DEGREES = calculations.EXTERNAL_Linear_regression(
                                                                long_regression_len_new, 
                                                                limit_reg_new, 
                                                                EXTERNAL_x_collect, 
                                                                collect_ask, 
                                                                collect_bid,
                                                                askPrice,
                                                                config,
                                                                count
                                                                )


# # ####################################################################################################################################
# # ################################ ADD CUSTOMISABLE ALGO SECTION

    # path = TurtleTurtle_path + '/data/active_stats/general/market_direction/VALR_ETH_market.json'
    # valr_data = toolUtils.read_json(path)

    # DIRECTION_SHRT = valr_data["SHORT_DEGREE"]["direction"]
    # DIRECTION_EXT = valr_data["EXTERNAL_DEGREES"]["direction"]




    if Risk_mode == 'mid':
        algo_data = ALGO.HF_TRADING_v2(
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
                                    )



    elif Risk_mode == 'low':
        algo_data = ALGO.HF_TRADING(
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
                                    )



    elif Risk_mode == 'high':
        algo_data = ALGO.HIGH_RISK(
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
                                    )


    elif Risk_mode == 'sell':
        algo_data = ALGO.sell_n_HOLD(
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
                                    )


    elif Risk_mode == 'buy':
        algo_data = ALGO.buy_n_HOLD(
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
                                    )


# # ################################ ADD CUSTOMISABLE ALGO SECTION
# # ####################################################################################################################################


#     # if BackTest_Active == True:
#     #     print(Global_BackTest.data_calc[Bot_Name]["x_collect"])


#     # if BackTest_Active == False:
#     #     print(Globals_Live.data_calc[Bot_Name]["x_collect"])


    bot_utils.print_status(
                            config, 
                            Bot_Name, 
                            askPrice, 
                            bidPrice, 
                            trade_status, 
                            capital, 
                            Risk_mode, 
                            BackTest_Active, 
                            BackTest_Active_print_statement, 
                            EXTERNAL_DEGREES[0]
                        )



