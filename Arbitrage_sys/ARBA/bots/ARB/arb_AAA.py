""" ARB_AAA """


import os
import Arbitrage_sys.ARBA.libs.utils.bot_utils as bot_utils
import Arbitrage_sys.ARBA.libs.utils.toolUtils as toolUtils

import Arbitrage_sys.ARBA.bots.ARB.algo.algo_arb_AAA as ALGO





def run_bot(config):
    """ 5 Run the Bot, This is the default setup for all bots """



# Config info
    TurtleTurtle_path = config['TurtleTurtle_path']


    bot_name = os.path.basename(__file__).split('.')[0]

    bots_wallet_dir = TurtleTurtle_path + '/Arbitrage_sys/ARBA/data/bot_data/wallets/'
    bot_json = bots_wallet_dir + bot_name + '.json'


    if os.path.exists(bot_json) != True:

        wallet = {}
        wallet["capital"] = 0
        wallet["limit"] = 0
        wallet["state"] = 'local_buy'

        toolUtils.write_to_json(bot_json, wallet)


    bot_wallet = toolUtils.read_json(bot_json)


    state = bot_wallet["state"]

    if state == 'local_buy':
        print('local_buy')

        ALGO.local_buy(bot_wallet, bot_json)

        # if state is on local buy, it means the money is sitting in the valr account
        # and needs to buy an asset coin and send the money back to coinbase, where it will wait
        # until its value matches the original price it was bought for

    elif state == 'global_sell':
        print('global_sell')

        ALGO.global_sell()
        # if the state is on global sell, the money would have arrived in coinbase
        # and it is now waiting for the value to match the original price and be sold and the state will
        # change tp global_arbitrage

    elif state == 'global_arbitrage':
        print('ready for arbitrage')

        # if state is global arbitrage, it means we are now ready and waiting for
        # an arbitrage oppertunity of 2% +, when this is True, the ZAR will buy a oppertune coin
        # and send it to valr where it will be sold for a profit


# # # ####################################################################################################################################
# # # ################################ ADD CUSTOMISABLE ALGO SECTION



        path_dir = TurtleTurtle_path + '/Arbitrage_sys/ARBA/data/Markets_Arbitrage_Calculations'
        path_to_json = path_dir + '/arbitrage_data.json'

        arbitrage_data = toolUtils.read_json(path_to_json)


        # LocaL - Luno VS Valr
        # L_btc_percentage = arbitrage_data["LOCAL_ARB"]["local_luno_valr_BTC"]
        # L_btc_price_diff = arbitrage_data["LOCAL_ARB"]["local_luno_valr_BTC"]


        # GLOBAL - Coinbase VS Valr price
        G_btc_percentage = arbitrage_data["GLOBAL_ARB"]["global_valr_coinbase_BTC"][1]
        G_btc_price_diff = arbitrage_data["GLOBAL_ARB"]["global_valr_coinbase_BTC"][0][0]

        G_eth_percentage = arbitrage_data["GLOBAL_ARB"]["global_valr_coinbase_ETH"][1]
        G_eth_price_diff = arbitrage_data["GLOBAL_ARB"]["global_valr_coinbase_ETH"][0][0]

        G_sol_percentage = arbitrage_data["GLOBAL_ARB"]["global_valr_coinbase_SOL"][1]
        G_sol_price_diff = arbitrage_data["GLOBAL_ARB"]["global_valr_coinbase_SOL"][0][0]




        # Bitcoin
        if (float(G_btc_percentage) >= float(2)) and float(G_btc_percentage) < float(3):
            text = ('🔰ARBITRAGE🔆 : ⚱️BitCoin : CoinBase >to>> Valr | ' + str(G_btc_percentage) + "% | " + "R" + str(G_btc_price_diff) + " Difference")
            coin = 'BTC'
            ALGO.arb_low(config, text, coin)

        elif (float(G_btc_percentage) >= float(3)) and float(G_btc_percentage) < float(4):
            text = ('🔰💠ARBITRAGE💠 : ⚱️BitCoin : CoinBase >to>> Valr | ' + str(G_btc_percentage) + "% | " + "R" + str(G_btc_price_diff) + " Difference")
            coin = 'BTC'
            ALGO.arb_low(config, text, coin)

        elif (float(G_btc_percentage) >= float(4)):
            text = ('🔰💎🏆ARBITRAGE🏆💎 : ⚱️BitCoin : CoinBase >to>> Valr | 🥇 ' + str(G_btc_percentage) + "% | 🚀" + "R" + str(G_btc_price_diff) + " Difference 💵")
            coin = 'BTC'
            ALGO.arb_low(config, text, coin)

        else:
            pass



        # Ethereum
        if (float(G_eth_percentage) >= float(2)) and float(G_eth_percentage) < float(3):
            text = ('🔰ARBITRAGE🔆 : 🔮Ethereum : CoinBase >to>> Valr | ' + str(G_eth_percentage) + "% | " + "R" + str(G_eth_price_diff) + " Difference")
            coin = 'ETH'
            ALGO.arb_low(config, text, coin)

        elif (float(G_eth_percentage) >= float(3)) and float(G_eth_percentage) < float(4):
            text = ('🔰💠ARBITRAGE💠 : 🔮Ethereum : CoinBase >to>> Valr | ' + str(G_eth_percentage) + "% | " + "R" + str(G_eth_price_diff) + " Difference")
            coin = 'ETH'
            ALGO.arb_low(config, text, coin)

        elif (float(G_eth_percentage) >= float(4)):
            text = ('🔰💎🏆ARBITRAGE🏆💎 : 🔮Ethereum : CoinBase >to>> Valr | 🥇 ' + str(G_eth_percentage) + "% | 🚀" + "R" + str(G_eth_price_diff) + " Difference 💵")
            coin = 'ETH'
            ALGO.arb_low(config, text, coin)

        else:
            pass



        # SOLANA
        if (float(G_sol_percentage) >= float(2)) and float(G_sol_percentage) < float(3):
            text = ('🔰ARBITRAGE🔆 : 🥏Solana : CoinBase >to>> Valr | ' + str(G_sol_percentage) + "% | " + "R" + str(G_sol_price_diff) + " Difference")
            coin = 'SOL'
            ALGO.arb_low(config, text, coin)

        elif (float(G_sol_percentage) >= float(3)) and float(G_sol_percentage) < float(4):
            text = ('🔰💠ARBITRAGE💠 :🥏Solana : CoinBase >to>> Valr | ' + str(G_sol_percentage) + "% | " + "R" + str(G_sol_price_diff) + " Difference")
            coin = 'SOL'
            ALGO.arb_low(config, text, coin)

        elif (float(G_sol_percentage) >= float(4)):
            text = ('🔰💎🏆ARBITRAGE🏆💎 : 🥏Solana : CoinBase >to>> Valr | 🥇 ' + str(G_sol_percentage) + "% | 🚀" + "R" + str(G_sol_price_diff) + " Difference 💵")
            coin = 'SOL'
            ALGO.arb_low(config, text, coin)

        else:
            pass






# # # # ################################ ADD CUSTOMISABLE ALGO SECTION
# # # # ####################################################################################################################################


    # bot_utils.print_status(
    #                         config, 
    #                         Bot_Name, 
    #                         askPrice, 
    #                         bidPrice, 
    #                         trade_status, 
    #                         capital, 
    #                         Risk_mode, 
    #                         BackTest_Active, 
    #                         BackTest_Active_print_statement, 
    #                         EXTERNAL_DEGREES[0]
    #                     )




