# stock_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np

# ---------- Step 1: Generate Sample Data ----------
tickers = [
    'SBIN', 'BAJFINANCE', 'TITAN', 'ITC', 'TCS', 'LT', 'TATACONSUM', 'RELIANCE',
    'HCLTECH', 'JSWSTEEL', 'ULTRACEMCO', 'POWERGRID', 'INFY', 'TRENT', 'BHARTIARTL',
    'TATAMOTORS', 'WIPRO', 'TECHM', 'NTPC', 'HINDUNILVR', 'APOLLOHOSP', 'M&M',
    'GRASIM', 'ICICIBANK', 'ADANIENT', 'ADANIPORTS', 'BEL', 'BAJAJFINSV',
    'EICHERMOT', 'COALINDIA', 'MARUTI', 'INDUSINDBK', 'ASIANPAINT', 'TATASTEEL',
    'HDFCLIFE', 'DRREDDY', 'SUNPHARMA', 'KOTAKBANK', 'SHRIRAMFIN', 'NESTLEIND',
    'ONGC', 'CIPLA', 'BPCL', 'BRITANNIA', 'SBILIFE', 'HINDALCO', 'HEROMOTOCO',
    'AXISBANK', 'HDFCBANK', 'BAJAJ-AUTO'
]

np.random.seed(42)
open_prices = np.random.randint(500, 4000, size=len(tickers))
close_prices = open_prices + np.random.randint(-100, 100, size=len(tickers))
daily_return = close_prices - open_prices
daily_return_pct = np.round((daily_return / open_prices) * 100, 2)

df = pd.DataFrame({
    "Ticker": tickers,
    "open": open_prices,
    "close": close_prices,
    "daily_return": daily_return,
    "daily_return_pct": daily_return_pct
})

# ---------- Step 2: Streamlit UI ----------
st.set_page_config(page_title="Nifty 50 Stock Dashboard", layout="wide")
st.title("📊 Nifty 50 Daily Stock Dashboard")

# 🔽 Select Ticker
selected_ticker = st.selectbox("Select a Ticker", df["Ticker"].unique())

# 🔍 Filter data
filtered = df[df["Ticker"] == selected_ticker]

# 📄 Show stock details
st.subheader(f"🔎 Details for: {selected_ticker}")
st.dataframe(filtered.style.format({"daily_return_pct": "{:.2f}%"}), use_container_width=True)

# 📈 Optional chart
st.subheader("📉 Open vs Close Price")
st.bar_chart(filtered[["open", "close"]].T)
