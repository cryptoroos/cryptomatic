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

trader = exchange.API(user.API_KEY, user.API_SECRET)

balances = trader.get_account()

for balance in balances['balances'] :
    if float(balance["locked"]) > 0:
        print '%s: %s (Locked)' % (balance['asset'], balance['free'])
    elif float(balance["free"]) > 0 :
        print '%s: %s (Free)' % (balance['asset'], balance['free'])

