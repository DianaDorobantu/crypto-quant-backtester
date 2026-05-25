import pandas as pd
from abc import ABC, abstractmethod

class BaseStrategy(ABC):

    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        pass
