import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data from the CSV file
file_path = 'TCS_NS_X_test.csv'
stock_data = pd.read_csv(file_path)

# Display the first few rows to understand the data structure
print(stock_data.head())

# Visualize the adjusted closing price for TCS
plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data['Adj Close'], label='Adjusted Close Price')
plt.title('Adjusted Closing Price of TCS')
plt.xlabel('Index')
plt.ylabel('Adjusted Close Price')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Plot correlation matrix for TCS
plt.figure(figsize=(12, 8))
correlation_matrix = stock_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for TCS')
plt.show()

# Additional Visualizations
# 1. Volume traded over time
plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data['Volume'], label='Volume Traded', color='orange')
plt.title('Volume Traded for TCS')
plt.xlabel('Index')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# 2. High and Low prices over time
plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data['High'], label='High Price', color='green')
plt.plot(stock_data.index, stock_data['Low'], label='Low Price', color='red')
plt.title('High and Low Prices of TCS')
plt.xlabel('Index')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# 3. Distribution of adjusted closing prices
plt.figure(figsize=(12, 6))
sns.histplot(stock_data['Adj Close'], kde=True)
plt.title('Distribution of Adjusted Closing Prices for TCS')
plt.xlabel('Adjusted Close Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 4. Moving average of adjusted closing prices
stock_data['Adj Close_MA50'] = stock_data['Adj Close'].rolling(window=50).mean()
plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data['Adj Close'], label='Adjusted Close Price')
plt.plot(stock_data.index, stock_data['Adj Close_MA50'], label='50-Day MA', color='purple')
plt.title('50-Day Moving Average of Adjusted Closing Prices for TCS')
plt.xlabel('Index')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
