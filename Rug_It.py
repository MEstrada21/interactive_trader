# import dash
# import dash_bootstrap_components as dbc
# from dash import dcc, html
# from dash.dependencies import Input, Output, State
# from page_1 import page_1
# from order_page import order_page
# from error_page import error_page
# from navbar import navbar
# from sidebar import sidebar, SIDEBAR_HIDDEN, SIDEBAR_STYLE
# from dash.dependencies import Input, Output
# from dash.exceptions import PreventUpdate
from interactive_trader import *
# from datetime import datetime
from ibapi.contract import Contract
# from ibapi.order import Order
# import time
# import threading
import pandas as pd

import finta as finta
import numpy as np

# import scipy as sp


# asset_a = fetch_historical_data(assets[0])
# print (asset_a)
# asset_B = fetch_contract_details(assets[1])

value = "AUD.USD"  # This is what your text input looks like on your app


# Create a contract object
def data_pull(forex_asset):
    contract = Contract()
    contract.symbol = forex_asset.split('.')[0]
    contract.secType = 'CASH'
    contract.exchange = 'IDEALPRO'  # 'IDEALPRO' is the currency exchange.
    contract.currency = forex_asset.split(".")[1]

    data = fetch_historical_data(contract)
    dataframex = pd.DataFrame(data)[['date', 'open', 'high', 'low', 'close']]

    return dataframex


# asset_a = data_pull("AUD.USD")
# asset_b = data_pull("NZD.USD")
# print(asset_b['close'])

def data_clean_and_calculate(asset_a, asset_b,):
    asset_a = data_pull(asset_a)[['date', 'close']]
    asset_b = data_pull(asset_b)[['date', 'close']]
    window = int(window)
    pair_data = pd.merge(asset_a, asset_b, on='date')
    pair_data.columns = ['date', 'asset_a', 'asset_b']
    # convert date to datetime
    pair_data['date'] = pd.to_datetime(pair_data['date'])

    def calculate_log_spread(row):
        return np.log(row['asset_a'] / row['asset_b'])

    pair_data['log_spread'] = pair_data.apply(calculate_log_spread, axis=1)

    # def calculate_moving_average(row, ma_parameter):
    #     moving_average = finta.SMA(row['log_spread'], ma_parameter)
    #     return moving_average
    #
    # pair_data['moving_average'] = pair_data.apply(calculate_moving_average, axis=1)

    return pair_data


def calculate_moving_average(row, ma_parameter):
    moving_average = finta.SMA(row['log_spread'], ma_parameter)
    return moving_average


data = data_clean_and_calculate("AUD.USD", "NZD.USD", 8)

print(data)

# asset_b = data_pull(currency_assets[1])


# Get your historical data


# asset_B = pd.DataFrame(fetch_contract_details(assets[1]))

# print(asset_A)
#
#
#

#     def rug_it(hist_data, candle_avg, tsh_sell,stop_loss_a,stop_loss_b, lot_size_a, lot_size_b,):
#     for
