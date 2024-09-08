import time
from domain.rsi_logic import RSILogic

class TradeService:
    def __init__(self, tradingview_api, okx_api):
        self.tradingview_api = tradingview_api
        self.okx_api = okx_api

    def monitor_rsi_and_trade(self, symbol, side, target_rsi, leverage, interval):
        while True:
            rsi_value = self.tradingview_api.get_rsi(symbol.replace("-", ""), interval)
            print(f"RSI: {rsi_value}")

            if RSILogic.should_place_order(rsi_value, target_rsi, side):
                self.okx_api.place_order(symbol, side, leverage)
                break
            else:
                time.sleep(2)
