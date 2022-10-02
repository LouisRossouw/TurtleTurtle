import os
import sys

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v5")
sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v5/Trading_sys")

platform = sys.platform
if platform == 'win32':
    sys.path.append(os.getenv("Turtle"))
elif platform == 'linux':
    sys.path.append(os.getenv("Turtle"))


# LocaL Exchanges
import Trading_sys.Valr.libs.valr.valr_api_tools as VALR
import Trading_sys.Luno.libs.luno.luno_api_utils as LUNO

# International Exchanges
import Trading_sys.CoinBase.libs.CoinBase_api_utils as COINBASE

import utils.ToolUtils as ToolUtils


def market_all(config_main):
    """ Collects all markets data now for arbitrage """


    # PATHS
    Path_main = config_main["TurtleTurtle_path"]
    
    # Local
    Valr_data_path = Path_main + '/Arbitrage_sys/ARBA/data/Markets_now/Local_Exchanges/Valr/Valr_data_now.json'
    Luno_data_path = Path_main + '/Arbitrage_sys/ARBA/data/Markets_now/Local_Exchanges/Luno/Luno_data_now.json'

    # International
    CoinBase_data_path = Path_main + '/Arbitrage_sys/ARBA/data/Markets_now/International_Exchanges/CoinBase/CoinBase_data_now.json'






    # get CoinBase
    COINBASE_MARKET = COINBASE.check_market()
    ToolUtils.write_to_json(CoinBase_data_path, COINBASE_MARKET)

    # get Valr
    VALR_MARKET = VALR.get_valr_market()
    ToolUtils.write_to_json(Valr_data_path, VALR_MARKET)

    # Luno
    LUNO_MARKET = LUNO.check_market()
    ToolUtils.write_to_json(Luno_data_path, LUNO_MARKET)











if __name__ == '__main__':



    config_main = ToolUtils.yaml_config("D:/work/projects/dev/projects/TurtleTurtle_v5/config_main.yaml")
    market_all(config_main)