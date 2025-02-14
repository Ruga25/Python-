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
# Assuming tesla_data is already obtained using yfinance
tesla_ticker = yf.Ticker("TSLA")
tesla_data = tesla_ticker.history(period="max")

# Now calling the make_graph function to plot the graph
make_graph(tesla_data, None, 'Tesla')
