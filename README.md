# NEXUS: Financial Intelligence Terminal 💹

A professional-grade market dashboard built with **Streamlit** and **Plotly**. This application provides real-time interactive charting for Cryptocurrencies, Stocks, and Forex.

## ⚡ Features
* **Live Data Feed:** Connects to Yahoo Finance API for real-time asset pricing.
* **Interactive Cartography:** Zoomable/Pannable Candlestick charts powered by Plotly.
* **Technical Analysis Layer:** Toggleable overlays for Moving Averages (SMA 50/200) and Exponential Moving Averages (EMA).
* **Metrics Engine:** Automatic calculation of daily delta and volume spikes.

## 🛠️ Technology Stack
* **Frontend:** Streamlit (Python-based UI Framework)
* **Visualization:** Plotly (Interactive Graphing)
* **Data Engineering:** YFinance & Pandas

## 🚀 Usage
1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Launch the Terminal:**
    ```bash
    streamlit run nexus_terminal.py
    ```
3.  **Operation:**
    * The dashboard will open in your default web browser (Localhost:8501).
    * Enter any ticker (e.g., `NVDA`, `ETH-USD`, `TATASTEEL.NS`) in the sidebar to load the asset.
