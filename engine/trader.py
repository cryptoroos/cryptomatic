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
# The main trading engine
# (c)CryptoRoos
# ------------------------------------------------------------------------------
class Trader:
    def __init__(self, trader, currency, value):
        self.trader = trader
        self.currency = currency
        self.value = value
        print 'Now starting to trade %f %s for you' % (value, currency)

    def run(self, rates):
        for r in rates:
            if self.currency == r['symbol']:
                print 'Value in USD is: %f (1 %s = %s)' % (self.value * float(r['price_usd']), self.currency, r['price_usd'])
