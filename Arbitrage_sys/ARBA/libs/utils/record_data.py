import os
import sys
import json
import datetime
import calendar





def coinbase_track_data(COINB, count, config):

    TurtleTurtle_path = config["TurtleTurtle_path"]


    Turtle_Dir = TurtleTurtle_path
    data_dir = str(Turtle_Dir) + '/data/market'
    track_market_dir = str(data_dir) + '/coinbase_market'

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
    market = COINB

    new_data = {date_time : market}

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







def luno_track_data(LUNO, count, config):

    TurtleTurtle_path = config["TurtleTurtle_path"]


    Turtle_Dir = TurtleTurtle_path
    data_dir = str(Turtle_Dir) + '/data/market'
    track_market_dir = str(data_dir) + '/luno_market'

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
    market = LUNO

    new_data = {date_time : market}

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







def valr_track_data(VLR, count, config):

    TurtleTurtle_path = config["TurtleTurtle_path"]
    clean_data = {}

    clean_data[VLR['BTCZAR']['currencyPair']] = VLR['BTCZAR']
    clean_data[VLR['ETHZAR']['currencyPair']] = VLR['ETHZAR']
    clean_data[VLR['XRPZAR']['currencyPair']] = VLR['XRPZAR']
    clean_data[VLR['USDCZAR']['currencyPair']] = VLR['USDCZAR']
    clean_data[VLR['SOLZAR']['currencyPair']] = VLR['SOLZAR']  


    Turtle_Dir = TurtleTurtle_path
    data_dir = str(Turtle_Dir) + '/data/market'
    track_market_dir = str(data_dir) + '/valr_market'

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
    market = clean_data

    new_data = {date_time : market}

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



def buy_sell_status(data, config):

    TurtleTurtle_path = config["TurtleTurtle_path"]

    Turtle_Dir = TurtleTurtle_path
    data_dir = str(Turtle_Dir) + '/data'
    track_market_dir = str(data_dir) + '/Sales/Trading_sys/Valr'

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

    current_working_path = str(dir_year) + '/' + str(day_month_name)

    # Create dirs
    if os.path.exists(dir_year) != True:
        os.mkdir(dir_year)
    if os.path.exists(current_working_path) != True:
        os.mkdir(current_working_path)


    json_data = str(current_working_path) + '/' + str(dir_date_name) + '.json'

    # get market data function
    market = data

    new_data = {date_time : market}

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

    # print(str(date_now) + ' : ' + str(date_time) + ' || sale saved')





