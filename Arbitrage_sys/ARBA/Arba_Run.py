import sys

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v5")

import utils.ToolUtils as ToolUtils

import Arbitrage_sys.ARBA.market_all as Collect_all_markets
import Arbitrage_sys.ARBA.bots.ARB.arb_watch as arb_calculator

import Arbitrage_sys.ARBA.bots.ARB.arb_AAA as arb_AAA



def arbitrage_run(config_main):




    # collects all the data from the markets and write it out
    Collect_all_markets.market_all(config_main)

    # Caluclates all the data to find arbitrage oppertunities
    arb_calculator.arb_watcher(config_main)


    # Bot
    arb_AAA.run_bot(config_main)












if __name__ == '__main__':


    config_main = ToolUtils.yaml_config("D:/work/projects/dev/projects/TurtleTurtle_v5/config_main.yaml")
    arbitrage_run(config_main)