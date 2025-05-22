# 📈 Stock Signal Visualization Tool

This Python script fetches historical stock data using Yahoo Finance, calculates trading signals based on the SMA (Simple Moving Average) crossover strategy, and generates a chart with buy/sell indicators.

---

## 🔍 Features

- Retrieves historical stock price data (default: last 6 months)
- Computes:
  - 50-day Simple Moving Average (SMA)
  - 200-day Simple Moving Average (SMA)
- Detects:
  - Buy signals (SMA50 > SMA200)
  - Sell signals (SMA50 < SMA200)
- Generates a clean and styled chart:
  - Price line (cyan)
  - SMA50 (yellow dashed)
  - SMA200 (red dashed)
  - Buy signals (green ↑)
  - Sell signals (red ↓)

---

## 📦 Requirements

Install the required Python libraries:
```bash
pip install yfinance matplotlib pandas
🚀 Usage
Run the script:

bash
Kopyala
Düzenle
python stock_signals.py
You'll be prompted:

java
Kopyala
Düzenle
Enter stock ticker (e.g., AAPL):
The script will:

Fetch the data

Calculate the signals

Save a plot as stock_chart.png in the working directory

📁 Output
The script produces:

A static chart image: stock_chart.png showing price, SMA lines, and buy/sell signals

Example visualization:

java
Kopyala
Düzenle
[ Close Price Graph ]
     ↑ green arrow = Buy
     ↓ red arrow   = Sell

