import sys
import random
import time

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v4")

import libs.utils.toolUtils as ToolUtils
import pprint


path = "D:/work/projects/dev/projects/TurtleTurtle_v4/data/market/whale_watch/2022/4_April/26_Tuesday_2022-04-26.json"
data = ToolUtils.read_json(path)


all = []
test = []



BTC_PUMP = []
BTC_DUMP = []

ETH_PUMP = []
ETH_DUMP = []

XRP_DUMP = []
XRP_PUMP = []

USDT_DUMP = []
USDT_PUMP = []


TOTAL_DUMP = []
TOTAL_PUMP = []



for i in data:

    date_time = data[i]

    if date_time == {}:

        all.append('None')
        test.append('None')


    else:

        for d in date_time:

            id = date_time[d]

            symbol = id[1]["symbol"]
            amount = id[1]["amount"]
            blockchain = id[1]["blockchain"]
            trend = id[2]




                # DUMP COLLECTORS
# Collect                             ###
    # DUMP
        # XRP
            if symbol == "BTC":
                if trend == 'dump':    
                    BTC_DUMP.append(amount)
            else:
                BTC_DUMP.append(0)


        # ETH
            if symbol == "ETH":
                if trend == 'dump':     
                    ETH_DUMP.append(amount)
            else:
                ETH_DUMP.append(0)


        # XRP
            if symbol == "XRP":
                if trend == 'dump':     
                    XRP_DUMP.append(amount)
            else:
                XRP_DUMP.append(0)

        # USDT
            if symbol == "USDT":
                if trend == 'dump':     
                    USDT_DUMP.append(amount)
            else:
                USDT_DUMP.append(0)






                # PUMP COLLECTORS
# Collect                               ### 
    # PUMP
            if symbol == "BTC":
                if trend == 'pump':     
                    BTC_PUMP.append(amount)
            else:
                BTC_PUMP.append(0)


        # ETH
            if symbol == "ETH":
                if trend == 'pump':     
                    ETH_PUMP.append(amount)
            else:
                ETH_PUMP.append(0)


        # XRP
            if symbol == "XRP":
                if trend == 'pump':     
                    XRP_PUMP.append(amount)
            else:
                XRP_PUMP.append(0)

        # XRP
            if symbol == "USDT":
                if trend == 'pump':     
                    USDT_PUMP.append(amount)
            else:
                USDT_PUMP.append(0)





            if trend == 'dump':
                TOTAL_DUMP.append(trend)
            else:
                TOTAL_DUMP.append('None')

            if trend == 'pump':
                TOTAL_PUMP.append(trend)
            else:
                TOTAL_PUMP.append('None')




            time.sleep(0.01)
            backtrack_num = 10



# SHORTEND:
# shorten the list to the above backtrack num length

    # DUMP:
            BTC_dump_shortened = BTC_DUMP[-backtrack_num:]
            ETH_dump_shortened = ETH_DUMP[-backtrack_num:]
            XRP_dump_shortened = XRP_DUMP[-backtrack_num:]
            USDT_dump_shortened = USDT_DUMP[-backtrack_num:]


    # PUMP:
            BTC_pump_shortened = BTC_PUMP[-backtrack_num:]
            ETH_pump_shortened = ETH_PUMP[-backtrack_num:]
            XRP_pump_shortened = XRP_PUMP[-backtrack_num:]
            USDT_pump_shortened = USDT_PUMP[-backtrack_num:]


            total_dump_shortened = TOTAL_DUMP[-backtrack_num:]
            total_pump_shortened = TOTAL_PUMP[-backtrack_num:]



# SUM:
# add up the total in the pump list

    # DUMP:
            BTC_DUMP_total_sum = sum(BTC_dump_shortened)
            ETH_DUMP_total_sum = sum(ETH_dump_shortened)
            XRP_DUMP_total_sum = sum(XRP_dump_shortened)
            USDT_DUMP_total_sum = sum(USDT_dump_shortened)



    # PUMP:    
            BTC_PUMP_total_sum = sum(BTC_pump_shortened)    
            ETH_PUMP_total_sum = sum(ETH_pump_shortened)   
            XRP_PUMP_total_sum = sum(XRP_pump_shortened)    
            USDT_PUMP_total_sum = sum(USDT_pump_shortened)   


# Count:

    # DUMP:
            count_total_dumps = total_dump_shortened.count('dump')
    # PUMP:
            count_total_pumps = total_pump_shortened.count('pump')           




            # DUMP
            if XRP_DUMP_total_sum > 15000000:
                above = '🅾️'
                ddump = '🅾️' + '🔷'

            elif XRP_DUMP_total_sum < 15000000:
                ddump = ''
                above = '.'

            # SUM
            if XRP_PUMP_total_sum > 15000000:
                ppump = '🔷'
                pump_above = '✅'
            elif XRP_PUMP_total_sum < 15000000:
                pump_above = '.'


            print(i, USDT_PUMP_total_sum, ETH_DUMP_total_sum)





            # print(str(i).split('.')[0],symbol.ljust(10),blockchain.ljust(10), above.ljust(20), pump_above.ljust(10))


            # if symbol == 'BTC':

            #     getdata_date = id[0]
            #     getdata_transaction = id[1]
            #     getdata_trend = id[2]

            #     #print(i, getdata_trend)
            #     all.append(getdata_trend)

            # else:
            #     pass


        # backtrack_num = 10
        # shortened = all[-backtrack_num:]


        # count_pump = ((shortened.count("pump")) / backtrack_num) * 100
        # count_dump = ((shortened.count("dump")) / backtrack_num) * 100
        # count_no_activity = ((shortened.count("no_activity")) / backtrack_num) * 100


        # difference = count_pump - count_dump

        # if float(difference) > float(20):
        #     print('above 10:')
        # if float(difference) < float(-0):
        #     print('bello -10:')



        # print(shortened)

        # p = (shortened.count("pump"))
        # d = (shortened.count("dump"))

        # print('\r' + i + ' | diff ' + str(round(difference,1)).ljust(5) + ' UP: ' + str(round(p,1)).ljust(5) + '%'.ljust(5), 'Down: ' + str(round(d,1)) + '%'.ljust(5), end="              ", flush=True)

        #print('\r' + i + ' | diff ' + str(round(difference,1)).ljust(5) + ' UP: ' + str(round(count_pump,1)).ljust(5) + '%'.ljust(5), 'Down: ' + str(round(count_dump,1)) + '%'.ljust(5), end="              ", flush=True)


# whale_counter(path)


# path_test = "D:/work/projects/dev/projects/TurtleTurtle_v4/data/market/valr_market/2022/4_April/21_Thursday_2022-04-21.json"


# market = ToolUtils.read_json(path)




















# data_pump = ['p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p',
# 'd', 'd', 'd', 'd', 'd','d', 'd', 'd', 'd', 'd','d', 'd', 'd', 'd', 'd','d', 'd', 'd', 'd', 'd','d', 'd', 'd', 'd', 'd','d', 'd', 'd', 'd', 'd',
# 'n', 'n', 'n', 'n', 'n','n','n', 'n', 'n', 'n', 'n','n','n', 'n', 'n', 'n', 'n','n','n', 'n', 'n', 'n', 'n','n','n', 'n', 'n', 'n', 'n','n']

# dump = []
# pump = []
# no_activity = []


# test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# random.shuffle(data_pump)

# dd = len(data_pump)

# ppump = []


# for i in range(1, 30):

#     input = data_pump[i]

#     if input == 'p':
#         ppump.append(input)






#     print(ppump[-3:])






#     # if i == 'p':
#     #     pump.append(i)

#     # elif i == 'd':
#     #     dump.append(i)

#     # elif i == 'n':
#     #     no_activity.append(i)



#     # count_pump = len(pump)
#     # count_dump = len(dump)
#     # count_no_act = len(no_activity)







#     time.sleep(0.1)
#     # print('\rpump: ' + str(count_pump), 'dump: ' + str(count_dump), 'no_act: ' + str(count_no_act), end="   ", flush=True)