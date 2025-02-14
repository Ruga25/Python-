import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the webpage containing the Tesla revenue data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)

# Step 2: Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the relevant table (in this case, the second table)
table = soup.find_all("table")[1]  # The table containing the Tesla revenue data

# Step 4: Parse the table headers and rows
headers = [header.get_text() for header in table.find_all('th')]  # Extract headers
rows = table.find_all('tr')[1:]  # Skip the header row

# Step 5: Extract data from the rows and store it in a list of dictionaries
data = []
for row in rows:
    cols = row.find_all('td')
    row_data = [col.get_text().strip() for col in cols]  # Get the data from each column
    data.append(row_data)

# Step 6: Create a DataFrame from the data
tesla_revenue = pd.DataFrame(data, columns=headers)

# Step 7: Display the last five rows of the DataFrame
print(tesla_revenue.tail())  # Display last five rows

