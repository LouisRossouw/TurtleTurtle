import os
import sys
import numpy
import datetime
import time

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v4")

from PIL import Image
import matplotlib.pyplot as plt

import libs.utils.toolUtils as toolUtils
import libs.utils.collect_historical_data as collect_data


config_path = os.path.join( os.path.dirname( __file__ ), '..' ) + '/config.yaml'
config = toolUtils.yaml_config(config_path)


TurtleTurtle_path = config["TurtleTurtle_path"]

TurtleTurtle_path + 'data/market/'

days = ["20_Wednesday"]
collected_WHALE_data = collect_data.collect_historical_data(config, market_name="whale", day_input=days)[0]
collected_VALR_data = collect_data.collect_historical_data(config, market_name="valr", day_input=days)[0]

WHALE_DATA = {}
VALR_DATA = {}



# WHALE DATA COLLECT


return_count = []
return_symbol = []
return_amount = []
return_guess_trend = []
return_details = []
return_total_count = []

time_stmp_02 = []

dump_trend = []
pump_trend = []

x_count = 0
for path in collected_WHALE_data:

    data = toolUtils.read_json(path)


    for time_stamp, value in data.items():

        time_stmp_02.append(time_stmp_02)

        key_list = value.keys()

        x_count += 1
        return_total_count.append(x_count)



        for i in key_list:
            time_stamp = value[i][0]
            symbol = value[i][1]["symbol"]
            amount = value[i][1]["amount"]
            guess_trend = value[i][2]

            from_type = value[i][1]["from"]["owner_type"]
            to_type = value[i][1]["to"]["owner_type"]

            if from_type == "exchange":
                from_type = "ex"
            elif from_type == "unknown":
                from_type = "un"

            if to_type == "exchange":
                to_type = "ex"
            elif to_type == "unknown":
                to_type = "un"

            quick_details = str(time_stamp).ljust(5) + ' || ' + str(x_count).ljust(10) + ' | ' + str(amount).split('.')[0].ljust(10) + ' | ' + str(symbol).ljust(4) + ' | ' + str(from_type) + ' -->> ' + str(to_type) + ' : ' + str(guess_trend).ljust(10)

            if guess_trend == 'pump':

                return_count.append(x_count)
                return_symbol.append(symbol)
                return_amount.append(amount)
                return_guess_trend.append(guess_trend)
                return_details.append(quick_details)
                pump_trend.append(guess_trend)


            elif guess_trend == 'dump':

                dump_trend.append(guess_trend)

            time.sleep(0.01)

            print('\rP ' + str(len(pump_trend)) + ' | D ' + str(len(dump_trend)), end="  ", flush=True)


return_BTC_bid = []
return_ETH_bid = []
return_XRP_bid = []
return_USDC_bid = []
return_MARKET_count = []

time_stmp = []

x_count_market = 0
for path in collected_VALR_data:
    


    data = toolUtils.read_json(path)

    for time_stamp, value in data.items():



        key_list = value.keys()
        x_count_market += 1



        BTC_bid = data[time_stamp]["BTCZAR"]["bidPrice"]
        ETH_bid = data[time_stamp]["ETHZAR"]["bidPrice"]
        XRP_bid = data[time_stamp]["XRPZAR"]["bidPrice"]
        USDC_bid = data[time_stamp]["USDCZAR"]["bidPrice"]

        return_BTC_bid.append(BTC_bid)
        return_ETH_bid.append(ETH_bid)
        return_XRP_bid.append(XRP_bid)
        return_USDC_bid.append(USDC_bid)

        return_MARKET_count.append(x_count_market)



        time_stmp.append(time_stamp)








save_path = TurtleTurtle_path + '/data/active_stats/general/whale_watch/test.png'

# plot bidprice
plt.title('WHALE_dev')
plt.xlabel('count')
plt.xticks(rotation=0)
plt.ylabel('value')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.2)
ee = plt.gcf()
ee.set_size_inches(65, 10)

# fig, ax = plt.subplots()
# ax.plot(return_MARKET_count, return_XRP_bid, color='magenta', linewidth=0.1)


# plt.plot(return_MARKET_count, return_XRP_bid)
# plt.scatter(return_count, return_count)


# # bid
# # plt.ylim(45000, 50000)
# plt.plot(x_count, x_count, color="blue", linewidth=1)



# lengg = len(return_count)
# for i in range(lengg):
#     plt.text(return_count[i], return_amount[i], return_symbol[i])


# plt.xticks(ticks=return_count, labels=return_details, rotation=70)




plt.scatter(return_count, return_amount)



# plt.autoscale()



plt.savefig(save_path, transparent=False)



