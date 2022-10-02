" Documentation at - https://github.com/coinbase/coinbase-python "

import os

from coinbase.wallet.client import Client




key = os.getenv('COINBASE_API_KEY')
key_secret = os.getenv('COINBASE_API_KEY_SECRET')

coinbase = Client(key, key_secret)



# user = coinbase.get_current_user()
# user_as_json_string = json.dumps(user)

# accounts = coinbase.get_accounts() # api key disabled for 48 hours


currencies = coinbase.get_currencies()


exchange_rate = coinbase.get_exchange_rates()


buy_price = coinbase.get_buy_price(currency_pair = 'ETH-ZAR')
sell_price = coinbase.get_sell_price(currency_pair = 'ETH-ZAR')
spot_price = coinbase.get_spot_price(currency_pair = 'ETH-ZAR')

# server_time = coinbase.get_time()

# auth_info = coinbase.get_auth_info()
# current_user = coinbase.get_current_user()


# Send Money to other wallet addresses outside of coinbase 
# coinbase.send_money(
#     account_id,
#     to="account address",
#     amount="0.01",
#     currency="ETH")

# Transfer money in coinbase
# coinbase.transfer_money(
#     account_id,
#     to="<coinbase_account_id>",
#     amount="1",
#     currency="BTC")








def check_market():
    """ Returns values in my luno account and the market """

    try:
        # Get market info pairs
        
        # BITCOIN
        btc_buy_price = coinbase.get_buy_price(currency_pair = 'BTC-ZAR')["amount"]
        btc_sell_price = coinbase.get_sell_price(currency_pair = 'BTC-ZAR')["amount"]
        btc_spot_price = coinbase.get_spot_price(currency_pair = 'BTC-ZAR')["amount"]

        # ETH
        eth_buy_price = coinbase.get_buy_price(currency_pair = 'ETH-ZAR')["amount"]
        eth_sell_price = coinbase.get_sell_price(currency_pair = 'ETH-ZAR')["amount"]
        eth_spot_price = coinbase.get_spot_price(currency_pair = 'ETH-ZAR')["amount"]


        # SOL
        sol_buy_price = coinbase.get_buy_price(currency_pair = 'SOL-ZAR')["amount"]
        sol_sell_price = coinbase.get_sell_price(currency_pair = 'SOL-ZAR')["amount"]





    except Exception as error:
        print(error)


    clean_data = {}

    clean_data["BTCZAR"] = {'currencyPair' : "BTCZAR", 
                                    "askPrice": btc_buy_price, 
                                    "bidPrice": btc_sell_price, 
                                    "highPrice": 0,
                                    "lowPrice": 0,                                    
                                    }

    clean_data["ETHZAR"] = {'currencyPair' : "ETHZAR", 
                                    "askPrice": eth_buy_price, 
                                    "bidPrice": eth_sell_price, 
                                    "highPrice": 0,
                                    "lowPrice": 0,                                    
                                    }


    clean_data["SOLZAR"] = {'currencyPair' : "SOLAR", 
                                    "askPrice": sol_buy_price, 
                                    "bidPrice": sol_sell_price, 
                                    "highPrice": 0,
                                    "lowPrice": 0,                                    
                                    }



    return(clean_data)





if __name__ == '__main__':


    check_market()