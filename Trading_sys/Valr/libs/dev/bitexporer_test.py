from urllib import response
import requests
import pprint
from datetime import datetime



url = "https://api.bitaps.com/btc/v1/blockchain/blocks/last/1"
response = requests.get(url, params={"transactions" : True}).json()




# def get_transanction(url, hash):

#     end_point = '/mempool/transactions'
#     response = requests.get(url + end_point).json()

#     return(response)












# pprint.pprint(response)

# timestamp = response["data"][0]["adjustedTimestamp"]

# date = datetime.fromtimestamp(timestamp)

pprint.pprint(response)
# print(date)





# if __name__ == '__main__':

#     url = "https://api.bitaps.com/btc/v1/"



#     r_transaction = get_transanction(url, "72d1bbb84749f729d6e36d75549fd836c1e67a229178289b7d42a27be229ffa3")



#     for i in r_transaction["data"]["list"]:

#         timestamp = i["time"]
#         date = datetime.fromtimestamp(timestamp)

#         print(date)



    # pprint.pprint(r_transaction)