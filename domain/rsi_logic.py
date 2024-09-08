class RSILogic:
    @staticmethod
    def should_place_order(rsi_value, target_rsi, side):
        if side == "short" and rsi_value > target_rsi:
            return True
        elif side == "long" and rsi_value < target_rsi:
            return True
        return False
