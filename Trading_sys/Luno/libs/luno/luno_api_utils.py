import os

import Luno.libs.luno.luno_api_utils as utils

from luno_python.client import Client



key = os.getenv('LUNO_API_KEY')
key_secret = os.getenv('LUNO_API_KEY_SECRET')

time_delay = 1
coin_pair = 'XRPZAR'

connection = Client(api_key_id=key, api_key_secret=key_secret)





# def check_market(coin_pair, asset_type):
#     """ Returns the markets values """

#     try:
#         market_info = connection.get_ticker(pair=coin_pair)
#         value = (market_info['bid'].split('.')[0])
#         my_balance = get_my_balance(asset_type)['balance'][0]['balance']
        
#         time_now = (str(datetime.datetime.now()).split('.')[0])

#         total = float(my_balance) * int(value)

#         print(f'{time_now} || market info || {coin_pair} - value = R{value} - my_eth_wallet_value = R{int(total)} // eth {my_balance}')

#     except Exception as error:
#         print(error)
        
#     return(market_info, value, my_balance, total)
    



def get_my_balance(asset_type):
    """ returns my balances for my wallets """

    balance = connection.get_balances(assets=asset_type)
    return(balance)





def calculate_fee(amount_of_coins, coin_pair):
    """ This hopefully returns an accurate fee for a transaction """

    current_coin_value = check_market(coin_pair)[coin_pair]['bid']
    
    fee_taker = connection.get_fee_info(pair=coin_pair)['taker_fee']
    calc_fee = float(fee_taker) * float(amount_of_coins) * (float(current_coin_value))
    #print(float(fee_taker) * 512 * 9.40)

    print(float(amount_of_coins) * float(current_coin_value))

    return(calc_fee)





def buy_sell_coin(coin_pair, buy_or_sell, counter_buy_amount, base_sell_amount):

    if buy_or_sell == 'BUY':
        buy = connection.post_market_order(pair=coin_pair, type='BUY', counter_volume=str(counter_buy_amount))
        print(buy)
    elif buy_or_sell == 'SELL':
        sell = connection.post_market_order(pair=coin_pair, type='SELL', base_volume=str(base_sell_amount))
        print(sell)






def BUY_market(input_coin='XRP'):
    """ buy from zar to xrp """

    if input_coin == 'XRP':
        coin = 'XRP'
        coinPair = 'XRPZAR'

    elif input_coin == 'ETH':
        coin = 'ETH'
        coinPair = 'ETHZAR'

    elif input_coin == 'BTC':
        coin = 'BTC'
        coinPair = 'BTCZAR'

    ZAR_wallet = connection.get_balances(assets='ZAR')['balance'][0]['balance']

    try:
        connection.post_market_order(pair=coinPair, type='BUY', counter_volume=str(ZAR_wallet)) # transaction2
    except Exception as error:
        print(error)
        print('Failed, second attempt transfering to ZAR to XRP')





def SELL_market(input_coin='XRP'):
    """ Function to sell out of a wallet """

    if input_coin == 'XRP':
        coin = 'XRP'
        coinPair = 'XRPZAR'

    elif input_coin == 'ETH':
        coin = 'ETH'
        coinPair = 'ETHZAR'

    elif input_coin == 'BTC':
        coin = 'BTC'
        coinPair = 'BTCZAR'

    COIN_wallet = connection.get_balances(assets=coin)['balance'][0]['balance']

    print('SELLING ||  || ' + str(input_coin))
    try:
        connection.post_market_order(pair=coinPair, type='SELL', base_volume=str(COIN_wallet)) # transaction2
    except Exception as error:
        print(error)
        print('Failed, second attempt transfering to ' + coin + ' to ZAR')





def check_market():
    """ Returns values in my luno account and the market """

    try:
        # Get market info pairs
        market_info_BTC = connection.get_ticker(pair='XBTZAR')
        market_info_ETH = connection.get_ticker(pair='ETHZAR')
        market_info_XRP = connection.get_ticker(pair='XRPZAR')


        # market value per coin
        btc_ask = (market_info_BTC['ask'])
        btc_bid = (market_info_BTC['bid'])
        btc_pair = (market_info_BTC['pair'])

        eth_ask = (market_info_ETH['ask'])
        eth_bid = (market_info_ETH['bid'])
        eth_pair = (market_info_ETH['pair'])

        xrp_ask = (market_info_XRP['ask'])
        xrp_bid = (market_info_XRP['bid'])
        xrp_pair = (market_info_XRP['pair'])


    except Exception as error:
        print(error)


    clean_data = {}

    clean_data["BTCZAR"] = {'currencyPair' : "BTCZAR", 
                                    "askPrice": btc_ask, 
                                    "bidPrice": btc_bid, 
                                    "highPrice": 0,
                                    "lowPrice": 0,                                    
                                    }

    clean_data["ETHZAR"] = {'currencyPair' : "ETHZAR", 
                                    "askPrice": eth_ask, 
                                    "bidPrice": eth_bid, 
                                    "highPrice": 0,
                                    "lowPrice": 0,                                    
                                    }

    clean_data["XRPZAR"] = {'currencyPair' : "XRPZAR", 
                                    "askPrice": xrp_ask, 
                                    "bidPrice": xrp_bid, 
                                    "highPrice": 0,
                                    "lowPrice": 0,                                    
                                    }





    return(clean_data)




if __name__ == '__main__':


    print(check_market())

