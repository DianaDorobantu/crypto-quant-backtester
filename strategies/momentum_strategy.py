import pandas as pd
from strategies.base_strategy import BaseStrategy


class MomentumStrategy(BaseStrategy):

    def __init__(self, window: int = 20):
        self.window = window

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:

        df = data.copy()

        df['returns'] = df['close'].pct_change()
        df['momentum'] = df['close'].pct_change(self.window)

        df['signal'] = 0

        df.loc[df['momentum'] > 0, 'signal'] = 1
        df.loc[df['momentum'] < 0, 'signal'] = -1

        return df