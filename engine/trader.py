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
    INCREASE_THRESHOLD = 2000

    def __init__(self, trader, currency, value):
        self.trader = trader
        self.currency = currency
        self.value = value
        print 'Now starting to trade %f %s for you' % (value, currency)

    def run(self, rates):
        for r in rates:
            try:
                if ( float(r['price_usd']) <= 1 and
                    float(r['percent_change_7d']) >= self.INCREASE_THRESHOLD ):
                    print 'Invest in: %s (1 %s = %s, increase = %f)' % (r['symbol'], r['symbol'], r['price_usd'], float(r['percent_change_7d']))
            except TypeError:
                #print 'price_usd: %s,  percent_change_7d: %s' % (r['price_usd'], r['percent_change_7d'])
                pass
            except:
                pass
            if self.currency == r['symbol']:
                print 'Value in USD is: %f (1 %s = %s)' % (self.value * float(r['price_usd']), self.currency, r['price_usd'])
