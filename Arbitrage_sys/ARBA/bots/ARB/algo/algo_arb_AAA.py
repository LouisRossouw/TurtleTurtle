import Managers_sys.TeleGram_Manager.Bot_Notifier as Bot_Notifier
import utils.ToolUtils as ToolUtils
import Trading_sys.Valr.libs.valr.valr_api_tools as valr_api



def arb_low(config, text, coin):
    """ This executes arbitrage orders - COINBASE >>TO>> VALR """



    print(coin)
    print(text)
    Bot_Notifier.Arbitrage_Alert_CoinBase(config, text)








def local_buy(bot_wallet, bot_json):
    """ if state is on local buy, it means the money is sitting in the valr account
        and needs to buy an asset coin and send the money back to coinbase, where it will wait
        until its value matches the original price it was bought for 
    """

    bot_wallet["state"] = "global_sell"
    # Update wallet to new state - global_sell
    ToolUtils.write_to_json(bot_json, bot_wallet)
        


    print('local buyyyinnnng')
    # valr_api.BUY_ZAR_to_SOLANA(5)




def global_sell():
    """ if the state is on global sell, the money would have arrived in coinbase
        and it is now waiting for the value to match the original price and be sold and the state will
        change tp global_arbitrage
    """

    print('global sellliiiing when we hit the original price point')