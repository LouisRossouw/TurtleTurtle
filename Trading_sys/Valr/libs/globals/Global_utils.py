import sys
from time import sleep

from numpy import append

import Valr.libs.utils.toolUtils as ToolUtils

import Valr.libs.globals.Global_Live as Global_Live
import Valr.libs.globals.Global_BackTest as Global_BackTest





def set_globals(config):
    """ 3 Sets the Globals at the very start when the program runs """

    BackTest_Active = config["BackTest_Active"]
    bot_list_valr = config["VALR_active_bots"]
    # bot_list_luno = config["LUNO_active_bots"]

    bot_list = {}
    bot_list.update(bot_list_valr)
    # bot_list.update(bot_list_luno)


    if BackTest_Active == True:

        for Bot_name in bot_list:

            # status = config['VALR_active_bots'][Bot_name]['status']
            status = bot_list[Bot_name]['status']

            if status != 'hold':

                GB_data = Global_BackTest.data
                GB_data[Bot_name] = {
                                    "collect_ask" : [], 
                                    "collect_bid" : [],
                                    "collect_lowPrice" : [],
                                    "collect_highPrice" : []
                                }


                # test
                GB_data_calc = Global_BackTest.data_calc
                GB_data_calc[Bot_name] = {
                                    "collect_data_bid" : 0, 
                                    "one_min_collection_bid" : 0,
                                    "one_min_collection_short_bid" : 0,
                                    "long_avg" : 0,
                                    "output_value_bid" : 0,
                                    "output_value_short_bid" : 0,
                                    "collect_data_ask" : 0,
                                    "one_min_collection_ask" : 0,
                                    "output_value_ask" : 0,
                                    "degrees" : 0,
                                    "x_collect_plot" : [],
                                    "x_regress_values" : 0,
                                    "calc_linregress" : 0,
                                    "long_bid" : 0,
                                    "ask_long_range" : 0,
                                    "ask_range" : 0,
                                    "bid_range" : 0,

                                    'long_regression_len' : 0,

                                    "long_regression_len_new" : 0,
                                    "x_regress_values_new" : 0,
                                    "calc_linregress_new" : 0,

                                    "collect_mean_bid" : [],
                                    "collect_mean_ask" : [],
                                    "collect_long" : [],
                                    "EXTERNAL_x_collect" : [],

                                    "sold_data" : [],
                                    "buy_data" : []
                                }



    elif BackTest_Active == False:   

        for Bot_name in bot_list:

            # status = config['VALR_active_bots'][Bot_name]['status']
            status = bot_list[Bot_name]['status']

            if status != 'hold':


                GB_data = Global_Live.data
                GB_data[Bot_name] = {
                                    "collect_ask" : [], 
                                    "collect_bid" : [],
                                    "collect_lowPrice" : [],
                                    "collect_highPrice" : []
                                }  

                # test
                GB_data_calc = Global_Live.data_calc
                GB_data_calc[Bot_name] = {
                                    "collect_data_bid" : 0, 
                                    "one_min_collection_bid" : 0,
                                    "one_min_collection_short_bid" : 0,
                                    "long_avg" : 0,
                                    "output_value_bid" : 0,
                                    "output_value_short_bid" : 0,
                                    "collect_data_ask" : 0,
                                    "one_min_collection_ask" : 0,
                                    "output_value_ask" : 0,
                                    "degrees" : 0,
                                    "x_collect_plot" : [],
                                    "x_regress_values" : 0,
                                    "calc_linregress" : 0,
                                    "long_bid" : 0,
                                    "ask_long_range" : 0,
                                    "ask_range" : 0,
                                    "bid_range" : 0,

                                    'long_regression_len' : 0,

                                    "long_regression_len_new" : 0,
                                    "x_regress_values_new" : 0,
                                    "calc_linregress_new" : 0,

                                    "collect_mean_bid" : [],
                                    "collect_mean_ask" : [],
                                    "collect_long" : [],
                                    "EXTERNAL_x_collect" : [],

                                    "sold_data" : [],
                                    "buy_data" : []
                                }


            

def pre_store_to_global(config, Bot_name, collected_data, LIVE_MARKET_DATA):
    """ 4 This calculates the data before giving it to a bot """
    
    BackTest_Active = config["BackTest_Active"]
    try:
        currency_pair = config["VALR_active_bots"][Bot_name]["currency_pair"]
    except KeyError:
        currency_pair = config["LUNO_active_bots"][Bot_name]["currency_pair"]    

    
    if BackTest_Active == True:

        GB_data = Global_BackTest.data

        collect_ask = Global_BackTest.data[Bot_name]["collect_ask"]
        collect_bid = Global_BackTest.data[Bot_name]["collect_bid"]
        collect_highPrice = Global_BackTest.data[Bot_name]["collect_highPrice"]
        collect_lowPrice = Global_BackTest.data[Bot_name]["collect_lowPrice"]

        askPrice_data = LIVE_MARKET_DATA[currency_pair]['askPrice']
        bidPrice_data = LIVE_MARKET_DATA[currency_pair]['bidPrice']

        lowPrice_data = LIVE_MARKET_DATA[currency_pair]['lowPrice']
        highPrice_data = LIVE_MARKET_DATA[currency_pair]['highPrice']

        # Append
        collect_ask.append(float(askPrice_data))
        collect_bid.append(float(bidPrice_data))

        collect_lowPrice.append(float(lowPrice_data))
        collect_highPrice.append(float(highPrice_data))

        GB_data[Bot_name] = {
                            "collect_ask" : collect_ask, 
                            "collect_bid" : collect_bid,
                            "collect_lowPrice" : collect_lowPrice,
                            "collect_highPrice" : collect_highPrice
                        }





    elif BackTest_Active == False:
        # puts all the data into the globals

        GB_data = Global_Live.data

        collect_ask = Global_Live.data[Bot_name]["collect_ask"]
        collect_bid = Global_Live.data[Bot_name]["collect_bid"]
        collect_highPrice = Global_Live.data[Bot_name]["collect_highPrice"]
        collect_lowPrice = Global_Live.data[Bot_name]["collect_lowPrice"]

        for path in collected_data:

            data = ToolUtils.read_json(path)

            for time in data:

                askPrice_data = data[time][currency_pair]['askPrice']
                bidPrice_data = data[time][currency_pair]['bidPrice']

                lowPrice_data = data[time][currency_pair]['lowPrice']
                highPrice_data = data[time][currency_pair]['highPrice']

                # Append
                collect_ask.append(float(askPrice_data))
                collect_bid.append(float(bidPrice_data))

                collect_lowPrice.append(float(lowPrice_data))
                collect_highPrice.append(float(highPrice_data))

        GB_data[Bot_name] = {
                            "collect_ask" : collect_ask, 
                            "collect_bid" : collect_bid,
                            "collect_lowPrice" : collect_lowPrice,
                            "collect_highPrice" : collect_highPrice
                        }




def append_new_stats(
                        collect_bid, 
                        one_min_collection_bid, 
                        one_min_collection_short_bid, 
                        long_avg, 
                        output_value_bid, 
                        output_value_short_bid, 
                        collect_ask, 
                        one_min_collection_ask, 
                        output_value_ask,
                        degrees, 
                        x_collect_plot, 
                        x_regress_values, 
                        calc_linregress, 
                        long_bid, 
                        ask_long_range, 
                        ask_range, 
                        bid_range,
                        Bot_Name,
                        count,
                        config,
                        EXTERNAL_DEGREES,
                        long_regression_len
                    ):
    """ 9 appends all the calcualted stats globally, for the specific bot """

    BackTest_Active = config["BackTest_Active"]


    if BackTest_Active == True:

        data_calc = Global_BackTest.data_calc

        collect_mean_bid = data_calc[Bot_Name]["collect_mean_bid"]
        collect_mean_ask = data_calc[Bot_Name]["collect_mean_ask"]
        collect_long = data_calc[Bot_Name]["collect_long"]



        collect_mean_bid.append(output_value_bid)
        collect_mean_ask.append(output_value_ask)
        collect_long.append(long_bid)

        # sell plotting
        sold_cordinates = Global_BackTest.sold_history_cordinates
        sold_amount = Global_BackTest.sold_history_amount
        buy_cordinates = Global_BackTest.buy_history_cordinates
        buy_amount = Global_BackTest.buy_history_amount

        sold_data = Global_BackTest.sold_data
        sold_data[sold_cordinates] = sold_amount

        buy_data = Global_BackTest.buy_data
        buy_data[buy_cordinates] = buy_amount



        data_calc[Bot_Name] =  {
                                "collect_data_bid" : collect_bid, 
                                "one_min_collection_bid" : one_min_collection_bid,
                                "one_min_collection_short_bid" : one_min_collection_short_bid,
                                "long_avg" : long_avg,
                                "output_value_bid" : output_value_bid,
                                "output_value_short_bid" : output_value_short_bid,
                                "collect_data_ask" : collect_ask,
                                "one_min_collection_ask" : one_min_collection_ask,
                                "output_value_ask" : output_value_ask,
                                "degrees" : degrees,
                                "x_collect_plot" : x_collect_plot,
                                "x_regress_values" : x_regress_values,
                                "calc_linregress" : calc_linregress,
                                "long_bid" : long_bid,
                                "ask_long_range" : ask_long_range,
                                "ask_range" : ask_range,
                                "bid_range" : bid_range,

                                'long_regression_len' : long_regression_len,

                                "long_regression_len_new" : EXTERNAL_DEGREES[1],
                                "x_regress_values_new" : EXTERNAL_DEGREES[2],
                                "calc_linregress_new" : EXTERNAL_DEGREES[3],

                                "collect_mean_bid" : collect_mean_bid,
                                "collect_mean_ask" : collect_mean_ask,
                                "collect_long" : collect_long,
                                "EXTERNAL_x_collect" : EXTERNAL_DEGREES[2],

                                "sold_data" : sold_data,
                                "buy_data" : buy_data
                            }


    elif BackTest_Active == False:

        data_calc = Global_Live.data_calc

        collect_mean_bid = data_calc[Bot_Name]["collect_mean_bid"]
        collect_mean_ask = data_calc[Bot_Name]["collect_mean_ask"]
        collect_long = data_calc[Bot_Name]["collect_long"]

        collect_mean_bid.append(output_value_bid)
        collect_mean_ask.append(output_value_ask)
        collect_long.append(long_bid)


        # sell plotting
        sold_cordinates = Global_Live.sold_history_cordinates
        sold_amount = Global_Live.sold_history_amount
        buy_cordinates = Global_Live.buy_history_cordinates
        buy_amount = Global_Live.buy_history_amount

        sold_data = Global_Live.sold_data
        sold_data[sold_cordinates] = sold_amount

        buy_data = Global_Live.buy_data
        buy_data[buy_cordinates] = buy_amount


        data_calc[Bot_Name] =  {
                                "collect_data_bid" : collect_bid, 
                                "one_min_collection_bid" : one_min_collection_bid,
                                "one_min_collection_short_bid" : one_min_collection_short_bid,
                                "long_avg" : long_avg,
                                "output_value_bid" : output_value_bid,
                                "output_value_short_bid" : output_value_short_bid,
                                "collect_data_ask" : collect_ask,
                                "one_min_collection_ask" : one_min_collection_ask,
                                "output_value_ask" : output_value_ask,
                                "degrees" : degrees,
                                "x_collect_plot" : x_collect_plot,
                                "x_regress_values" : x_regress_values,
                                "calc_linregress" : calc_linregress,
                                "long_bid" : long_bid,
                                "ask_long_range" : ask_long_range,
                                "ask_range" : ask_range,
                                "bid_range" : bid_range,

                                'long_regression_len' : long_regression_len,

                                "long_regression_len_new" : EXTERNAL_DEGREES[1],
                                "x_regress_values_new" : EXTERNAL_DEGREES[2],
                                "calc_linregress_new" : EXTERNAL_DEGREES[3],

                                "collect_mean_bid" : [],
                                "collect_mean_ask" : [],
                                "collect_long" : [],
                                "EXTERNAL_x_collect" : EXTERNAL_DEGREES[2],


                                "sold_data" : sold_data,
                                "buy_data" : buy_data
                            }







if __name__ == '__main__':

    config = ToolUtils.yaml_config("D:/work/projects/dev/projects/TurtleTurtle_v4/config.yaml")
    set_globals(config)