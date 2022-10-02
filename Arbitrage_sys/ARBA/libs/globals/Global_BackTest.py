
""" Collect data for BackTest """

day = ''
time = ''


data = {}
data_calc = {}
plot_data = {}


collect_ask = []
collect_bid = []
collect_highPrice = []
collect_lowPrice = []

x_collect_plot = []
EXTERNAL_x_collect = []

sold_history_cordinates = None
sold_history_amount = None
sold_data = {}

buy_history_cordinates = None
buy_history_amount = None
buy_data = {}


plot_counter = 1





time_delay_buy = 0
time_delay_sell = 0



## Sales.py
previous_price = 0