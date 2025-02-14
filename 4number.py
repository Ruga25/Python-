import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to extract GME revenue data using web scraping
def extract_gme_revenue_data():
    url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
    
    # Use requests to download the webpage
    response = requests.get(url)
    html_data_2 = response.text
    
    # Parse the html data with BeautifulSoup
    soup = BeautifulSoup(html_data_2, 'html.parser')
    
    # Find the relevant table (assuming it's the second table)
    table = soup.find_all('table')[1]
    
    # Extract data from rows and columns in the table
    rows = table.find_all('tr')
    headers = [header.text.strip() for header in rows[0].find_all('th')]
    
    # Extract the revenue data from the table body
    revenue_data = []
    for row in rows[1:]:
        columns = row.find_all('td')
        revenue_data.append([col.text.strip() for col in columns])
    
    # Create a DataFrame for the revenue data
    gme_revenue = pd.DataFrame(revenue_data, columns=headers)
    
    # Display the last five rows using tail function
    print("GameStop Revenue Data (Last 5 Rows):")
    print(gme_revenue.tail())

# Call the function to extract and display the revenue data
extract_gme_revenue_data()
