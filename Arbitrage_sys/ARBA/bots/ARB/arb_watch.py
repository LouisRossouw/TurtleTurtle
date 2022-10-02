""" This Bot calculates arbitrage opportunities between exchanges """

import os

import utils.ToolUtils as ToolUtils
# import libs.utils.collect_historical_data as collect_historical_data






def price_spread_coinbase(valr, coinbase):
    """ Gets the price difference between coinbase / valr """

    exchanges_group = []
    exchanges_group.append(coinbase)
    exchanges_group.append(valr)

    exchange_min = min(exchanges_group)
    exchange_max = max(exchanges_group)

    spread = exchange_max - exchange_min

    if exchange_max == coinbase:
        buy_low_on = 'valr'
        sell_high_on = 'coinbase'
    else:
        buy_low_on = 'coinbase'
        sell_high_on = 'valr' 

    spread_clean = round(spread,2)

    return(spread_clean, buy_low_on, sell_high_on)




def get_spread(luno, valr):
    """ Gets the price difference between luno / valr """

    exchanges_group = []
    exchanges_group.append(luno)
    exchanges_group.append(valr)

    exchange_min = min(exchanges_group)
    exchange_max = max(exchanges_group)

    spread = exchange_max - exchange_min

    if exchange_max == luno:
        buy_low_on = 'valr'
        sell_high_on = 'luno'
    else:
        buy_low_on = 'luno'
        sell_high_on = 'valr' 

    spread_clean = round(spread,2)

    return(spread_clean, buy_low_on, sell_high_on)





def arb_watcher(config_main):
    """ Calculates and returns the price differences using historical data that gets recorded every 10 seconds """

    TurtleTurtle_path = config_main["TurtleTurtle_path"]

    
    # Local
    Valr_data_path = TurtleTurtle_path + '/Arbitrage_sys/ARBA/data/Markets_now/Local_Exchanges/Valr/Valr_data_now.json'
    Luno_data_path = TurtleTurtle_path + '/Arbitrage_sys/ARBA/data/Markets_now/Local_Exchanges/Luno/Luno_data_now.json'

    # International
    CoinBase_data_path = TurtleTurtle_path + '/Arbitrage_sys/ARBA/data/Markets_now/International_Exchanges/CoinBase/CoinBase_data_now.json'

    read_luno_data = ToolUtils.read_json(Luno_data_path)
    read_valr_data = ToolUtils.read_json(Valr_data_path)
    read_coinbase_data = ToolUtils.read_json(CoinBase_data_path)



#               # GET data from historical recorded data #              #                   #                   #                   #                   #
# LUNO
    BTC_luno_askPrice = float(read_luno_data["BTCZAR"]["askPrice"])
    BTC_luno_bidPrice = float(read_luno_data["BTCZAR"]["bidPrice"])

    ETH_luno_askPrice = float(read_luno_data["ETHZAR"]["askPrice"])
    ETH_luno_bidPrice = float(read_luno_data["ETHZAR"]["bidPrice"])

    XRP_luno_askPrice = float(read_luno_data["XRPZAR"]["askPrice"])
    XRP_luno_bidPrice = float(read_luno_data["XRPZAR"]["bidPrice"])



# VALR
    BTC_valr_askPrice = float(read_valr_data["BTCZAR"]["askPrice"])
    BTC_valr_bidPrice = float(read_valr_data["BTCZAR"]["bidPrice"])

    ETH_valr_askPrice = float(read_valr_data["ETHZAR"]["askPrice"])
    ETH_valr_bidPrice = float(read_valr_data["ETHZAR"]["bidPrice"])

    XRP_valr_askPrice = float(read_valr_data["XRPZAR"]["askPrice"])
    XRP_valr_bidPrice = float(read_valr_data["XRPZAR"]["bidPrice"])

    SOL_valr_askPrice = float(read_valr_data["SOLZAR"]["askPrice"])
    SOL_valr_bidPrice = float(read_valr_data["SOLZAR"]["bidPrice"])



# COINBASE
    BTC_coinbase_askPrice = float(read_coinbase_data["BTCZAR"]["askPrice"])
    BTC_coinbase_bidPrice = float(read_coinbase_data["BTCZAR"]["bidPrice"])

    ETH_coinbase_askPrice = float(read_coinbase_data["ETHZAR"]["askPrice"])
    ETH_coinbase_bidPrice = float(read_coinbase_data["ETHZAR"]["bidPrice"])

    SOL_coinbase_askPrice = float(read_coinbase_data["SOLZAR"]["askPrice"])
    SOL_coinbase_bidPrice = float(read_coinbase_data["SOLZAR"]["bidPrice"])





#           # SPREAD | calculate the price differences between all the exchanges #              #                   #                   #                   #

# local exchanges in South Africa

# LUNO >>> VALR:

    btc_ASK_spread_LV = get_spread(BTC_luno_askPrice, BTC_valr_askPrice)
    btc_BID_spread_LV = get_spread(BTC_luno_bidPrice, BTC_valr_bidPrice)
    btc_buy_spread_LV = get_spread(BTC_luno_askPrice, BTC_valr_bidPrice)

    eth_ASK_spread_LV = get_spread(ETH_luno_askPrice, ETH_valr_askPrice)
    eth_BID_spread_LV = get_spread(ETH_luno_bidPrice, ETH_valr_bidPrice)
    eth_buy_spread_LV = get_spread(ETH_luno_askPrice, ETH_valr_bidPrice)

    xrp_ASK_spread_LV = get_spread(XRP_luno_askPrice, XRP_valr_askPrice)
    xrp_BID_spread_LV = get_spread(XRP_luno_bidPrice, XRP_valr_bidPrice)
    xrp_buy_spread_LV = get_spread(XRP_luno_askPrice, XRP_valr_bidPrice)





# Global - international exchanges around the world

# LUNO/VALR >>> COINBASE:

    #   ARBITRAGE difference in ZAR | ask >> bid

    btc_valr_and_coinbase_SPREAD = price_spread_coinbase(BTC_valr_bidPrice, BTC_coinbase_askPrice)
    eth_valr_and_coinbase_SPREAD = price_spread_coinbase(ETH_valr_bidPrice, ETH_coinbase_askPrice)
    sol_valr_and_coinbase_SPREAD = price_spread_coinbase(SOL_valr_bidPrice, SOL_coinbase_askPrice)


    #   ARBITRAGE difference in ZAR | ask >> bid

    btc_valr_and_coinbase_SPREAD_PERCENTAGE = ToolUtils.get_percentage_difference(BTC_valr_bidPrice, BTC_coinbase_askPrice)
    eth_valr_and_coinbase_SPREAD_PERCENTAGE = ToolUtils.get_percentage_difference(ETH_valr_bidPrice, ETH_coinbase_askPrice)
    sol_valr_and_coinbase_SPREAD_PERCENTAGE = ToolUtils.get_percentage_difference(SOL_valr_bidPrice, SOL_coinbase_askPrice)








                    # STORE DATA IN DICT
    data = {}

    data["LOCAL_ARB"] = {"local_luno_valr_BTC" : btc_buy_spread_LV,
                         "local_luno_valr_ETH" : eth_buy_spread_LV,
                         "local_luno_valr_XRP" : xrp_buy_spread_LV,
                        }



    data["GLOBAL_ARB"] = {"global_valr_coinbase_BTC" : [btc_valr_and_coinbase_SPREAD, btc_valr_and_coinbase_SPREAD_PERCENTAGE],
                         "global_valr_coinbase_ETH" : [eth_valr_and_coinbase_SPREAD, eth_valr_and_coinbase_SPREAD_PERCENTAGE],
                         "global_valr_coinbase_SOL" : [sol_valr_and_coinbase_SPREAD, sol_valr_and_coinbase_SPREAD_PERCENTAGE],
                        }








                    # WRITE / UPDATE FILE

    path_dir = TurtleTurtle_path + '/Arbitrage_sys/ARBA/data/Markets_Arbitrage_Calculations'
    path_to_json = path_dir + '/arbitrage_data.json'

    if os.path.exists(path_dir) != True:
        os.mkdir(path_dir)

    ToolUtils.write_to_json(path_to_json, data)












if __name__ == '__main__':

    
    config_path = ("D:/work/projects/dev/projects/TurtleTurtle_v4") + '/config.yaml'
    config = ToolUtils.yaml_config(config_path)


    arb_watcher(config)