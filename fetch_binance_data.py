# Step 1: Import libraries
import ccxt
import pandas as pd

# Step 2: Connect to Binance
exchange = ccxt.binance()

# Step 3: Fetch data
symbol = 'BTC/USDT' # choose instrument
timeframe = '1h' # defines the candle interval
limit = 10000 # download the latest {limit} {timeframe} candles

bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit) # => nested lists

# Step 4: Create DataFrame
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(bars, columns=columns)

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms') # transform from Unix timestamps

# Step 5: Save DataFrame into a CSV file
output_path = 'data/btcusdt_1h.csv'
df.to_csv(output_path, index=False)

print(f'Saved data to {output_path}')