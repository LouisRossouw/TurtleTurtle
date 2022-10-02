import sys
import numpy
import math

from scipy import stats

import Valr.libs.globals.Global_utils as Global_utils

import Valr.libs.globals.Global_Live as Globals_Live
import Valr.libs.globals.Global_BackTest as Global_BackTest






def linear_regression(x, y, plot, min_count_check):
    """ add regression and Calculate the degrees"""


    x_len_check = len(x)
 
    if x_len_check == min_count_check:

        slope, intercept, r, p, std_err = stats.linregress(x, y)
        def myfunc(x):
            return slope * x + intercept

        calc_linregress = list(map(myfunc, x))

        lengh = len(x)
        x1 = x[0]
        x2 = x[lengh - 1]

        end = len(calc_linregress)
        y1 = calc_linregress[0]
        y2 = calc_linregress[end - 1]


        def get_angle(x1, x2, y1, y2):

            deltaY = ((y2) - (y1))
            deltaX = ((x2) - (x1))
            distance = (deltaX + deltaY) ** (1/2)
            radian = math.atan2(deltaY, deltaX)
            return(numpy.degrees(radian))

        degree = get_angle(x1,x2,y1,y2)

        data = {}
        data['degree'] = degree
        data['calc_linregress'] = calc_linregress

        return(data)










def EXTERNAL_Linear_regression(long_regression_len_new, limit_reg_new, EXTERNAL_x_collect, collect_ask, collect_bid, askPrice, config, count):
    """ 6 This calculates the external linear regression line """

    BackTest_Active = config["BackTest_Active"]

    if BackTest_Active == False:

        for i in range(len(collect_ask)):
            EXTERNAL_x_collect.append(i)

    if BackTest_Active == True:

        EXTERNAL_x_collect.append(count)

    x_pure = collect_bid[long_regression_len_new:]
    x_regress_values_new = EXTERNAL_x_collect[long_regression_len_new:]
    x_clean = []
    for xs in range(1, len(x_pure) + 1):
        x_clean.append(xs)
    y = collect_bid[long_regression_len_new:]
    reg_data = linear_regression(x_clean, y, False, limit_reg_new)
    try:
        degrees_new = reg_data['degree']
        calc_linregress_new = reg_data['calc_linregress']
    except TypeError:
        degrees_new = 0

    calc_linregress_new = reg_data
    EXTERNAL_DEGREES = degrees_new


    return(EXTERNAL_DEGREES, long_regression_len_new, x_regress_values_new, calc_linregress_new)





def INTERNAL_Linear_regression(long_regression_len_new, limit_reg, x_collect_plot, collect_ask, collect_bid, askPrice, config, count):

    BackTest_Active = config["BackTest_Active"]

    if BackTest_Active == False:

        for i in range(len(collect_ask)):
            x_collect_plot.append(i)

    if BackTest_Active == True:

        x_collect_plot.append(count)

    # Linear Regression
    x_pure = collect_bid[long_regression_len_new:]
    x_regress_values_new = x_collect_plot[long_regression_len_new:]
    x_clean = []
    for xs in range(1, len(x_pure) + 1):
        x_clean.append(xs)

    y = collect_bid[long_regression_len_new:]
    reg_data = linear_regression(x_clean, y, False, limit_reg)

    try:
        degrees = reg_data['degree']
        calc_linregress = reg_data['calc_linregress']
    except TypeError:
        degrees = 0

    calc_linregress = reg_data

    return(x_collect_plot, x_regress_values_new, degrees, calc_linregress)




# def calc(collect_bid, bidPrice, EMA_spread_bid, SMA_spread_long_bid, collect_ask, askPrice, EMA_spread_ask, count, long_regression_len, limit_reg, x_collect_plot):
def extra_calculations(  
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
            ):

    """ 8 calculates all the needed data """

    # get the bid_avarage
    # collect_bid.append(float(bidPrice))
    one_min_collection_bid = collect_bid[EMA_spread_bid:]
    one_min_collection_short_bid = collect_bid[-200:]
    long_avg = collect_bid[SMA_spread_long_bid:]
    output_value_bid = numpy.mean(one_min_collection_bid)
    output_value_short_bid = numpy.average(one_min_collection_short_bid)

    # get the ask_avarage
    # collect_ask.append(float(askPrice))
    one_min_collection_ask = collect_ask[EMA_spread_ask:]
    output_value_ask = numpy.mean(one_min_collection_ask)

    # LINEAR_REGRESSION - getand return calc, degrees, linear regression etc
    get_calc_deg_data = INTERNAL_Linear_regression(long_regression_len, limit_reg, x_collect_plot, collect_ask, collect_bid, askPrice, config, count)

    x_collect_plot = get_calc_deg_data[0]
    x_regress_values = get_calc_deg_data[1]
    degrees = get_calc_deg_data[2]
    calc_linregress = get_calc_deg_data[3]

    long_bid = numpy.average(long_avg)
    
    ask_long_range = float(askPrice) - float(long_bid)
    ask_range = float(askPrice) - float(output_value_ask)
    bid_range = float(output_value_bid) - float(bidPrice)




    # plot data
    Global_utils.append_new_stats(
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
                                    round(ask_range, 1), 
                                    round(bid_range, 1),
                                    Bot_Name,
                                    count,
                                    config,
                                    EXTERNAL_DEGREES,
                                    long_regression_len
                                )




    return(
            collect_bid, 
            one_min_collection_bid, 
            one_min_collection_short_bid, 
            long_avg, output_value_bid, 
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
            bid_range
            )