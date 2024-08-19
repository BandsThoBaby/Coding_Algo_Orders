import ccxt
import key_file as k
import time
import schedule

# Connect Exchange
binance = ccxt.binance({
    'enableRateLimit': True,
    'apiKey': k.XP_Key,
    'secret': k.XP_Secret
})

# Fetch and print balance, only showing non-zero balances
balance = binance.fetch_balance()

symbol = 'BTC/USDT'
size = 1  # Size = number of contracts
bid = 30000
params = {'timeInForce': 'PostOnly'}

# Making an order
# order = binance.create_limit_buy_order(symbol, size, bid, params)
# print("Order details:", order)

# cancel order
# binance.cancel_all_orders(symbol)

# sleep 10 seconds
# print ('just made the order now sleepings for 10s..')
# time.sleep(10)

# cancel order
# binance.cancel_all_orders(symbol)


'''
### HOW TO LOOP/CANCEL - REPEAT ORDERS 

go = True

while go == True:

    binance.create_limit_buy_order(symbol, size, bid, params)

    time.sleep(5)

    binance.cancel_all_orders(symbol)


'''

def bot():

    binance.create_limit_buy_order(symbol, size, bid, params)

    time.sleep(5)

    binance.cancel_all_orders(symbol)

schedule.every(28).seconds.do(bot)

while True:
    try:
        schedule.run_pending()
    except:
        print('+++++ MAYBE AN INTERNET PROB OR SOMETHING')
        time.sleep(30)
        

