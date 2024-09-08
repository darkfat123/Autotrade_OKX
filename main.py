import time
from config import config
from infrastructure.okx_api import OKXAPI
from infrastructure.tradingview_api import TradingViewAPI
from application.trade_service import TradeService

def main():
    api_key, secret_key, passphrase = config.load_config()

    flag = "1"  # Production: 0, Demo: 1
    symbol = input("Enter Symbol: ").upper() + "-USDT"
    side = input("Enter long/short: ")
    leverage = input("Enter Leverage: ")
    interval = input("Enter Interval: ")
    target_rsi = float(input("Enter RSI value: "))

    tradingview_api = TradingViewAPI()
    okx_api = OKXAPI(api_key, secret_key, passphrase, flag)
    trade_service = TradeService(tradingview_api, okx_api)

    print(f"Monitoring {symbol} for {side} position with {leverage}x leverage.")
    trade_service.monitor_rsi_and_trade(symbol, side, target_rsi, leverage, interval)

if __name__ == "__main__":
    main()
