import yfinance as yf
import pandas as pd
import ta

# List of NIFTY 50 stock tickers in NSE format
nifty50_tickers = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "HINDUNILVR.NS",
    "ITC.NS", "ICICIBANK.NS", "KOTAKBANK.NS", "SBIN.NS", "AXISBANK.NS",
    "LT.NS", "BAJFINANCE.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "SUNPHARMA.NS",
    "TITAN.NS", "ULTRACEMCO.NS", "TATASTEEL.NS", "ONGC.NS", "HCLTECH.NS",
    "POWERGRID.NS", "NTPC.NS", "WIPRO.NS", "M&M.NS", "MARUTI.NS",
    "TECHM.NS", "DRREDDY.NS", "TATAMOTORS.NS", "NESTLEIND.NS", "INDUSINDBK.NS",
    "SBILIFE.NS", "GRASIM.NS", "CIPLA.NS", "BAJAJFINSV.NS", "HEROMOTOCO.NS",
    "ADANIPORTS.NS", "DIVISLAB.NS", "BRITANNIA.NS", "JSWSTEEL.NS", "BPCL.NS",
    "HINDALCO.NS", "COALINDIA.NS", "EICHERMOT.NS", "SHREECEM.NS", "UPL.NS",
    "IOC.NS", "TATACONSUM.NS", "DABUR.NS", "PIDILITIND.NS"
]

# Create a new Excel writer object
writer = pd.ExcelWriter('nifty50_historical_data_with_indicators.xlsx', engine='openpyxl')

# Function to fetch and save data with indicators
def fetch_and_save_data(symbol):
    df = yf.download(symbol, start="2015-01-01", end="2024-07-19", interval='1d')
    if not df.empty:
        # Calculate Technical Indicators
        df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
        df['EMA_20'] = ta.trend.ema_indicator(df['Close'], window=20)
        df['RSI_14'] = ta.momentum.rsi(df['Close'], window=14)
        df['MACD'] = ta.trend.macd(df['Close'])
        df['MACD_Signal'] = ta.trend.macd_signal(df['Close'])
        bb = ta.volatility.BollingerBands(close=df['Close'], window=20, window_dev=2)
        df['BB_High'] = bb.bollinger_hband()
        df['BB_Low'] = bb.bollinger_lband()
        df['VWAP'] = ta.volume.volume_weighted_average_price(df['High'], df['Low'], df['Close'], df['Volume'])
        df['Stochastic_Oscillator'] = ta.momentum.stoch(df['High'], df['Low'], df['Close'], window=14, smooth_window=3)
        df['CCI'] = ta.trend.cci(df['High'], df['Low'], df['Close'], window=20)
        
        # Check for missing values and handle them
        df.ffill(inplace=True)
        df.bfill(inplace=True)
        
        # Save the dataframe to a sheet in the Excel file
        df.to_excel(writer, sheet_name=symbol.replace('.', '_'))
        print(f"Data for {symbol} fetched and saved successfully!")
    else:
        print(f"Failed to fetch data for {symbol}")

# Fetch data for all NIFTY 50 stocks
for stock in nifty50_tickers:
    fetch_and_save_data(stock)

# Save and close the Excel writer
writer.close()
print("All data has been fetched and saved to nifty50_historical_data_with_indicators.xlsx")
