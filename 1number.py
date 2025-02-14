# Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# 1. Extract Stock Data using yfinance
def get_stock_data(ticker):
    # Create ticker object
    stock_ticker = yf.Ticker(ticker)
    
    # Get historical stock data for the max period
    stock_data = stock_ticker.history(period="max")
    
    # Return stock data
    return stock_data

# Get GameStop (GME) stock data
gme_data = get_stock_data("GME")

# 2. Data Processing: Reset index and display the first few rows of data
gme_data.reset_index(inplace=True)
print(gme_data.head())

# 3. Plotting GameStop Stock Data using Matplotlib
def plot_stock_data(stock_data):
    plt.figure(figsize=(10,6))
    plt.plot(stock_data['Date'], stock_data['Close'], label='GameStop Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.title('GameStop Stock Price Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot the stock data
plot_stock_data(gme_data)

# 4. Build a Dashboard using Dash to visualize GameStop stock data
app = dash.Dash(__name__)

# Define layout for the Dash app
app.layout = html.Div([
    html.H1("GameStop Stock Dashboard"),
    dcc.Graph(
        id='stock-graph',
        figure={
            'data': [
                go.Scatter(
                    x=gme_data['Date'],
                    y=gme_data['Close'],
                    mode='lines',
                    name='Stock Price'
                ),
            ],
            'layout': go.Layout(
                title='GameStop Stock Prices Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Stock Price (USD)'},
                template='plotly_dark'
            )
        }
    ),
    html.Div([
        html.H4("Stock Data Summary:"),
        html.P(f"Total Rows: {len(gme_data)}"),
        html.P(f"Start Date: {gme_data['Date'].min()}"),
        html.P(f"End Date: {gme_data['Date'].max()}")
    ])
])

# Run the Dash web application
if __name__ == '__main__':
    app.run_server(debug=True)
