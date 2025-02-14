import yfinance as yf
import pandas as pd

# Step 1: Use yfinance to create a ticker object for GameStop (GME)
gme_ticker = yf.Ticker("GME")

# Step 2: Extract historical stock data for GameStop with the maximum period
gme_data = gme_ticker.history(period="max")

# Step 3: Reset the index of the gme_data DataFrame
gme_data.reset_index(inplace=True)

# Step 4: Display the first five rows of the gme_data DataFrame
print(gme_data.head())
