import Luno.libs.utils.toolUtils as utils
import Luno.libs.globals.Global_utils as Global_utils

# LUNO
import Luno.bots.luno.bot_luno as bot_luno





def Run_Bot(config, Bot_Name, LIVE_MARKET_DATA, collected_data, count):
    """ 3 This executes the bot """


    # Rember to import the new bot name at the top !!!


# LUNO


    if Bot_Name == 'bot_luno':

        status = config['LUNO_active_bots'][Bot_Name]['status']
        if status == 'hold':
            pass

        else:
            Global_utils.pre_store_to_global(config, Bot_Name, collected_data, LIVE_MARKET_DATA)
            bot_luno.run_bot(
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