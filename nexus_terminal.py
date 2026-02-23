import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(layout="wide", page_title="NEXUS Terminal")

# --- SIDEBAR CONTROLS ---
st.sidebar.title("NEXUS CONTROL")
ticker = st.sidebar.text_input("Asset Ticker", value="BTC-USD").upper()
timeframe = st.sidebar.selectbox("Timeframe", ["1mo", "3mo", "6mo", "1y", "5y", "max"])
overlay = st.sidebar.multiselect("Technical Indicators", ["SMA 50", "SMA 200", "EMA 20"])

# --- DATA ENGINE ---
def load_data(ticker, period):
    try:
        data = yf.download(ticker, period=period)
        return data
    except Exception as e:
        st.error(f"Data Fetch Error: {e}")
        return None

# --- MAIN DASHBOARD ---
st.title(f"⚡ NEXUS: Market Intelligence | {ticker}")

data = load_data(ticker, timeframe)

if data is not None and not data.empty:
    # 1. METRIC CARDS
    current_price = data['Close'].iloc[-1]
    prev_price = data['Close'].iloc[-2]
    delta = current_price - prev_price
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", f"${current_price:,.2f}", f"{delta:,.2f}")
    col2.metric("Volume", f"{data['Volume'].iloc[-1]:,}")
    col3.metric("High (Period)", f"${data['High'].max():,.2f}")

    # 2. INTERACTIVE CHART (Plotly)
    fig = go.Figure()

    # Candlestick Trace
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    name='Price'))

    # Technical Indicators Logic
    if "SMA 50" in overlay:
        sma50 = data['Close'].rolling(window=50).mean()
        fig.add_trace(go.Scatter(x=data.index, y=sma50, mode='lines', name='SMA 50', line=dict(color='cyan')))
    
    if "SMA 200" in overlay:
        sma200 = data['Close'].rolling(window=200).mean()
        fig.add_trace(go.Scatter(x=data.index, y=sma200, mode='lines', name='SMA 200', line=dict(color='orange')))
        
    if "EMA 20" in overlay:
        ema20 = data['Close'].ewm(span=20, adjust=False).mean()
        fig.add_trace(go.Scatter(x=data.index, y=ema20, mode='lines', name='EMA 20', line=dict(color='magenta')))

    # Chart Styling (Dark Mode)
    fig.update_layout(height=600, template="plotly_dark", title_text="")
    st.plotly_chart(fig, use_container_width=True)

    # 3. RAW DATA INSPECTOR
    with st.expander("Incoming Data Stream (Raw)"):
        st.dataframe(data.tail(10))

else:
    st.warning("Waiting for Satellite Link... (Check Ticker Symbol)")

# --- FOOTER ---
st.markdown("---")
st.caption("SYSTEM STATUS: ONLINE | POWERED BY PYTHON & STREAMLIT")
