import os
import sys
import time

platform = sys.platform
if platform == 'win32':
    os.environ["Turtle"] = "D:/work/projects/dev/projects/TurtleTurtle"
    sys.path.append(os.getenv("Turtle"))
elif platform == 'linux':
    os.environ["Turtle"] = "/home/pi/Desktop/TurtleTurtle"
    sys.path.append(os.getenv("Turtle"))

# Import Utils
import utils.ToolUtils as ToolUtils

# Trading Systems
import Trading_sys.Valr.Valr_Trading_Run as Valr_RUN
import Trading_sys.Luno.Luno_Trading_Run as Luno_RUN

# Arbitrage Systems
import Arbitrage_sys.ARBA.Arba_Run as Arba_Run

# Whale Systems
import Whale_sys.Whale_Alert.Whale_Run as Whale_Run











def Run_TurtleTurtle():
    """ This Runs the Main System """

    config_main = ToolUtils.yaml_config(os.getenv("Turtle") + "/config_main.yaml")






######## Trading Sys ##################################################################
    if config_main["valr_sys_active"] == True:
        Valr_RUN.run(config_main)

    if config_main["luno_sys_active"] == True:
        Luno_RUN.run(config_main)


######## Arbitrage Sys ################################################################

    if config_main["arba_sys_active"] == True:
        Arba_Run.arbitrage_run(config_main)


######## Whale Sys ####################################################################

    if config_main["whale_sys"] == True:
        whale_data = Whale_Run.get_whale(config_main)
        Whale_Run.whale_record_data('count', config_main, whale_data)





if __name__ == '__main__':

    Run_TurtleTurtle()
