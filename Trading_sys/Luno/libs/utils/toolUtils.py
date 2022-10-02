import os
import json
import yaml
import numpy
import datetime
import calendar




#            # Configs

def yaml_config(config_path):
    """ Open yaml configs """
    config = yaml.safe_load(open(config_path))
    return(config)



#            # Coin conversions

def rands_to_coins(total_rand_count, coin_market_value):
    """ This takes a rand and converts its value to coins """
    # input rands, input the total coins i have that i want to convert to rands
    rand_value = float(total_rand_count) / float(coin_market_value)
    return(rand_value)

def coin_to_rands(coin_count, coin_market_value):
    """ This takes a coin and converts its value to rands """
    rand_value = float(coin_count) * float(coin_market_value)
    return(rand_value)

def usdc_to_rands(coin_count, coin_market_value):
    """ This takes a coin and converts its value to rands """
    rand_value = coin_count * coin_market_value
    return(rand_value)


#             # Percentages

def get_percentage_difference(new_value, original_value):
    """ finds the percentage difference between new number and original """
    output_value = ((float(new_value) - float(original_value)) / float(original_value)) * 100
    return(output_value)

def percent_increase(percent, input_value):
    """ adds a percent to a value and returns it"""
    output_value = float(((input_value / 100) * float(percent)) + float(input_value))
    return(float(output_value))

def percent_decrease(percent, input_value):

    value = float(((input_value / 100) * float(percent)) + float(input_value))
    mathss = float(value) - float(input_value)
    output_value = float(input_value) - float(mathss)
    return(output_value)




#           # Numpy analyze data

def find_mean_in_data(coin, data):
    """ This finds the avarage number in a list """
    collected_values = []
    for i in (data):
        month = data[i][0]
        day_name = data[i][1]
        # Market values
        try:
            btc_datas = data[i][2][month][day_name][coin]
            collected_values.append(float(btc_datas))
        except KeyError:
            pass
    output_value = numpy.mean(collected_values)
    return(output_value)


def find_meadian_in_data(coin, data):
    """ This finds the middle number in a sorted list """
    collected_values = []
    for i in (data):
        month = data[i][0]
        day_name = data[i][1]
        # Market values
        try:
            btc_datas = data[i][2][month][day_name][coin]
            collected_values.append(float(btc_datas))
        except KeyError:
            pass
    output_value = numpy.median(collected_values)
    return(output_value)


def find_mode_in_data(coin, data):
    """ This finds the number that appears the most """
    collected_values = []
    for i in (data):
        month = data[i][0]
        day_name = data[i][1]
        # Market values
        try:
            btc_datas = data[i][2][month][day_name][coin]
            collected_values.append(float(btc_datas))
        except KeyError:
            pass
    # output_value = stats.mode(collected_values)
    output_value = 'not working'
    return(output_value)


def find_deviation_in_data(coin, data):
    """ This gets deviation spread from the mean (average num )"""
    collected_values = []
    for i in (data):
        month = data[i][0]
        day_name = data[i][1]
        # Market values
        try:
            btc_datas = data[i][2][month][day_name][coin]
            collected_values.append(float(btc_datas))
        except KeyError:
            pass
    output_value = numpy.std(collected_values)
    return(output_value)

def find_percentile_in_data(coin, data, percent):
    """ This returns the percentil, give a list, and a percent """
    collected_values = []
    for i in (data):
        month = data[i][0]
        day_name = data[i][1]
        # Market values
        try:
            btc_datas = data[i][2][month][day_name][coin]
            collected_values.append(float(btc_datas))
        except KeyError:
            pass
    output_value = numpy.percentile(collected_values, percent)
    return(output_value)



#        # Json read/write ata

def write_to_json(json_path, data):
    """ Create and write to json file """
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=6)

def read_json(json_path):
    """ Reads json file """
    with open(json_path) as f:
        json_file = json.loads(f.read())

    return(json_file)


def get_dates():
    # Date functions
    date_now_full = (str(datetime.datetime.now()))
    date_now = (str(datetime.datetime.now()).split(' ')[0])
    date_time = (str(datetime.datetime.now()).split(' ')[1])
    day_num = datetime.datetime.today().day
    day_name = calendar.day_name[datetime.date.today().weekday()]
    date_year = datetime.datetime.today().year
    day_month_num = datetime.datetime.today().month
    day_month_name = calendar.month_name[day_month_num]

    dict = {}
    dict['date_NOW'] = [date_now, date_time, day_num, day_name, date_year, day_month_num, day_month_name, date_now_full]
    
    return(date_now, date_time, day_num, day_name, date_year, day_month_num, day_month_name, dict, date_now_full)



def get_bots(path):
    """ collects the bots from dir """

    exchange_names_dir = os.listdir(path)
    data = {}
    for exchange in exchange_names_dir:
        all_bot_name = os.listdir(path + '/' + exchange)
        for bot in all_bot_name:
            bot_name = bot.split('.')[0]
            data[bot_name] = exchange

    return(data, exchange_names_dir)


if __name__ == '__main__':

    paths = "D:\\work\\projects\dev\projects\\TurtleTurtle_v2\\bots"
    print(get_bots(paths))