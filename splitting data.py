import pandas as pd
from sklearn.model_selection import train_test_split

# Load the normalized data
file_path = 'nifty50_normalized_data_with_indicators.xlsx'
excel_data = pd.ExcelFile(file_path)

# Create a dictionary to store DataFrames for each stock
stock_data = {sheet: excel_data.parse(sheet) for sheet in excel_data.sheet_names}

# Dictionary to store split data
split_data = {}

# Split the data for each stock
for stock, df in stock_data.items():
    # Ensure the Date column is not included in the features
    X = df.drop(['Date', 'Close'], axis=1)
    y = df['Close']
    
    # Split into training (70%), validation (15%), and test (15%) sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    split_data[stock] = {
        'X_train': X_train, 'X_val': X_val, 'X_test': X_test,
        'y_train': y_train, 'y_val': y_val, 'y_test': y_test
    }

# Verify the split for one stock
print(f"Train set size: {split_data['RELIANCE_NS']['X_train'].shape}")
print(f"Validation set size: {split_data['RELIANCE_NS']['X_val'].shape}")
print(f"Test set size: {split_data['RELIANCE_NS']['X_test'].shape}")

# Save the split data to separate files (optional)
for stock, data in split_data.items():
    data['X_train'].to_csv(f'{stock}_X_train.csv', index=False)
    data['X_val'].to_csv(f'{stock}_X_val.csv', index=False)
    data['X_test'].to_csv(f'{stock}_X_test.csv', index=False)
    data['y_train'].to_csv(f'{stock}_y_train.csv', index=False)
    data['y_val'].to_csv(f'{stock}_y_val.csv', index=False)
    data['y_test'].to_csv(f'{stock}_y_test.csv', index=False)
