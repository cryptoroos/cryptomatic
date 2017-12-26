# ------------------------------------------------------------------------------
#
#   _____                  _        _____                 
#  / ____|                | |      |  __ \                
# | |     _ __ _   _ _ __ | |_ ___ | |__) |___   ___  ___ 
# | |    | '__| | | | '_ \| __/ _ \|  _  // _ \ / _ \/ __|
# | |____| |  | |_| | |_) | || (_) | | \ \ (_) | (_) \__ \
#  \_____|_|   \__, | .__/ \__\___/|_|  \_\___/ \___/|___/
#               __/ | |                                   
#              |___/|_|                                   
#
# Automatic cryptocurrency trader
# (c)CryptoRoos
# ------------------------------------------------------------------------------
import os
import sys
import time
import argparse
import userconfig as user
from exchanges import binance as exchange
from markets import coinmarketcap as market

# Parsing the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--quantity", type=int, help="Buy/Sell Quantity", default=6)
parser.add_argument("--symbol", type=str, help="Market Symbol (Ex: IOTABTC)", default='IOTABTC')
parser.add_argument("--profit", type=float, help="Target Profit", default=1.3)
parser.add_argument("--orderid", type=int, help="Target Order Id", default=0)
parser.add_argument("--testmode", type=bool, help="Test Mode True/False", default=False)
parser.add_argument("--wait_time", type=int, help="Wait Time (seconds)", default=3)
parser.add_argument("--increasing", type=float, help="Buy Price +Increasing (0.00000001)", default=0.00000001)
parser.add_argument("--decreasing", type=float, help="Sell Price -Decreasing (0.00000001)", default=0.00000001)
option = parser.parse_args()

# Populate global variables
WAIT_TIME = option.wait_time  # seconds

# Print balances of the trader
trader = exchange.API(user.API_KEY, user.API_SECRET)

balances = trader.get_account()

tradable_currencies = {}

print ("Your portfolio is as follows:")

for balance in balances['balances'] :
    if float(balance["locked"]) > 0:
        print '%s: %s (Locked)' % (balance['asset'], balance['free'])
    elif float(balance["free"]) > 0 :
        print '%s: %s (Free)' % (balance['asset'], balance['free'])
        tradable_currencies[balance['asset']] = balance["free"]



#List tradable currencies
#for asset in tradable_currencies:
#	print '%s: %s' % (asset, tradable_currencies[asset])

# Prompt the user to ask the currency to trade in
#name = raw_input("Select the currency you want to trade in:")

name = "USDT"

if name in tradable_currencies.keys():
    trading_in = name
    trading_val = float(tradable_currencies[trading_in])
    print 'Now starting to trade in %s for you' % (trading_in)
else:
    print("Invalid currency")
    raise SystemExit()

rates = market.API()

def main():
    while True:

        startTime = time.time()
        rate = rates.get_all()
        for r in rate:
            if trading_in == r['symbol']:
                print 'Value in USD is: %f (1 %s = %s)' % (trading_val * float(r['price_usd']), trading_in, r['price_usd'])
        endTime = time.time()

        if endTime - startTime < WAIT_TIME:
            time.sleep(WAIT_TIME - (endTime - startTime))
                   
if __name__ == "__main__":
    main()
