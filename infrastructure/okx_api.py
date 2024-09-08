import okx.Account as Account
import okx.Trade as Trade

class OKXAPI:
    def __init__(self, api_key, secret_key, passphrase, flag):
        self.accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
        self.tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)

    def set_leverage(self, symbol, leverage):
        return self.accountAPI.set_leverage(instId=f"{symbol}-SWAP", lever=leverage, mgnMode="isolated")

    def place_order(self, symbol, side, leverage):
        self.set_leverage(symbol, leverage)
        trade = self.tradeAPI.place_order(
            instId=f"{symbol}-SWAP",
            tdMode="isolated",
            side="sell" if side == "short" else "buy",
            posSide="net",
            ordType="market",
            sz="1"
        )
        
        if trade["code"] == "0":
            print(f"Successful order, order_id = {trade['data'][0]['ordId']}")
        else:
            print(f"Unsuccessful order, error_code = {trade['data'][0]['sCode']}, message = {trade['data'][0]['sMsg']}")
        return trade["code"]
