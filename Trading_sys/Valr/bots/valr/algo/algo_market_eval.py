import Valr.libs.utils.toolUtils as utils

import Valr.libs.globals.Global_BackTest as Global_BackTest
import Valr.libs.globals.Global_Live as Global_Live

import Valr.libs.utils.calculations as calculations

import Managers_sys.TeleGram_Manager.Bot_Notifier as Bot_Notifier





def HF_TRADING(
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

    EMA_spread_ask = -1
    EMA_spread_bid = -1
    SMA_spread_long_bid = -1
    collected_data_amount = 2
    long_regression_len = -3000
    limit_reg = 3000
    limit_sell = 0
    limit_buy = 0

    TurtleTurtle_path = config["TurtleTurtle_path"]
    BackTest_Active = config["BackTest_Active"]
    TurtleTurtle_audio_path = config["TurtleTurtle_audio_path"]
    limit = wally_json['limit']

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

    EXTERNAL_DEGREES_CLEAN = EXTERNAL_DEGREES[0]

    path = TurtleTurtle_path + '/data/active_stats/general/market_direction/VALR_ETH_market.json'


    read_data = utils.read_json(path)
    EXT_notification = read_data["EXTERNAL_DEGREES"]["notification"]
    SHRT_notification = read_data["SHORT_DEGREE"]["notification"]


    data = {}

    # SHORT DEGREE (1 DAY DIRECTION)
    if (SHORT_DEGREE >= float(5)) and (SHORT_DEGREE <= float(20)):
        data["SHORT_DEGREE"] = {"direction" : "positive", "description" : "positive || uptred, swing trade up trend", "degree" : SHORT_DEGREE, "notification" : 'A' }
        if SHRT_notification != 'A':
            Bot_Notifier.SHORT_direction(config, askPrice, bidPrice, data)

    elif (SHORT_DEGREE >= float(-10)) and (SHORT_DEGREE <= float(5)):
        data["SHORT_DEGREE"] = {"direction" : "Neutral", "description" : "Neutral || sideways trend, lets do high freq short trading", "degree" : SHORT_DEGREE, "notification" : 'B' }
        if SHRT_notification != 'B':
            Bot_Notifier.SHORT_direction(config, askPrice, bidPrice, data)

    elif SHORT_DEGREE > float(20):
        data["SHORT_DEGREE"] = {"direction" : "positive_hold", "description" : "POSITIVE! || upward trend, LETS HOLD and unil we flatten out", "degree" : SHORT_DEGREE, "notification" : 'C' }
        if SHRT_notification != 'C':
            Bot_Notifier.SHORT_direction(config, askPrice, bidPrice, data)

    elif (SHORT_DEGREE < float(-10)) and (SHORT_DEGREE > float(-25)):
        data["SHORT_DEGREE"] = {"direction" : "Negative", "description" : "Negative || we are going downhill, hold", "degree" : SHORT_DEGREE, "notification" : 'D' }      
        if SHRT_notification != 'D':
            Bot_Notifier.SHORT_direction(config, askPrice, bidPrice, data)

    elif SHORT_DEGREE <= float(-25):
        data["SHORT_DEGREE"] = {"direction" : "Negative", "description" : "NEGATIVE! || if we are in SELL mode, lets cut our losses and sell now before we loose too much",  "degree" : SHORT_DEGREE, "notification" : 'E' }
        if SHRT_notification != 'E':
            Bot_Notifier.SHORT_direction(config, askPrice, bidPrice, data)
    



    # LONG DEGREE (2 DAY DIRECTION)
    if (EXTERNAL_DEGREES_CLEAN >= float(5)) and (EXTERNAL_DEGREES_CLEAN <= float(20)):
        data["EXTERNAL_DEGREES"] = {"direction" : "positive", "description" : "positive || uptred, swing trade up trend", "degree" : EXTERNAL_DEGREES_CLEAN, "notification" : 'A' }
        if EXT_notification != 'A':
            Bot_Notifier.LONG_direction(config, askPrice, bidPrice, data)

    elif (EXTERNAL_DEGREES_CLEAN >= float(-5)) and (EXTERNAL_DEGREES_CLEAN <= float(5)):
        data["EXTERNAL_DEGREES"] = {"direction" : "Neutral", "description" : "Neutral || sideways trend, lets do high freq short trading", "degree" : EXTERNAL_DEGREES_CLEAN, "notification" : 'B' }
        if EXT_notification != 'B':
            Bot_Notifier.LONG_direction(config, askPrice, bidPrice, data)

    elif EXTERNAL_DEGREES_CLEAN > float(20):
        data["EXTERNAL_DEGREES"] = {"direction" : "positive_hold", "description" : "POSITIVE! || upward trend, LETS HOLD and unil we flatten out", "degree" : EXTERNAL_DEGREES_CLEAN, "notification" : 'C' }
        if EXT_notification != 'C':
            Bot_Notifier.LONG_direction(config, askPrice, bidPrice, data)

    elif (EXTERNAL_DEGREES_CLEAN < float(-5)) and (EXTERNAL_DEGREES_CLEAN > float(-25)):
        data["EXTERNAL_DEGREES"] = {"direction" : "Negative", "description" : "Negative || we are going downhill, hold", "degree" : EXTERNAL_DEGREES_CLEAN, "notification" : 'D' }  
        if EXT_notification != 'D':
            Bot_Notifier.LONG_direction(config, askPrice, bidPrice, data)

    elif EXTERNAL_DEGREES_CLEAN <= float(-25):
        data["EXTERNAL_DEGREES"] = {"direction" : "Negative", "description" : "NEGATIVE! || if we are in SELL mode, lets cut our losses and sell now before we loose too much",  "degree" : EXTERNAL_DEGREES_CLEAN, "notification" : 'E' }
        if EXT_notification != 'E':
            Bot_Notifier.LONG_direction(config, askPrice, bidPrice, data)

    # print(SHORT_DEGREE, EXTERNAL_DEGREES_CLEAN)

    utils.write_to_json(path, data)

