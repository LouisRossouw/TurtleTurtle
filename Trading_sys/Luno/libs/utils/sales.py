import os
from datetime import datetime
import numpy

import Luno.libs.utils.collect_historical_data as Collect
import Luno.libs.utils.toolUtils as ToolUtils
import Luno.libs.globals.Global_BackTest as GLOBAL

from calendar import monthrange



def get_profits(all=True, input_bot=None, input="year"):
    """ This runs through the recorded sales made and calculates profits """

    config_path =  (os.getenv("Turtle") + "/Trading_sys/Luno") + '/config.yaml'
    configs = ToolUtils.yaml_config(config_path)


    if all == True:

        if input == 'year':
            year = ["2022"]
            data_sales = Collect.collect_historical_sales(configs, year_input=year)[2]
        elif input == 'day':
            day = ["22_Friday"]
            data_sales = Collect.collect_historical_sales(configs, day_input=day)[0]
        elif input == 'month':
            month = ["April"]
            data_sales = Collect.collect_historical_sales(configs, month_input=month)[1]

        data_sales.sort()
        profit_all = 'All Profits👻'

        for bot in configs["VALR_active_bots"]:

            currency_pair = configs["VALR_active_bots"][bot]["currency_pair"]

            if currency_pair == "ETHZAR":
                pair = "🔮"
            elif currency_pair == "XRPZAR":
                pair = "🔹"
            elif currency_pair == "BTCZAR":
                pair = "⚱️"


            if bot != "Market_eval":

                # calculations
                all_profit = []
                all_win_loss = []
                all_dates = []
                all_wins = []
                all_loss = []

                zar_balance_list = []
                total_profit = []
                between_sale_dates = []

                brea_line = ('\n\n' + pair + ' --------- ' + bot + '\n')
                titles = '\n'+(str('             DATE            ').ljust(14) + ' | ' + str("CP  ").ljust(3) + ' | ' + str("    TOTAL").ljust(12) + ' | ' + str(" PROFIT").ljust(6))

                profit_all += brea_line + titles

                for path in data_sales:

                    day_data = ToolUtils.read_json(path)

                    for time in day_data:

                        bot_name = day_data[time]["Bot_Name"]

                        if bot == bot_name:
                        
                            trade_type = day_data[time]["trade_type"]
                            askPrice = day_data[time]["askPrice"]
                            bidPrice = day_data[time]["bidPrice"]
                            zar_balance = day_data[time]["my_zar_balance_in_rands"]
                            currencypair = day_data[time]["currencypair"]
                            Date = day_data[time]["Date"]

                            new_date = datetime.fromisoformat(Date)
                            date_short = new_date.strftime("%x")
                            time_short = new_date.strftime("%X")[:-3]

                            clean_date = date_short + ' ' + time_short

                            date_count = str(new_date.strftime("%d/%m/%Y"))
                            all_dates.append(date_count)


                            if trade_type == "sell_high|EXIT":

                                zar_balance_list.append(zar_balance)
                                balances = zar_balance_list[-2:]
                                between_sale_dates.append(date_count)
                                between_sales = between_sale_dates[-2:]

                                try:
                                    # calculate profit
                                    profit = float(balances[1]) - float(balances[0])
                                except IndexError:
                                    sale_delata = 0
                                    profit = 0


                                if float(profit) > float(500):
                                    star = '⭐️'
                                else:
                                    star = ''

                                all_profit.append(profit)


                                try:
                                    percent = float(balances[0]) / float(balances[1]) * 100
                                    ROI = (float(profit) / float(balances[0])) * 100
                                except IndexError:
                                    ROI = 0
                                    percent = 0

                                total_profit.append(profit)
                                calculated_all_profit = round(sum(total_profit),2)


                                if float(profit) < float(-0):
                                    win_loss = "🛑"
                                    all_loss.append(profit)
                                elif float(profit) > float(0):
                                    win_loss = "✅"
                                    all_wins.append(profit)
                                else:
                                    win_loss = '💤'
                                    pass

                                return_sale_details = '\n'+ win_loss + '|'+ str(clean_date).split('.')[0].ljust(10) + ' | ' + str(currencypair)[:-3].ljust(2) + ' | R' + str(calculated_all_profit).ljust(12) + ' | R' + str(round(profit,2)).ljust(7) + ' | ' + str(round(ROI,1)) + '%' + star
                                profit_all += return_sale_details




                            first_date = all_dates[:1]
                            last_date = all_dates[-1:]

                            date_format = "%d/%m/%Y"
                            a = datetime.strptime(first_date[0], date_format)
                            b = datetime.strptime(last_date[0], date_format)
                            delta = b - a



                avarage = numpy.average(all_profit)
                monthly_day_prediction = float(avarage) * 30

                losses_count = len(all_loss)
                winnings_count = len(all_wins)


                # calculate expected end month profit
                get_dates = ToolUtils.get_dates()
                today_num = get_dates[2]
                month_name = get_dates[6]
                num_days = monthrange(get_dates[4], get_dates[5])[1] 
                days_left = num_days - today_num
                month_end_profit_preditction = avarage * days_left
                
                predicted = month_end_profit_preditction + sum(total_profit)



                try:
                    winning_score = winnings_count / (losses_count + winnings_count) * 100
                except ZeroDivisionError:
                    winning_score = 0

                try:
                    loosing_score = losses_count / (losses_count + winnings_count) * 100
                except ZeroDivisionError:
                    loosing_score = 0


                try:
                    last_2_sales = all_dates[-2:]

                    print(last_2_sales[0], last_2_sales[1])

                    date_format = "%d/%m/%Y"
                    sale_a = datetime.strptime(last_2_sales[0], date_format)
                    sale_b = datetime.strptime(last_2_sales[1], date_format)
                    sale_delata = sale_a - sale_b
                except IndexError:
                    pass



                # filter for avrg symbol
                if (avarage <= 20):
                    avg_symb = '💩'
                if (avarage >= 0) and (avarage <= 49):
                    avg_symb = '💤'
                elif (avarage >= 50) and (avarage <= 100):
                    avg_symb = '🍩'
                elif (avarage >= 101) and (avarage <= 150):
                    avg_symb = '🔅'
                elif (avarage >= 150) and (avarage <= 200):
                    avg_symb = '⭐️'
                elif (avarage >= 201) and (avarage <= 300):
                    avg_symb = '⭐️⭐️'
                elif (avarage >= 301) and (avarage <= 450):
                    avg_symb = '🌟'
                elif (avarage >= 451) and (avarage <= 600):
                    avg_symb = '💎'
                elif (avarage >= 601) and (avarage <= 1000):
                    avg_symb = '💎💎'
                elif (avarage >= 1001):
                    avg_symb = '💎💎💎'
                else:
                    avg_symb = ''


                try:
                    profit_all += '\n\n📜 : Ac: ' + str(delta).split(',')[0]
                    profit_all += '\n📜 : DL: ' + str(days_left) + ' days left of ' + str(month_name)
                    profit_all += '\n\n📜 : AVG: R' + str(round(avarage,2)) + ' ' + avg_symb
                    profit_all += '\n📜 : PRF: R' + str(round(sum(total_profit),2))
                    profit_all += '\n\n📜 : POT: R' + str(round(month_end_profit_preditction,2))
                    profit_all += '\n📜 : END: R' + str(round(predicted,2))
     
                    profit_all += '\n\n📜 : W/L: ' + str(winnings_count) + '/' + str(losses_count)
                    profit_all += '\n📜 : ' + 'Win_prob: ' + str(round(winning_score,1)) + '%\n📜 : loss_prob: '+ str(round(loosing_score,1)) + '%'

                except UnboundLocalError:
                    pass


    return(profit_all)



if __name__ == '__main__':

    profits = get_profits(all=True, input_bot=None, input="month")
    print(profits)



