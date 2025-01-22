from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Load the Excel file
file_path = 'nifty50_historical_data_with_indicators.xlsx'
excel_data = pd.ExcelFile(file_path)

# Create a dictionary to store DataFrames for each stock
stock_data = {sheet: excel_data.parse(sheet) for sheet in excel_data.sheet_names}

# Create the scaler object
scaler = MinMaxScaler()

# Columns to be normalized
columns_to_scale = [
    'Open', 'High', 'Low', 'Close', 'Volume', 'SMA_20', 'EMA_20', 'RSI_14',
    'MACD', 'MACD_Signal', 'BB_High', 'BB_Low', 'VWAP', 'Stochastic_Oscillator', 'CCI'
]

# Normalize the data for each stock
for stock, df in stock_data.items():
    # Ensure 'Date' column is not included in the scaling
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    stock_data[stock] = df

# Verify normalization for one stock
print(stock_data['RELIANCE_NS'].head())

# Save the normalized data back to the Excel file without the extra index column
with pd.ExcelWriter('nifty50_normalized_data_with_indicators.xlsx', engine='openpyxl') as writer:
    for stock, df in stock_data.items():
        df.to_excel(writer, sheet_name=stock.replace('.', '_'), index=False)
