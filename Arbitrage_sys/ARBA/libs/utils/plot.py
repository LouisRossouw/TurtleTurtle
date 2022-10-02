import os
import numpy
import datetime

from PIL import Image
import matplotlib.pyplot as plt

import Valr.libs.globals.Global_BackTest as Global_BackTest
import Valr.libs.globals.Global_Live as Global_Live







def plot_animation(config, count):
    """ This plots a graph of the backtesting """


    active_bots = config["VALR_active_bots"]
    BackTest_Active = config["BackTest_Active"]

    if BackTest_Active == True:
        data_plot = Global_BackTest.data_calc
    elif BackTest_Active == False:
        data_plot = Global_Live.data_calc



    for bot in active_bots:

        status = active_bots[bot]["status"]
        Plot_graph = active_bots[bot]["Plot_graph"]

        if status != 'hold':
            if Plot_graph == True:


                collect_data_bid = data_plot[bot]["collect_data_bid"]
                one_min_collection_bid = data_plot[bot]["one_min_collection_bid"]
                one_min_collection_short_bid = data_plot[bot]["one_min_collection_short_bid"]

                long_avg = data_plot[bot]["long_avg"]
                output_value_bid = data_plot[bot]["output_value_bid"]
                output_value_short_bid = data_plot[bot]["output_value_short_bid"]

                collect_data_ask = data_plot[bot]["collect_data_ask"]
                one_min_collection_ask = data_plot[bot]["one_min_collection_ask"]
                output_value_ask = data_plot[bot]["output_value_ask"]

                degrees = data_plot[bot]["degrees"]
                x_collect = data_plot[bot]["x_collect_plot"]
                x_regress_values = data_plot[bot]["x_regress_values"]

                calc_linregress = data_plot[bot]["calc_linregress"]
                long_bid = data_plot[bot]["long_bid"]
                ask_long_range = data_plot[bot]["ask_long_range"]

                ask_range = data_plot[bot]["ask_range"]
                bid_range = data_plot[bot]["bid_range"]

                long_regression_len = data_plot[bot]["long_regression_len"]

                long_regression_len_new = data_plot[bot]["long_regression_len_new"]
                x_regress_values_new = data_plot[bot]["x_regress_values_new"]
                calc_linregress_new = data_plot[bot]["calc_linregress_new"]

                collect_mean_ask = data_plot[bot]["collect_mean_ask"]
                collect_mean_bid = data_plot[bot]["collect_mean_bid"]
                collect_long = data_plot[bot]["collect_long"]

                sold_data = data_plot[bot]["sold_data"]
                buy_data = data_plot[bot]["buy_data"]


                x_axis = []

                count = 0
                for i in x_collect:
                    count += 1
                    x_axis.append(count)



                x_regress = numpy.array(x_regress_values)[long_regression_len:]

                x_regress_new = numpy.array(x_regress_values_new)[long_regression_len_new:]


                ask_min_value = min(collect_data_ask)
                ask_max_value = max(collect_data_ask)

                bid_min_value = min(collect_data_bid)
                bid_max_value = max(collect_data_bid)

                day = str(datetime.datetime.now())
                day_date = day.split(' ')[0]

                img_path_long_avarage = config["TurtleTurtle_path"] + "/data/backtest/graph_animation/" +  bot + "_BACKTEST_ANim_" + str(count) + '.png'
                img_path_askprice_avarage = config["TurtleTurtle_path"] + "/data/backtest/graph_animation/" +  bot + "_BACKTEST_ANim_" + str(count) + '.png'


                ## BID
                # plot bidprice
                plt.title('test')
                plt.xlabel('time')
                plt.xticks(rotation=0)
                plt.ylabel('value')
                plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
                ee = plt.gcf()
                ee.set_size_inches(65, 10)

                fig, ax = plt.subplots()
                # # ax.scatter(x_regress_values, y)
                ax.plot(x_regress, calc_linregress["calc_linregress"], color='lime', linewidth=1)
                # # plot EXTERNAL MAIN LINEAR REGRESSION
                ax.plot(x_regress_new, calc_linregress_new["calc_linregress"], color='magenta', linewidth=1)

                # bid
                plt.ylim(float(bid_min_value), float(bid_max_value))
                plt.plot(x_axis, collect_data_bid, color="blue", linewidth=0.05)

                # # plot avarage_bidprice
                plt.ylim(float(bid_min_value), float(bid_max_value))
                    
                plt.plot(x_axis, collect_mean_bid, color="navy", linewidth=0.5)

                # # plot avarage_long
                plt.ylim(float(bid_min_value), float(bid_max_value))
                    
                plt.plot(x_axis, collect_long, color="yellow", linewidth=0.5)

                ## ASK
                plt.ylim(float(bid_min_value), float(bid_max_value))
                plt.plot(x_axis, collect_data_ask, color='darkred', linewidth=0.05)

                # # plot avarage_askprice
                ee = plt.gcf()
                ee.set_size_inches(65, 10)

                plt.ylim(float(bid_min_value), float(bid_max_value))

                plt.plot(x_axis, collect_mean_ask, color='red', linewidth=0.5)

                for i in sold_data:  
                    # plt.text(i, sold_data[i] + 150, 'SOLD', color='blue') 
                    plt.scatter(i, sold_data[i], color='green')

                for i in buy_data:   
                    # plt.text(i, buy_data[i] + 150, 'BUY', color='red') 
                    plt.scatter(i, buy_data[i], color='red')


                plt.savefig(img_path_askprice_avarage, transparent=True)

                # # # composit images
                # img_ask_avg = Image.open(img_path_askprice_avarage)
                # img_width, img_height = img_ask_avg.size

                # img_color_backround = Image.new('RGBA', (img_width, img_height), (75, 75, 75))
                # Image.alpha_composite(img_color_backround, img_ask_avg).save(config["TurtleTurtle_path"] + "/data/backtest/graph_animation/" + bot + "_BACKTEST_ANIMATION_" + str(count) + ".png")

                # # playsound(PATH_TURTLE_AUDIO_DIR + '/tiky_07.wav')

                # # cleanup
                # os.remove(img_path_askprice_avarage)








def plot_graph_every_sale(config, count):
    """ This plots a graph of the backtesting """



    BackTest_Active = config["BackTest_Active"]

    VALR_active_bots = config["VALR_active_bots"]
    # LUNO_active_bots = config["LUNO_active_bots"]


    active_bots = {}
    # active_bots.update(LUNO_active_bots)
    active_bots.update(VALR_active_bots)





    if BackTest_Active == True:
        data_plot = Global_BackTest.data_calc
    elif BackTest_Active == False:
        data_plot = Global_Live.data_calc



    for bot in active_bots:

        status = active_bots[bot]["status"]
        Plot_graph = active_bots[bot]["Plot_graph"]

        if status != 'hold':
            if Plot_graph == True:


                collect_data_bid = data_plot[bot]["collect_data_bid"]
                one_min_collection_bid = data_plot[bot]["one_min_collection_bid"]
                one_min_collection_short_bid = data_plot[bot]["one_min_collection_short_bid"]

                long_avg = data_plot[bot]["long_avg"]
                output_value_bid = data_plot[bot]["output_value_bid"]
                output_value_short_bid = data_plot[bot]["output_value_short_bid"]

                collect_data_ask = data_plot[bot]["collect_data_ask"]
                one_min_collection_ask = data_plot[bot]["one_min_collection_ask"]
                output_value_ask = data_plot[bot]["output_value_ask"]

                degrees = data_plot[bot]["degrees"]
                x_collect = data_plot[bot]["x_collect_plot"]
                x_regress_values = data_plot[bot]["x_regress_values"]

                calc_linregress = data_plot[bot]["calc_linregress"]
                long_bid = data_plot[bot]["long_bid"]
                ask_long_range = data_plot[bot]["ask_long_range"]

                ask_range = data_plot[bot]["ask_range"]
                bid_range = data_plot[bot]["bid_range"]

                long_regression_len = data_plot[bot]["long_regression_len"]

                long_regression_len_new = data_plot[bot]["long_regression_len_new"]
                x_regress_values_new = data_plot[bot]["x_regress_values_new"]
                calc_linregress_new = data_plot[bot]["calc_linregress_new"]

                collect_mean_ask = data_plot[bot]["collect_mean_ask"]
                collect_mean_bid = data_plot[bot]["collect_mean_bid"]
                collect_long = data_plot[bot]["collect_long"]

                sold_data = data_plot[bot]["sold_data"]
                buy_data = data_plot[bot]["buy_data"]


                x_axis = []

                count = 0
                for i in x_collect:
                    count += 1
                    x_axis.append(count)



                x_regress = numpy.array(x_regress_values)[long_regression_len:]

                x_regress_new = numpy.array(x_regress_values_new)[long_regression_len_new:]


                ask_min_value = min(collect_data_ask)
                ask_max_value = max(collect_data_ask)

                bid_min_value = min(collect_data_bid)
                bid_max_value = max(collect_data_bid)

                day = str(datetime.datetime.now())
                day_date = day.split(' ')[0]

                img_path_long_avarage = config["TurtleTurtle_path"] + "/data/backtest/graphs/" + str(day_date) + '.png'
                img_path_askprice_avarage = config["TurtleTurtle_path"] + "/data/backtest/graphs/" + str(day_date) + '.png'


                try:
                    ## BID
                    # plot bidprice
                    plt.title('test')
                    plt.xlabel('time')
                    plt.xticks(rotation=0)
                    plt.ylabel('value')
                    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
                    ee = plt.gcf()
                    ee.set_size_inches(65, 10)

                    fig, ax = plt.subplots()
                    # # ax.scatter(x_regress_values, y)
                    ax.plot(x_regress, calc_linregress["calc_linregress"], color='lime', linewidth=1)
                    # # plot EXTERNAL MAIN LINEAR REGRESSION
                    ax.plot(x_regress_new, calc_linregress_new["calc_linregress"], color='magenta', linewidth=1)

                    # bid
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                    plt.plot(x_axis, collect_data_bid, color="blue", linewidth=0.05)

                    # # plot avarage_bidprice
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                        
                    plt.plot(x_axis, collect_mean_bid, color="navy", linewidth=0.5)

                    # # plot avarage_long
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                        
                    plt.plot(x_axis, collect_long, color="yellow", linewidth=0.5)

                    ## ASK
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                    plt.plot(x_axis, collect_data_ask, color='darkred', linewidth=0.05)

                    # # plot avarage_askprice
                    ee = plt.gcf()
                    ee.set_size_inches(65, 10)

                    plt.ylim(float(bid_min_value), float(bid_max_value))

                    plt.plot(x_axis, collect_mean_ask, color='red', linewidth=0.5)

                    for i in sold_data:  
                        # plt.text(i, sold_data[i] + 150, 'SOLD', color='blue') 
                        plt.scatter(i, sold_data[i], color='green')

                    for i in buy_data:   
                        # plt.text(i, buy_data[i] + 150, 'BUY', color='red') 
                        plt.scatter(i, buy_data[i], color='red')


                    plt.savefig(img_path_askprice_avarage, transparent=True)

                    # # composit images
                    img_ask_avg = Image.open(img_path_askprice_avarage)
                    img_width, img_height = img_ask_avg.size

                    img_color_backround = Image.new('RGBA', (img_width, img_height), (75, 75, 75))
                    Image.alpha_composite(img_color_backround, img_ask_avg).save(config["TurtleTurtle_path"] + "/data/backtest/graphs/" + bot + '_' + str(count) + "_BACKTEST.png")

                    # playsound(PATH_TURTLE_AUDIO_DIR + '/tiky_07.wav')

                    # cleanup
                    os.remove(img_path_askprice_avarage)

                except TypeError as e:
                    print(e)

















def plot_graph_live(config):
    """ This plots a graph of the live market """


    BackTest_Active = config["BackTest_Active"]

    VALR_active_bots = config["VALR_active_bots"]
    # LUNO_active_bots = config["LUNO_active_bots"]


    active_bots = {}
    # active_bots.update(LUNO_active_bots)
    active_bots.update(VALR_active_bots)


    if BackTest_Active == True:
        data_plot = Global_BackTest.data_calc
    elif BackTest_Active == False:
        data_plot = Global_Live.data_calc



    for bot in active_bots:

        status = active_bots[bot]["status"]
        Plot_graph = active_bots[bot]["Plot_graph"]

        if status != 'hold':
            if Plot_graph == True:

                collect_data_bid = data_plot[bot]["collect_data_bid"]
                one_min_collection_bid = data_plot[bot]["one_min_collection_bid"]
                one_min_collection_short_bid = data_plot[bot]["one_min_collection_short_bid"]

                long_avg = data_plot[bot]["long_avg"]
                output_value_bid = data_plot[bot]["output_value_bid"]
                output_value_short_bid = data_plot[bot]["output_value_short_bid"]

                collect_data_ask = data_plot[bot]["collect_data_ask"]
                one_min_collection_ask = data_plot[bot]["one_min_collection_ask"]
                output_value_ask = data_plot[bot]["output_value_ask"]

                degrees = data_plot[bot]["degrees"]
                x_collect = data_plot[bot]["x_collect_plot"]
                x_regress_values = data_plot[bot]["x_regress_values"]

                calc_linregress = data_plot[bot]["calc_linregress"]
                long_bid = data_plot[bot]["long_bid"]
                ask_long_range = data_plot[bot]["ask_long_range"]

                ask_range = data_plot[bot]["ask_range"]
                bid_range = data_plot[bot]["bid_range"]

                long_regression_len = data_plot[bot]["long_regression_len"]

                long_regression_len_new = data_plot[bot]["long_regression_len_new"]
                x_regress_values_new = data_plot[bot]["x_regress_values_new"]
                calc_linregress_new = data_plot[bot]["calc_linregress_new"]

                collect_mean_ask = data_plot[bot]["collect_mean_ask"]
                collect_mean_bid = data_plot[bot]["collect_mean_bid"]
                collect_long = data_plot[bot]["collect_long"]

                sold_data = data_plot[bot]["sold_data"]
                buy_data = data_plot[bot]["buy_data"]


                x_axis = []

                count = 0
                for i in x_collect:
                    count += 1
                    x_axis.append(count)



                x_regress = numpy.array(x_regress_values)[long_regression_len:]

                x_regress_new = numpy.array(x_regress_values_new)[long_regression_len_new:]


                ask_min_value = min(collect_data_ask)
                ask_max_value = max(collect_data_ask)

                bid_min_value = min(collect_data_bid)
                bid_max_value = max(collect_data_bid)

                day = str(datetime.datetime.now())
                day_date = day.split(' ')[0]

                img_path_long_avarage = config["TurtleTurtle_path"] + "/data/active_stats/general/graph_live/" + str(day_date) + '.png'
                img_path_askprice_avarage = config["TurtleTurtle_path"] + "/data/active_stats/general/graph_live/" + str(day_date) + '.png'

                ## BID
                # plot bidprice
                plt.title('test')
                plt.xlabel('time')
                plt.xticks(rotation=0)
                plt.ylabel('value')
                plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
                ee = plt.gcf()
                ee.set_size_inches(65, 10)

                fig, ax = plt.subplots()
                # # ax.scatter(x_regress_values, y)
                ax.plot(x_regress, calc_linregress["calc_linregress"], color='lime', linewidth=1)
                # # plot EXTERNAL MAIN LINEAR REGRESSION
                ax.plot(x_regress_new, calc_linregress_new["calc_linregress"], color='magenta', linewidth=1)

                # bid
                plt.ylim(float(bid_min_value), float(bid_max_value))
                plt.plot(x_axis, collect_data_bid, color="blue", linewidth=0.7)

                # # plot avarage_bidprice
                plt.ylim(float(bid_min_value), float(bid_max_value))
                    
                # plt.plot(x_axis, collect_mean_bid, color="navy", linewidth=0.5)

                # # # plot avarage_long
                # plt.ylim(float(bid_min_value), float(bid_max_value))
                    
                # plt.plot(x_axis, collect_long, color="yellow", linewidth=0.5)

                ## ASK
                plt.ylim(float(bid_min_value), float(bid_max_value))
                plt.plot(x_axis, collect_data_ask, color='darkred', linewidth=0.7)

                # # plot avarage_askprice
                ee = plt.gcf()
                ee.set_size_inches(65, 10)

                # plt.ylim(float(bid_min_value), float(bid_max_value))

                # plt.plot(x_axis, collect_mean_ask, color='red', linewidth=0.5)

                # for i in sold_data:  
                #     # plt.text(i, sold_data[i] + 150, 'SOLD', color='blue') 
                #     plt.scatter(i, sold_data[i], color='green')

                # for i in buy_data:   
                #     # plt.text(i, buy_data[i] + 150, 'BUY', color='red') 
                #     plt.scatter(i, buy_data[i], color='red')


                plt.savefig(img_path_askprice_avarage, transparent=True)

                # # composit images
                img_ask_avg = Image.open(img_path_askprice_avarage)
                img_width, img_height = img_ask_avg.size

                img_color_backround = Image.new('RGBA', (img_width, img_height), (85, 85, 85))
                Image.alpha_composite(img_color_backround, img_ask_avg).save(config["TurtleTurtle_path"] + "/data/active_stats/general/graph_live/" + bot + "_LIVE.png")

                # playsound(PATH_TURTLE_AUDIO_DIR + '/tiky_07.wav')

                # cleanup
                os.remove(img_path_askprice_avarage)











def plot_graph(config):
    """ This plots a graph of the backtesting """


    BackTest_Active = config["BackTest_Active"]

    VALR_active_bots = config["VALR_active_bots"]
    # LUNO_active_bots = config["LUNO_active_bots"]


    active_bots = {}
    # active_bots.update(LUNO_active_bots)
    active_bots.update(VALR_active_bots)



    if BackTest_Active == True:
        data_plot = Global_BackTest.data_calc
    elif BackTest_Active == False:
        data_plot = Global_Live.data_calc



    for bot in active_bots:

        status = active_bots[bot]["status"]
        Plot_graph = active_bots[bot]["Plot_graph"]

        if status != 'hold':
            if Plot_graph == True:


                

                collect_data_bid = data_plot[bot]["collect_data_bid"]
                one_min_collection_bid = data_plot[bot]["one_min_collection_bid"]
                one_min_collection_short_bid = data_plot[bot]["one_min_collection_short_bid"]

                long_avg = data_plot[bot]["long_avg"]
                output_value_bid = data_plot[bot]["output_value_bid"]
                output_value_short_bid = data_plot[bot]["output_value_short_bid"]

                collect_data_ask = data_plot[bot]["collect_data_ask"]
                one_min_collection_ask = data_plot[bot]["one_min_collection_ask"]
                output_value_ask = data_plot[bot]["output_value_ask"]

                degrees = data_plot[bot]["degrees"]
                x_collect = data_plot[bot]["x_collect_plot"]
                x_regress_values = data_plot[bot]["x_regress_values"]

                calc_linregress = data_plot[bot]["calc_linregress"]
                long_bid = data_plot[bot]["long_bid"]
                ask_long_range = data_plot[bot]["ask_long_range"]

                ask_range = data_plot[bot]["ask_range"]
                bid_range = data_plot[bot]["bid_range"]

                long_regression_len = data_plot[bot]["long_regression_len"]

                long_regression_len_new = data_plot[bot]["long_regression_len_new"]
                x_regress_values_new = data_plot[bot]["x_regress_values_new"]
                calc_linregress_new = data_plot[bot]["calc_linregress_new"]

                collect_mean_ask = data_plot[bot]["collect_mean_ask"]
                collect_mean_bid = data_plot[bot]["collect_mean_bid"]
                collect_long = data_plot[bot]["collect_long"]

                sold_data = data_plot[bot]["sold_data"]
                buy_data = data_plot[bot]["buy_data"]


                x_axis = []

                count = 0
                for i in x_collect:
                    count += 1
                    x_axis.append(count)



                x_regress = numpy.array(x_regress_values)[long_regression_len:]

                x_regress_new = numpy.array(x_regress_values_new)[long_regression_len_new:]


                ask_min_value = min(collect_data_ask)
                ask_max_value = max(collect_data_ask)

                bid_min_value = min(collect_data_bid)
                bid_max_value = max(collect_data_bid)

                day = str(datetime.datetime.now())
                day_date = day.split(' ')[0]

                img_path_long_avarage = config["TurtleTurtle_path"] + "/data/backtest/graphs/" + str(day_date) + '.png'
                img_path_askprice_avarage = config["TurtleTurtle_path"] + "/data/backtest/graphs/" + str(day_date) + '.png'


                try:
                    ## BID
                    # plot bidprice
                    plt.title('test')
                    plt.xlabel('time')
                    plt.xticks(rotation=0)
                    plt.ylabel('value')
                    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
                    ee = plt.gcf()
                    ee.set_size_inches(65, 10)

                    fig, ax = plt.subplots()
                    # # ax.scatter(x_regress_values, y)
                    ax.plot(x_regress, calc_linregress["calc_linregress"], color='lime', linewidth=1)
                    # # plot EXTERNAL MAIN LINEAR REGRESSION
                    ax.plot(x_regress_new, calc_linregress_new["calc_linregress"], color='magenta', linewidth=1)

                    # bid
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                    plt.plot(x_axis, collect_data_bid, color="blue", linewidth=0.05)

                    # # plot avarage_bidprice
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                        
                    plt.plot(x_axis, collect_mean_bid, color="navy", linewidth=0.5)

                    # # plot avarage_long
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                        
                    plt.plot(x_axis, collect_long, color="yellow", linewidth=0.5)

                    ## ASK
                    plt.ylim(float(bid_min_value), float(bid_max_value))
                    plt.plot(x_axis, collect_data_ask, color='darkred', linewidth=0.05)

                    # # plot avarage_askprice
                    ee = plt.gcf()
                    ee.set_size_inches(65, 10)

                    plt.ylim(float(bid_min_value), float(bid_max_value))

                    plt.plot(x_axis, collect_mean_ask, color='red', linewidth=0.5)

                    for i in sold_data:  
                        # plt.text(i, sold_data[i] + 150, 'SOLD', color='blue') 
                        plt.scatter(i, sold_data[i], color='green')

                    for i in buy_data:   
                        # plt.text(i, buy_data[i] + 150, 'BUY', color='red') 
                        plt.scatter(i, buy_data[i], color='red')


                    plt.savefig(img_path_askprice_avarage, transparent=True)

                    # # composit images
                    img_ask_avg = Image.open(img_path_askprice_avarage)
                    img_width, img_height = img_ask_avg.size

                    img_color_backround = Image.new('RGBA', (img_width, img_height), (75, 75, 75))
                    Image.alpha_composite(img_color_backround, img_ask_avg).save(config["TurtleTurtle_path"] + "/data/backtest/graphs/" + bot + "_BACKTEST.png")

                    # playsound(PATH_TURTLE_AUDIO_DIR + '/tiky_07.wav')

                    # cleanup
                    os.remove(img_path_askprice_avarage)

                except TypeError as e:
                    print(e)