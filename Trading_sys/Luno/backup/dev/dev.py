import sys

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v4")

import bots.valr.algo.glob as GB

capital = 10000

cost_dollar_count = 5

count = 0




for i in range(20):

    MODE = GB.mode
    test = 0


    if MODE == 'buy_low':

        for i in range(cost_dollar_count):

            count += 1

            if count != cost_dollar_count:

                avrg_split = capital / cost_dollar_count

                test += avrg_split

                print(MODE, count ,capital - test)

            else:
                GB.mode = 'sell_high'
                count = 0



    elif MODE == 'sell_high':

        for i in range(cost_dollar_count):

            count += 1

            if count != cost_dollar_count:

                avrg_split = capital / cost_dollar_count

                test += avrg_split

                print(MODE, count ,capital + test)

            else:
                GB.mode = 'buy_low'
                count = 0

