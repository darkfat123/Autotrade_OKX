from tradingview_ta import TA_Handler

class TradingViewAPI:
    def get_rsi(self, symbol, interval):
        handler = TA_Handler(symbol=symbol, screener="Crypto", exchange="OKX", interval=interval)
        analysis = handler.get_analysis()
        return analysis.indicators["RSI"]
