import os

import Luno.libs.utils.toolUtils as utils


def collect_historical_data(
                        config, 
                        market_name,
                        year_input=None,
                        month_input=None,
                        day_input=None,
                    ):
    """ Collects all the historical data that has been recorded """

    if market_name == 'luno':
        path_to_data = config["TurtleTurtle_path"] + '/data/market/luno_market'
    elif market_name == 'valr':
        path_to_data = config["TurtleTurtle_path"] + '/data/market/valr_market'
    elif market_name == 'whale':
        path_to_data = config["TurtleTurtle_path"] + '/data/market/whale_watch'
    elif market_name == 'coinbase':
        path_to_data = config["TurtleTurtle_path"] + '/data/market/coinbase_market'





# Cleans up the inputs
    day_list = []
    if day_input != None:
        for i in day_input:
            input_split = i.split('_')
            day_name_clean = input_split[0] + '_' + input_split[1].lower()
            day_list.append(day_name_clean)


    month_list = []
    if month_input != None:
        for i in month_input:
            day_cleaner = i.lower()
            month_list.append(day_cleaner)


    year_list = []
    if year_input != None:
        for i in year_input:
            year_cleaner = i.lower()
            year_list.append(year_cleaner)


    return_year_list = []
    return_month_list = []
    return_day_list = []
    
    for path, directories, files in os.walk(path_to_data):

# search for a specifc days - requires a list
        for file in files:

            file_split = file.split('_')

            day_num = file_split[0].lower()
            day_name = file_split[1].lower()

            if (day_num + '_' + day_name) in day_list:
                return_day_list.append(os.path.join(path, file).replace('\\', '/'))

# Search for specific months - requires a list
        if month_input != None:
            for month in directories:
                if month.lower() in month_list:
                    month_path = os.path.join(path, month)

                    for d in os.listdir(month_path):
                        return_month_list.append(os.path.join(month_path, d).replace('\\', '/'))


# Search for specific Year - requires a list
        if year_input != None:
            for year in directories:
                if year.lower() in year_list:
                    year_path = os.path.join(path, year)

                    for d in os.listdir(year_path):
                        months_paths = os.path.join(year_path, d).replace('\\', '/')

                        for m in os.listdir(months_paths):
                            return_year_list.append(os.path.join(months_paths, m).replace('\\', '/'))



    return return_day_list, return_month_list, return_year_list




def append_historical_data(data_list, currencyPair):

    return_data = {}

    askPrice = []
    bidPrice = []
    highPrice = []
    lowPrice = []

    for day in data_list:

        split_name = os.path.basename(day).split('_')
        month_name = os.path.basename(os.path.dirname(day))
        month_name_clean = month_name.split('_')[1]
        day_name = split_name[0] + '_' + split_name[1] + '_' + month_name_clean
    
        json_data = utils.read_json(day)


        return_data[day_name] = json_data


    for i in return_data:
        for e in return_data[i]:
            for s in return_data[i][e][currencyPair]:
                ask = return_data[i][e][currencyPair]['askPrice']
                bid = return_data[i][e][currencyPair]['bidPrice']
                # high = return_data[i][e]['ETHZAR']['highPrice']
                # low = return_data[i][e]['ETHZAR']['lowPrice']

                askPrice.append(float(ask))
                bidPrice.append(float(bid))
                # highPrice.append(high)
                # lowPrice.append(low)


    return(askPrice, bidPrice)







def collect_historical_sales(
                        config, 
                        year_input=None,
                        month_input=None,
                        day_input=None,
                    ):
    """ Collects all the historical data that has been recorded """


    path_to_data = config["TurtleTurtle_path"] + '/data/sales'


# Cleans up the inputs
    day_list = []
    if day_input != None:
        for i in day_input:
            input_split = i.split('_')
            day_name_clean = input_split[0] + '_' + input_split[1].lower()
            day_list.append(day_name_clean)


    month_list = []
    if month_input != None:
        for i in month_input:
            day_cleaner = i.lower()
            month_list.append(day_cleaner)


    year_list = []
    if year_input != None:
        for i in year_input:
            year_cleaner = i.lower()
            year_list.append(year_cleaner)


    return_year_list = []
    return_month_list = []
    return_day_list = []
    
    for path, directories, files in os.walk(path_to_data):

# search for a specifc days - requires a list
        for file in files:

            file_split = file.split('_')

            day_num = file_split[0].lower()
            day_name = file_split[1].lower()

            if (day_num + '_' + day_name) in day_list:
                return_day_list.append(os.path.join(path, file).replace('\\', '/'))

# Search for specific months - requires a list
        if month_input != None:
            for month in directories:
                if month.lower() in month_list:
                    month_path = os.path.join(path, month)

                    for d in os.listdir(month_path):
                        return_month_list.append(os.path.join(month_path, d).replace('\\', '/'))


# Search for specific Year - requires a list
        if year_input != None:
            for year in directories:
                if year.lower() in year_list:
                    year_path = os.path.join(path, year)

                    for d in os.listdir(year_path):
                        months_paths = os.path.join(year_path, d).replace('\\', '/')

                        for m in os.listdir(months_paths):
                            return_year_list.append(os.path.join(months_paths, m).replace('\\', '/'))



    return return_day_list, return_month_list, return_year_list


















if __name__ == '__main__':

    f = ['09_Saturday', '10_Sunday']
    months = ['March']
    market_name = 'valr'
    config = utils.yaml_config("D:/work/projects/dev/projects/TurtleTurtle_v4/config.yaml")


    test = collect_historical_data(
                        config, 
                        market_name,
                        year_input=None,
                        month_input=None,
                        day_input=f,
                    )

    for i in test[0]:
        print(i)

    # p = append_historical_data(test[2], currencyPair='XRPZAR')




    # print(p)



