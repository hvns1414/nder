import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def generate_signals(data):
    data['SMA50'] = data['Close'].rolling(window=50).mean()
    data['SMA200'] = data['Close'].rolling(window=200).mean()
    data['Signal'] = 0
    data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1  # Buy
    data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1 # Sell
    return data

def plot_stock_chart(data, ticker):
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['Close'], label='Close Price', color='cyan')
    ax.plot(data.index, data['SMA50'], label='SMA 50', color='yellow', linestyle='dashed')
    ax.plot(data.index, data['SMA200'], label='SMA 200', color='red', linestyle='dashed')
    
    buy_signals = data[data['Signal'] == 1]
    sell_signals = data[data['Signal'] == -1]
    ax.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Buy Signal', alpha=1, zorder=3)
    ax.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Sell Signal', alpha=1, zorder=3)
    
    ax.set_title(f"Stock Prediction for {ticker}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    plt.savefig("stock_chart.png", dpi=300)
    plt.close()

def main():
    ticker = input("Enter stock ticker (e.g., AAPL): ")
    data = fetch_stock_data(ticker)
    data = generate_signals(data)
    plot_stock_chart(data, ticker)
    print("Stock chart saved as 'stock_chart.png'")

if __name__ == "__main__":
    main()
