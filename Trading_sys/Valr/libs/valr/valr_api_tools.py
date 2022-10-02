import os
from valr_python import Client
from valr_python.exceptions import IncompleteOrderWarning

import Valr.libs.utils.toolUtils as utils

key = os.getenv('VALR_API_KEY')
key_secret = os.getenv('VALR_API_KEY_SECRET')

Valr_client = Client(api_key=key, api_secret=key_secret)
bot_01 = "944487537284722688"



def get_valr_market_SIMPLE():
    """ Collects the current market values of each currency pair - SIMPLE unformatted version """
    market = Valr_client.get_market_summary()

    return(market)





def get_valr_market():
    """ Collects the current market values of each currency pair """
    market = Valr_client.get_market_summary()

    data = {}
    for i in market:
        currencyPair = i['currencyPair']
        askPrice = i['askPrice'] 
        bidPrice = i['bidPrice']
        highPrice = i['highPrice']
        lowPrice = i['lowPrice']

        data[currencyPair] = {
                            'currencyPair' : currencyPair, 
                            'askPrice' : askPrice, 
                            'bidPrice' : bidPrice, 
                            'highPrice' : highPrice, 
                            'lowPrice' : lowPrice
                            }

    return(data)





def Valr_get_balances(type):
    """ gets my account wallets balances """
    if type == 'main':
        bal = Valr_client.get_balances()
    elif type != 'main':
        bal = Valr_client.get_balances(subaccount_id=type)
    data = {}
    for i in bal:
        currency = i['currency']
        available = i['available']
        reserved = i['reserved']
        total = i['total']
        data[currency] = {'available' : available, 'reserved' : reserved, 'total' : total}

    return(data)



def buy_zar_to_usdc(amount_in_coins, bot):
    """ BUY ZAR to USDC BOT ACCOUNT """
    coin_reduce = float(amount_in_coins)
    a = str(coin_reduce).split('.')[0]
    b = str(coin_reduce).split('.')[1]
    coin = a + '.' + b[:1]
    print('trying to buy :' + coin)
    Valr_client.post_market_order(
                        pair='USDCZAR',
                        side='BUY',
                        base_amount= str(coin),
                        subaccount_id= bot
                        )


def SELL_usdc_to_zar(amount_in_coins, bot):
    """ SELL ZAR to USDC BOT ACCOUNT """
    Valr_client.post_market_order(
                        pair='USDCZAR',
                        side='SELL',
                        base_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )




def BUY_ZAR_to_ETH(amount_in_coins, bot):
    """ BUY ZAR to ETH BOT ACCOUNT """
    # coin_reduce = float(amount_in_coins)
    # a = str(coin_reduce).split('.')[0]
    # b = str(coin_reduce).split('.')[1]
    # coin = a + '.' + b[:1]
    print('trying to buy :' + str(amount_in_coins))
    Valr_client.post_market_order(
                        pair='ETHZAR',
                        side='BUY',
                        base_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )

def SELL_ETH_to_ZAR(amount_in_coins, bot):
    """ SELL ETH to ZAR BOT ACCOUNT """  
    # just need eth balance
    Valr_client.post_market_order(
                        pair='ETHZAR',
                        side='SELL',
                        base_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )





def BUY_ZAR_to_XRP(amount_in_coins, bot):
    """ BUY ZAR to ETH BOT ACCOUNT """

    print('trying to buy :' + str(amount_in_coins))
    Valr_client.post_market_order(
                        pair='XRPZAR',
                        side='BUY',
                        base_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )

def SELL_XRP_to_ZAR(amount_in_coins, bot):
    """ SELL ETH to ZAR BOT ACCOUNT """  
    # just need eth balance
    Valr_client.post_market_order(
                        pair='XRPZAR',
                        side='SELL',
                        base_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )




def BUY_ETH_to_DAI(amount_in_coins, bot):
    """ buy ETH to DAI BOT ACCOUNT """  
    # pay amount must be eth balance
    Valr_client.post_simple_order(
                        currency_pair='DAIETH',
                        pay_in_currency='ETH',
                        side='BUY',
                        pay_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )



def SELL_DAI_to_ETH(amount_in_coins, bot):
    """ SELL DAI to ETH BOT ACCOUNT """  
    Valr_client.post_simple_order(
                        currency_pair='DAIETH',
                        pay_in_currency='DAI',
                        side='SELL',
                        pay_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )



def BUY_ZAR_to_SOLANA(amount_in_coins, bot):
    """ BUY ZAR to SOLANA BOT ACCOUNT """

    print('trying to buy :' + str(amount_in_coins))
    Valr_client.post_market_order(
                        pair='SOLZAR',
                        side='BUY',
                        base_amount= str(amount_in_coins),
                        subaccount_id= bot
                        )













if __name__ == '__main__':

    bot_01 = "944487537284722688"

    Bot_Play_XRP = "955025768003440640"
    Pocahontas_bot = '947570881745940480'
    bot_AAA = "951756907636871168"
    bot_BBB = "944487537284722688"

    # bal = Valr_get_balances(BuzzLightYear_bot)['ETH']['available']
    # bal = Valr_get_balances(Bot_Play_XRP)['ZAR']['available']
    # # bid = get_valr_market()['ETHZAR']
    # print(bal)




    dd = get_valr_market()


    print(dd["SOLZAR"])



    # ppp = Valr_client.get_subaccounts()
    # print(ppp)


    # e = utils.percent_decrease(1.5 ,float(bid))
    # p = utils.percent_increase(1.5 ,float(15.41))
    # print(p)

    # print(bid)

    # if float(bid) > 15.44:
    #     print('yes')


    # coinz = (float(bal)) / float(bid) 


    #coinz_rand = coinz * float(15.25)


    #SELL_usdc_to_zar(572.42, bot_01)



    #p = buy_zar_to_usdc(coinz, bot_01)

    #p = get_valr_market()['USDCZAR']['bidPrice']

    # Valr_client.post_market_order(
    #                     pair='USDCZAR',
    #                     side='BUY',
    #                     base_amount= str(615),
    #                     subaccount_id= bot_01
    #                     )


    # SELL_ETH_to_ZAR(bal, Pocahontas_bot)

    #SELL_DAI_to_ETH(bal, Pocahontas_bot)


    # p = Valr_client.get_market_summary()
    # for i in p:
    #     print(i)