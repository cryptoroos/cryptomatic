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
# API for CoinMarketCap: Cryptocurrency Market Capitalizations
#         https://coinmarketcap.com/
# (c)CryptoRoos
# ------------------------------------------------------------------------------
import requests

class API:
    BASE_URL    = "https://api.coinmarketcap.com/v1/ticker/"
    
    def __init__(self):
        pass
    
    def get_all(self):
        return self._get("limit=0")

    def _get(self, query={}):
        url = "%s?%s" % (self.BASE_URL, query)
        header = {}
        return requests.get(url, headers=header, \
            timeout=30, verify=True).json()
