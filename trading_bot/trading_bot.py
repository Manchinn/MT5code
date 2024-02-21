import MetaTrader5 as mt5
import time
from mt5_trade_functions import market_order, close_all_positions

if __name__ == '__main__':

    # open your own trading account: https://icmarkets.com/?camp=60457
    login = 10000321503
    password = 'MvD!YcW1'
    server = 'MetaQuotes-Demo'

    mt5.initialize()
    mt5.login(login, password, server)

    """
    Trading bot logic
    
    1) Opens a Trade on XAUUSD 1 lot
    2) Strategy waits 5 seconds and then closes the position
    """

    symbol = 'XAUUSD'
    volume = 20.0
    order_type = 'sell'  # values 'buy' or 'sell'

    market_order(symbol, volume, order_type)
    time.sleep(20)
    close_all_positions('all')  # accepts values 'buy', 'sell' or 'all'

