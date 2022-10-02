import os
import sys

import Valr.libs.utils.toolUtils as utils
import Valr.libs.globals.Global_utils as Global_utils

# VALR
# Bot imports
import Valr.bots.valr.Market_eval as Market_eval

# algo bots
import Valr.bots.valr.bot_AAA as bot_AAA
import Valr.bots.valr.bot_BBB as bot_BBB
import Valr.bots.valr.bot_CCC as bot_CCC

# play
import Valr.bots.valr.bot_play_xrp as bot_play_xrp



def Run_Bot(config, Bot_Name, LIVE_MARKET_DATA, collected_data, count):
    """ 3 This executes the bot """


    # Rember to import the new bot name at the top !!!


# VALR


#### Manual play around bots
    if Bot_Name == 'bot_play_xrp':

        status = config['VALR_active_bots'][Bot_Name]['status']
        if status == 'hold':
            pass

        else:
            Global_utils.pre_store_to_global(config, Bot_Name, collected_data, LIVE_MARKET_DATA)
            bot_play_xrp.run_bot(
                            config, 
                            Bot_Name,
                            LIVE_MARKET_DATA,
                            collected_data,
                            count
                            )



    if Bot_Name == 'bot_AAA':

        status = config['VALR_active_bots'][Bot_Name]['status']
        if status == 'hold':
            pass

        else:
            Global_utils.pre_store_to_global(config, Bot_Name, collected_data, LIVE_MARKET_DATA)
            bot_AAA.run_bot(
                            config, 
                            Bot_Name,
                            LIVE_MARKET_DATA,
                            collected_data,
                            count
                            )



    if Bot_Name == 'bot_BBB':

        status = config['VALR_active_bots'][Bot_Name]['status']
        if status == 'hold':
            pass

        else:
            Global_utils.pre_store_to_global(config, Bot_Name, collected_data, LIVE_MARKET_DATA)
            bot_BBB.run_bot(
                            config, 
                            Bot_Name, 
                            LIVE_MARKET_DATA,
                            collected_data,
                            count
                            )



    if Bot_Name == 'bot_CCC':

        status = config['VALR_active_bots'][Bot_Name]['status']
        if status == 'hold':
            pass

        else:
            Global_utils.pre_store_to_global(config, Bot_Name, collected_data, LIVE_MARKET_DATA)
            bot_CCC.run_bot(
                            config, 
                            Bot_Name, 
                            LIVE_MARKET_DATA,
                            collected_data,
                            count
                            )





#####################################################################

#### ASSISTANT BOTS
    if Bot_Name == 'Market_eval':

        status = config['VALR_active_bots'][Bot_Name]['status']
        if status == 'hold':
            pass

        else:
            Global_utils.pre_store_to_global(config, Bot_Name, collected_data, LIVE_MARKET_DATA)
            Market_eval.run_bot(
                            config, 
                            Bot_Name, 
                            LIVE_MARKET_DATA,
                            collected_data,
                            count
                            )









if __name__ == '__main__':

    Bot_Name = 'BudahBoss_bot'
    LIVE_MARKET_DATA = None
    config = utils.yaml_config("D:/work/projects/dev/projects/TurtleTurtle_v4/config.yaml")

    Run_Bot(Bot_Name, LIVE_MARKET_DATA, config)