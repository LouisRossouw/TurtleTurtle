import os
import sys
import time

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle")
sys.path.append("D:/work/projects/dev/projects/TurtleTurtle/Trading_sys")

platform = sys.platform
if platform == 'win32':
    sys.path.append(os.getenv("Turtle"))
elif platform == 'linux':
    sys.path.append(os.getenv("Turtle"))

import Valr.libs.valr.valr_api_tools as valr

import Valr.libs.utils.toolUtils as ToolUtils
import Valr.libs.utils.collect_historical_data as collect_data
import Valr.libs.TurtleTurtle_utils as BOT_RUN
import Valr.libs.utils.record_data as record_datas

import Valr.libs.globals.Global_utils as Global_utils
import Valr.libs.globals.Global_Live as Global_Live
import Valr.libs.globals.Global_BackTest as Global_BackTest

import Valr.libs.utils.plot as Plotter





def run(config_main):
    """ 1 starts and runs the program """
 

    config_path = config_main["valr_config_path"] + '/config.yaml'
    config = ToolUtils.yaml_config(config_path)

    PATH_TURTLE_DIR = config['TurtleTurtle_path']
    BACKTEST_ACTIVE = config['BackTest_Active']
    BOTS_DIR = PATH_TURTLE_DIR + '/bots'
    LIVE_speed = 0
    BACKTEST_speed = 0

    valr_record_market = config['valr_record_market']


    for market_dir in os.listdir(BOTS_DIR):
        exchange_dir = os.listdir(PATH_TURTLE_DIR + '/bots/' + market_dir)


# VALR  
        if market_dir == 'valr':

            #collect data
            year=['2022']
            days = ['12_Tuesday', '13_Wednesday', '14_Thursday', '15_Friday', '16_Saturday']
            collected_data = collect_data.collect_historical_data(config, 'valr', year_input=year)[2]
            collected_data.sort()


# BackTest   
            # if Backtest is True - we sim
            if BACKTEST_ACTIVE == True:
                amount_of_data = config["Live_data_amount"]
                Global_utils.set_globals(config)
                count = 0
                for json_file in collected_data:
                    json_file_data = ToolUtils.read_json(json_file)
                    Global_BackTest.day = str(os.path.basename(json_file)).split('.')[0]

                    for tick in json_file_data:
                        # every tick gets fed to a bot
                        time.sleep(BACKTEST_speed)
                        Global_BackTest.time = str(tick).split('.')[0]
                        data = json_file_data[tick]
                        LIVE_MARKET_DATA = data
                        count += 1

                        for bot in exchange_dir:
                            bot_name = str(bot).split('.')[0]

                            # feed data to bots as if it was live
                            BOT_RUN.Run_Bot(
                                            config, 
                                            bot_name, 
                                            LIVE_MARKET_DATA,
                                            collected_data[-amount_of_data:],
                                            count
                                            )

                Plotter.plot_graph(config)





# LIVE
            elif BACKTEST_ACTIVE == False:
                count = 0
                time.sleep(LIVE_speed)
                amount_of_data = config["Live_data_amount"]
                Global_utils.set_globals(config)
                LIVE_MARKET_DATA = valr.get_valr_market()
                for bot in exchange_dir:
                    bot_name = str(bot).split('.')[0]
                    # Recieve live data every 5 seconds
                    BOT_RUN.Run_Bot(
                                    config, 
                                    bot_name, 
                                    LIVE_MARKET_DATA,
                                    collected_data[-amount_of_data:],
                                    count
                                    )



                # track VALR market
                if valr_record_market == True:
                    try:
                        record_datas.valr_track_data(LIVE_MARKET_DATA, count, config)
                    except Exception as e:
                        print('Error record market valr json file | ' + str(e))

                # # Check and plot whales
                # try:
                #     whale_data = WH.get_whale(config)
                #     WH.whale_record_data(count, config, whale_data)
                # except Exception as e:
                #     print('Error Whale alerter | ' + str(e))


                Plotter.plot_graph_live(config)
                        







if __name__ == '__main__':


    config_main = ToolUtils.yaml_config("D:/work/projects/dev/projects/TurtleTurtle_old/TurtleTurtle_v5/config_main.yaml")
    run(config_main)