import os
import sys
import time

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v5")
sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v5/Trading_sys")

platform = sys.platform
if platform == 'win32':
    sys.path.append(os.getenv("Turtle"))
elif platform == 'linux':
    sys.path.append(os.getenv("Turtle"))


import Luno.libs.luno.luno_api_utils as luno

import Luno.libs.utils.toolUtils as ToolUtils
import Luno.libs.utils.collect_historical_data as collect_data
import Luno.libs.TurtleTurtle_utils as BOT_RUN
import Luno.libs.utils.record_data as record_datas

import Luno.libs.globals.Global_utils as Global_utils
import Luno.libs.globals.Global_Live as Global_Live
import Luno.libs.globals.Global_BackTest as Global_BackTest

import Luno.libs.utils.plot as Plotter




def run(config_main):
    """ 1 starts and runs the program """


    config_path = config_main["luno_config_path"] + '/config.yaml'
    config = ToolUtils.yaml_config(config_path)

    PATH_TURTLE_DIR = config['TurtleTurtle_path']
    BACKTEST_ACTIVE = config['BackTest_Active']
    BOTS_DIR = PATH_TURTLE_DIR + '/bots'
    LIVE_speed = 0
    BACKTEST_speed = 0

    luno_record_market = config['luno_record_market']


    for market_dir in os.listdir(BOTS_DIR):
        exchange_dir = os.listdir(PATH_TURTLE_DIR + '/bots/' + market_dir)




# LUNO
        if market_dir == 'luno':

            #collect data
            year=['2022']
            days = ['12_Tuesday', '13_Wednesday', '14_Thursday', '15_Friday', '16_Saturday']
            collected_data = collect_data.collect_historical_data(config, 'luno', year_input=year)[2]
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
                LIVE_MARKET_DATA = luno.check_market()
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
   

                # track luno market
                if luno_record_market == True:
                    try:
                        record_datas.luno_track_data(LIVE_MARKET_DATA, count, config)
                    except Exception as e:
                        print('Error record market luno json file | ' + str(e))











if __name__ == '__main__':

    config_main = ToolUtils.yaml_config("D:/work/projects/dev/projects/TurtleTurtle_v5/config_main.yaml")
    run(config_main)