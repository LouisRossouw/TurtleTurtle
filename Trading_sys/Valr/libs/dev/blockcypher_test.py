import blockcypher as BLKCP
import pprint
import datetime


# satoshi_conversion = BLKCP.from_base_unit(4108168341, 'btc')

transaction_details_test = BLKCP.get_transaction_details(tx_hash='a9e01cf0b6ddbc6328d438676e863ff1279ac79a615fddc5928a107b12104c86', coin_symbol="btc")

# dd = datetime.datetime(2022, 4, 24, 14, 11, 30, 228000)

HASH = BLKCP.get_broadcast_transactions(limit=25)


height = BLKCP.get_latest_block_height(coin_symbol='btc')



for i in HASH:

    size = i["size"]
    total = i["total"]

    satoshi_conversion = BLKCP.from_base_unit(total, 'btc')


    print(satoshi_conversion)

    # print(total)


# print('\n', satoshi_conversion)