import pandas as pd

# Load the Excel file
file_path = 'nifty50_historical_data_with_indicators.xlsx'
excel_data = pd.ExcelFile(file_path)

# Create a dictionary to store DataFrames for each stock
stock_data = {sheet: excel_data.parse(sheet) for sheet in excel_data.sheet_names}

# Display the first few rows of data for one of the stocks
print(stock_data['RELIANCE_NS'].head())

for stock, df in stock_data.items():
    # Check for remaining missing values
    print(f"{stock}: {df.isnull().sum().sum()} missing values")
