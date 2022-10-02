import os
import sys
import json
import time
import calendar
import datetime
from pprint import pprint
from whalealert.whalealert import WhaleAlert

import utils.ToolUtils as toolUtils
import Managers_sys.TeleGram_Manager.Bot_Notifier as Bot_Notifier




WHALE_API = os.getenv("WHALE_ALERT_API_KEY")
whale = WhaleAlert()




def address_check(TurtleTurtle_path, whale_address):
    """ Runs a quick address check on rich list """

    rich_list_dir = TurtleTurtle_path + '/Whale_sys/Whale_Alert/Rich_List'

    address_list = []

    for rich_list in os.listdir(rich_list_dir):
        
        rich_file = rich_list.split('.')[0]
        path = rich_list_dir + '/' + rich_list

        with open(path) as f:
            for rich_addr in f:

                rich_address = rich_addr.split('\n')[0]

                address_list.append(rich_address)

    if whale_address in address_list:
        check = True
    else:
        check = False

    return(check)




def whale_record_data(count, config, whale_data):

    TurtleTurtle_path = config["TurtleTurtle_path"]

    Turtle_Dir = TurtleTurtle_path
    data_dir = str(Turtle_Dir) + '/data'
    track_market_dir = str(data_dir) + '/Whale_Watch'

    if os.path.exists(data_dir) != True:
        os.mkdir(data_dir)

    if os.path.exists(track_market_dir) != True:
        os.mkdir(track_market_dir)

    # Date functions
    date_now = (str(datetime.datetime.now()).split(' ')[0])
    date_time = (str(datetime.datetime.now()).split(' ')[1])
    date_year = datetime.datetime.today().year
    day_name = calendar.day_name[datetime.date.today().weekday()]
    day_day = datetime.datetime.today().day
    day_month_num = datetime.datetime.today().month
    day_month_name = calendar.month_name[day_month_num]

    # Date directories
    dir_date_name = str(day_day).zfill(2) + '_' + str(day_name) + '_' + str(date_now)
    dir_year = str(track_market_dir) + '/' + str(date_year)

    current_working_path = str(dir_year) + '/' + str(day_month_num) + '_' + str(day_month_name)

    # Create dirs
    if os.path.exists(dir_year) != True:
        os.mkdir(dir_year)
    if os.path.exists(current_working_path) != True:
        os.mkdir(current_working_path)


    json_data = str(current_working_path) + '/' + str(dir_date_name) + '.json'

    # get market data function
    
    new_data = {date_time : whale_data}

    if os.path.exists(json_data) != True:
        with open(json_data, 'w') as f:
            json.dump(new_data, f, indent=4)

    if os.path.exists(json_data) == True:
        with open(json_data) as f:
            json_file = json.loads(f.read())

    json_file.update(new_data)

    with open(json_data, 'w') as f:
        json.dump(json_file, f, indent=4)


    dt = (date_time).split('.')[0]

    # print(str(date_now) + ' : ' + str(date_time) + ' || market tracked')




def get_whale(config):
    """ Runs and checks for large transactions using the whale_alert.io API """

    TurtleTurtle_path = config["TurtleTurtle_path"]
    whale_dir_track = TurtleTurtle_path + '/Whale_sys/Whale_Alert/data/live_transaction_data.json'


    if os.path.exists(whale_dir_track) != True:
        track_data_empty = {}
        toolUtils.write_to_json(whale_dir_track, track_data_empty)

    # Specify a single transaction from the last 10 minutes
    start_time = int(time.time() - 500)
    # transaction_count_limit = amount

    success, transactions, status = whale.get_transactions(start_time, api_key=WHALE_API)

    data = []

    BTC_coin_count = float(0)
    ETH_coin_count = float(0)
    XRP_coin_count = float(0)

    historic_data = toolUtils.read_json(whale_dir_track)

    data_now = {}  

    # for i in range(transaction_count_limit):
    for i in transactions:

        n = i

        single_transaction = i

        # Get
        amount_in_coins = i["amount"]
        amount_in_usdc = i["amount_usd"]
        blockchain = i["blockchain"]

        FROM_owner = i["from"]["owner"]
        FROM_type = i["from"]["owner_type"]
        FROM_address = i["from"]["address"]

        TO_owner = i["to"]["owner"]
        TO_type = i["to"]["owner_type"]
        TO_address = i["to"]["address"]

        hash = i["hash"]
        id = i["id"]
        symbol = i["symbol"]

        Timestamp = i["timestamp"]
        transaction_count = i["transaction_count"]
        transaction_type = i["transaction_count"]

        date_time = str(datetime.datetime.fromtimestamp(Timestamp))

        check = address_check(TurtleTurtle_path, FROM_address)

        text_start = '___________________________\n'
        text_01 =  '\nAmount_coin: ' + str(amount_in_coins) + ' ' + symbol + '\nAmount_usdc: ' + str(amount_in_usdc) + ' USDC'
        text_02 = '\n\nBlockChain: ' + str(blockchain)
        text_03 = '\n\nFrom: ' + '\n\nType: ' + FROM_type + '\nOwner: ' + FROM_owner
        text_04 = '\n\nTo:' + '\n\nType: ' + TO_type + '\nOwner: ' + TO_owner
        text_05 = '\n\nSymbol: ' + symbol
        text_06 = '\nIs_rich_list: ' + str(check)
        text_07 = '\n\nDate: ' + str(date_time)
        text_end = '\n___________________________'

        message = text_start + text_01 + text_02 + text_03 + text_04 + text_05 + text_06 + text_07 + text_end


        if FROM_type == "exchange":
            FROM_type = "ex"
        elif FROM_type == "unknown":
            FROM_type = "un"

        if TO_type == "exchange":
            TO_type = "ex"
        elif TO_type == "unknown":
            TO_type = "un"


        if id not in historic_data:


        # BTC
            # possible for hold - possible POSITIVE PRICE ACTION
            if symbol == 'BTC':
                if FROM_type == 'ex':
                    if TO_type == 'un':
                            BTC_coin_count += float(amount_in_coins)  
                            #print(message + '\nwhales might buy - possible large pump or sell? | ' + str(BTC_coin_count) + text_end )
                            historic_data[id] = {}
                            trend = 'possible hold'
                            data_now[id] = [date_time, single_transaction, trend]
                            notification_data = [date_time, single_transaction, trend, message] 
                            quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |⚱️' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💰 ' + str(trend) + ' 💰 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            #Bot_Notifier.Whale_alert(config, notification_data, quick_details)


            # possible for sale - possible CRASH
            if symbol == 'BTC':
                if FROM_type == 'un':
                    if TO_type == 'ex':
                        BTC_coin_count += float(amount_in_coins)   
                        #print(message + '\npossible CRASH | ' + str(BTC_coin_count) + text_end )
                        historic_data[id] = {}
                        trend = 'dump'
                        data_now[id] = [date_time, single_transaction, trend]
                        notification_data = [date_time, single_transaction, trend, message]
                        if float(amount_in_coins) > float(1000):
                            quick_details = '🅾️🅾️'+str(amount_in_coins).split('.')[0].ljust(10) + ' |⚱️' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💩 ' + str(trend) + ' 💩 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)
                        else:
                            quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |⚱️' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💩 ' + str(trend) + ' 💩 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)


        # ETH
            # possible for hold - possible POSITIVE PRICE ACTION
            if symbol == 'ETH':
                if FROM_type == 'ex':
                    if TO_type == 'un':
                            ETH_coin_count += float(amount_in_coins)         
                            #print(message + '\nwhales might buy - possible large pump or sell? | ' + str(ETH_coin_count) + text_end)
                            historic_data[id] = {}
                            trend = 'possible hold'
                            data_now[id] = [date_time, single_transaction, trend]
                            notification_data = [date_time, single_transaction, trend, message]
                            quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |🔮' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💰 ' + str(trend) + ' 💰 ' + str(blockchain)
                            print(text_start + quick_details + text_end) 
                            #Bot_Notifier.Whale_alert(config, notification_data, quick_details)


            # possible for sale - possible CRASH
            if symbol == 'ETH':
                if FROM_type == 'un':
                    if TO_type == 'ex':
                        ETH_coin_count += float(amount_in_coins)   
                        #print(message + '\npossible CRASH | ' + str(ETH_coin_count) + text_end)
                        historic_data[id] = {}
                        trend = 'dump'
                        data_now[id] = [date_time, single_transaction, trend]
                        notification_data = [date_time, single_transaction, trend, message] 
                        if float(amount_in_coins) > float(2000):
                            quick_details = '🆘🆘' + str(amount_in_coins).split('.')[0].ljust(10) + ' |🔮' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💩 ' + str(trend) + ' 💩 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)
                        else:
                            quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |🔮' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💩 ' + str(trend) + ' 💩 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)


        # XRP
            # possible for hold - possible POSITIVE PRICE ACTION
            if symbol == 'XRP':
                if FROM_type == 'ex':
                    if TO_type == 'un':
                            XRP_coin_count += float(amount_in_coins)    
                            #print(message + '\nwhales might buy - possible large pump or sell? | ' + str(XRP_coin_count) + text_end)
                            historic_data[id] = {}
                            trend = 'possible hold'
                            data_now[id] = [date_time, single_transaction, trend]
                            notification_data = [date_time, single_transaction, trend, message]
                            quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |🔹' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💰 ' + str(trend) + ' 💰 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            #Bot_Notifier.Whale_alert(config, notification_data, quick_details)


            # possible for sale - possible CRASH
            if symbol == 'XRP':
                if FROM_type == 'un':
                    if TO_type == 'ex':
                        XRP_coin_count += float(amount_in_coins) 
                        #print(message + '\npossible CRASH | ' + str(XRP_coin_count) + text_end)
                        historic_data[id] = {}
                        trend = 'dump'
                        data_now[id] = [date_time, single_transaction, trend] 
                        notification_data = [date_time, single_transaction, trend, message] 
                        if float(amount_in_coins) > float(10000000):
                            quick_details = '⛔️⛔️'+str(amount_in_coins).split('.')[0].ljust(10) + ' |🔹' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💩 ' + str(trend) + ' 💩 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)
                        else:
                            quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |🔹' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💩 ' + str(trend) + ' 💩 ' + str(blockchain)
                            print(text_start + quick_details + text_end)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)


            # # USDT to exchange, whales might buy - possible large pump
            if symbol == 'USDT':
                if FROM_type == 'un':
                    if TO_type == 'ex':
                        #print(message + '\nwhales might buy - possible large pump' + text_end)
                        historic_data[id] = {}
                        trend = 'pump'
                        data_now[id] = [date_time, single_transaction, trend]
                        notification_data = [date_time, single_transaction, trend, message] 
                        if float(amount_in_coins) > float(10000000):
                            quick_details = '❇️❇️'+str(amount_in_coins).split('.')[0].ljust(10) + ' |🔘' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 🚀 ' + str(trend) + ' 🚀 ' + str(blockchain)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)
                        else:
                            quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |🔘' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 🚀 ' + str(trend) + ' 🚀 ' + str(blockchain)
                            Bot_Notifier.Whale_alert(config, notification_data, quick_details)


            # # USDT to exchange, whales not buying - down trend
            if symbol == 'USDT':
                if FROM_type == 'ex':
                    if TO_type == 'un':
                        #print(message + '\nwhales not buying - down trend' + text_end)
                        historic_data[id] = {}
                        trend = 'no_activity'
                        data_now[id] = [date_time, single_transaction, trend]
                        notification_data = [date_time, single_transaction, trend, message] 
                        quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |🔘' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 🤖 ' + str(trend) + ' 🤖 ' + str(blockchain)
                        print(text_start + quick_details + text_end)
                        #Bot_Notifier.Whale_alert(config, notification_data, quick_details)


            if check == True:
                #print(message + '\nBIG BOY is moving Money' + text_end)
                historic_data[id] = {}
                trend = 'BIGBOY'
                data_now[id] = [date_time, single_transaction, trend]
                notification_data = [date_time, single_transaction, trend, message] 
                quick_details = str(amount_in_coins).split('.')[0].ljust(10) + ' |🔰' + str(symbol).ljust(4) + ' | ' + str(FROM_type) + ' -->> ' + str(TO_type) + ' : 💎 ' + str(trend) + ' 💎 ' + str(blockchain)
                print(text_start + quick_details + text_end)
                #Bot_Notifier.Whale_alert(config, notification_data, quick_details)


        # else:
        #     print(id, symbol, amount_in_coins)

    toolUtils.write_to_json(whale_dir_track, historic_data)

    return(data_now)




if __name__ == '__main__':

    config_path = os.path.dirname((os.path.dirname((__file__)))) + '/config.yaml'
    config = toolUtils.yaml_config(config_path)

    amount = 5
    count = 1

    cc = 0

    while True:
        cc += 1
        print('\rCount: ' + str(cc), end="      ", flush=True)
        time.sleep(10)
        whale_data = get_whale(config)
        whale_record_data(count, config, whale_data)




