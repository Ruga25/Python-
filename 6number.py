import yfinance as yf
import matplotlib.pyplot as plt

# Function to plot the stock graph
def make_graph(stock_data, revenue_data, title):
    # Plotting the stock closing price
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label=f'{title} Stock Price')
    plt.title(f'{title} Stock Price Graph', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Stock Price (USD)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
# Assuming gme_data is already obtained using yfinance
gme_ticker = yf.Ticker("GME")
gme_data = gme_ticker.history(period="max")

# Now calling the make_graph function to plot the graph
make_graph(gme_data, None, 'GameStop')
