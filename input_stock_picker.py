import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.dates as mdates
from mpl_interactions import zoom_factory, panhandler

class DipSelector:
    def __init__(self, data):
        self.data = data.copy()
        self.data['Date'] = pd.to_datetime(self.data['Date']).dt.tz_localize(None)
        self.dips = []
        self.fig, self.ax = plt.subplots(figsize=(15, 8))
        self.scatter = None
        self.setup_plot()

    def setup_plot(self):
        self.ax.plot(self.data['Date'], self.data['Close'], label='Close Price', linewidth=1.5)
        self.ax.set_title('Select Dips on NVDA Chart (Use scroll to zoom, right-click to pan)')
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Price')
        self.ax.legend()
        plt.xticks(rotation=45)
        self.ax.grid(True, alpha=0.3)

        self.done_button_ax = plt.axes([0.81, 0.05, 0.1, 0.075])
        self.done_button = Button(self.done_button_ax, 'Done')
        self.done_button.on_clicked(self.on_done)

        self.undo_button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])
        self.undo_button = Button(self.undo_button_ax, 'Undo')
        self.undo_button.on_clicked(self.on_undo)

        self.clear_button_ax = plt.axes([0.59, 0.05, 0.1, 0.075])
        self.clear_button = Button(self.clear_button_ax, 'Clear All')
        self.clear_button.on_clicked(self.on_clear)

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

        zoom_factory(self.ax)
        panhandler(self.fig)

    def on_click(self, event):
        if event.inaxes == self.ax and event.button == 1:  # Left click only
            x = event.xdata
            if x is not None:
                date = pd.Timestamp(mdates.num2date(x)).tz_localize(None)
                closest_date = min(self.data['Date'], key=lambda d: abs(d - date))
                price = self.data.loc[self.data['Date'] == closest_date, 'Close'].values[0]
                
                self.dips.append((closest_date, price))
                if self.scatter:
                    self.scatter.remove()
                self.scatter = self.ax.scatter(*zip(*self.dips), color='red', s=80, zorder=5, 
                                             label='Selected Dips')
                plt.draw()

    def on_undo(self, event):
        if self.dips:
            self.dips.pop()
            if self.scatter:
                self.scatter.remove()
            if self.dips:
                self.scatter = self.ax.scatter(*zip(*self.dips), color='red', s=80, zorder=5)
            else:
                self.scatter = None
            plt.draw()

    def on_clear(self, event):
        self.dips.clear()
        if self.scatter:
            self.scatter.remove()
            self.scatter = None
        plt.draw()

    def on_done(self, event):
        plt.close()

    def get_dips(self):
        return pd.DataFrame(self.dips, columns=['Date', 'Price'])

# Date range - extended for more data
start_date = "2023-01-01"
end_date = "2025-01-01"

print("Fetching NVDA stock data...")
# Fetch stock data
stock = yf.Ticker("NVDA")
stock_data = stock.history(start=start_date, end=end_date).reset_index()
stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.tz_localize(None)

print(f"Fetched {len(stock_data)} trading days of data")

# Calculate technical indicators for dip detection
print("Calculating technical indicators...")

# Moving Averages
stock_data['MA_10'] = stock_data['Close'].rolling(window=10, min_periods=1).mean()
stock_data['MA_50'] = stock_data['Close'].rolling(window=50, min_periods=1).mean()
stock_data['MA_200'] = stock_data['Close'].rolling(window=200, min_periods=1).mean()

# Bollinger Bands
stock_data['BB_Middle'] = stock_data['Close'].rolling(window=20).mean()
bb_std = stock_data['Close'].rolling(window=20).std()
stock_data['BB_Upper'] = stock_data['BB_Middle'] + (bb_std * 2)
stock_data['BB_Lower'] = stock_data['BB_Middle'] - (bb_std * 2)
stock_data['BB_Position'] = (stock_data['Close'] - stock_data['BB_Lower']) / (stock_data['BB_Upper'] - stock_data['BB_Lower'])

# RSI (14-day)
delta = stock_data['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
stock_data['RSI'] = 100 - (100 / (1 + rs))
stock_data['RSI'].fillna(50, inplace=True)

# Volume indicators
stock_data['Volume_MA'] = stock_data['Volume'].rolling(window=20, min_periods=1).mean()
stock_data['Volume_Ratio'] = stock_data['Volume'] / stock_data['Volume_MA']

# Price action indicators
stock_data['Daily_Return'] = stock_data['Close'].pct_change()
stock_data['Volatility_20'] = stock_data['Daily_Return'].rolling(window=20).std() * np.sqrt(252)  # Annualized

# Days and decline since last high
last_high_index = 0
stock_data['Days_Since_High'] = 0
stock_data['Decline_From_High'] = 0.0

for i in range(1, len(stock_data)):
    if stock_data.loc[i, 'High'] > stock_data.loc[last_high_index, 'High']:
        last_high_index = i
    
    stock_data.loc[i, 'Days_Since_High'] = (stock_data.loc[i, 'Date'] - stock_data.loc[last_high_index, 'Date']).days
    high_price = stock_data.loc[last_high_index, 'High']
    stock_data.loc[i, 'Decline_From_High'] = (stock_data.loc[i, 'Close'] - high_price) / high_price

# Support level detection (rolling minimum)
stock_data['Support_Level'] = stock_data['Low'].rolling(window=30, min_periods=1).min()
stock_data['Distance_From_Support'] = (stock_data['Close'] - stock_data['Support_Level']) / stock_data['Support_Level']

# Recent performance
stock_data['Week_Return'] = stock_data['Close'].pct_change(periods=5)
stock_data['Month_Return'] = stock_data['Close'].pct_change(periods=20)

# MACD
exp1 = stock_data['Close'].ewm(span=12).mean()
exp2 = stock_data['Close'].ewm(span=26).mean()
stock_data['MACD'] = exp1 - exp2
stock_data['MACD_Signal'] = stock_data['MACD'].ewm(span=9).mean()
stock_data['MACD_Histogram'] = stock_data['MACD'] - stock_data['MACD_Signal']

# Stochastic Oscillator
low_min = stock_data['Low'].rolling(window=14).min()
high_max = stock_data['High'].rolling(window=14).max()
stock_data['Stoch_K'] = 100 * (stock_data['Close'] - low_min) / (high_max - low_min)
stock_data['Stoch_D'] = stock_data['Stoch_K'].rolling(window=3).mean()

# Price relative to moving averages
stock_data['Price_vs_MA50'] = (stock_data['Close'] - stock_data['MA_50']) / stock_data['MA_50']
stock_data['Price_vs_MA200'] = (stock_data['Close'] - stock_data['MA_200']) / stock_data['MA_200']

# Initialize target column
stock_data['Is_Dip'] = 0

# Select relevant features for dip detection
feature_columns = [
    "Date", "Close", "High", "Low", "Volume",
    "RSI", "BB_Position", "MACD", "MACD_Signal", "MACD_Histogram",
    "Stoch_K", "Stoch_D", "Days_Since_High", "Decline_From_High",
    "Distance_From_Support", "Week_Return", "Month_Return",
    "Price_vs_MA50", "Price_vs_MA200", "Volatility_20", "Volume_Ratio",
    "Is_Dip"
]

cleaned_data = stock_data[feature_columns].copy()

print("Launching interactive dip selector...")
# Launch interactive dip selector
selector = DipSelector(cleaned_data)
plt.show()

user_dips = selector.get_dips()

if not user_dips.empty:
    print(f"Selected {len(user_dips)} dips")
    
    # Mark selected dips
    for _, row in user_dips.iterrows():
        dip_date = pd.Timestamp(row['Date']).tz_localize(None)
        closest_date = min(cleaned_data['Date'], key=lambda d: abs(d - dip_date))
        cleaned_data.loc[cleaned_data['Date'] == closest_date, 'Is_Dip'] = 1

    print(f"Marked {cleaned_data['Is_Dip'].sum()} dips in the dataset")
else:
    print("No dips were selected")

# Save to CSV
file_path = "./nvda_dip_signals.csv"
cleaned_data.to_csv(file_path, index=False)
print(f"Data saved to '{file_path}'")

# Show summary statistics
print(f"\nDataset Summary:")
print(f"Total trading days: {len(cleaned_data)}")
print(f"Date range: {cleaned_data['Date'].min().date()} to {cleaned_data['Date'].max().date()}")
print(f"Selected dips: {cleaned_data['Is_Dip'].sum()}")
print(f"Dip percentage: {cleaned_data['Is_Dip'].mean()*100:.2f}%")

# Display first few rows
print(f"\nFirst 5 rows of processed data:")
print(cleaned_data.head())

# Plot final results
if not user_dips.empty:
    plt.figure(figsize=(15, 8))
    plt.plot(cleaned_data['Date'], cleaned_data['Close'], label='NVDA Close Price', linewidth=1.5)
    
    # Plot moving averages
    plt.plot(cleaned_data['Date'], cleaned_data.get('MA_50', cleaned_data['Close']), 
             label='50-day MA', alpha=0.7, linestyle='--')
    
    # Plot selected dips
    dip_data = cleaned_data[cleaned_data['Is_Dip'] == 1]
    if len(dip_data) > 0:
        plt.scatter(dip_data['Date'], dip_data['Close'], 
                   color='red', s=100, label='Selected Dips (Buy Points)', zorder=5, marker='v')
    
    plt.title('NVDA with Selected Dip Points (Buy Signals)')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    print(f"\nSelected dip dates and prices:")
    for _, dip in user_dips.iterrows():
        print(f"Date: {dip['Date'].date()}, Price: ${dip['Price']:.2f}")
else:
    print("No visualization created as no dips were selected.")