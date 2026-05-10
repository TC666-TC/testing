import yfinance as yf
import pandas as pd

stocks = ["AAPL", "0700.HK", "NVDA"]

with pd.ExcelWriter("my_stocks.xlsx") as writer:
    for s in stocks:
        df = yf.download(s, period="1mo")
        df.to_excel(writer, sheet_name=s)