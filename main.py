# Import necessary libraries
import requests  # To send HTTP requests to the webpage
from bs4 import BeautifulSoup  # To parse HTML content
import pandas as pd  # To store data in a structured format and export it to CSV

# URL of the iPhone page on Apple's website (India version)
url = "https://www.apple.com/in/iphone/"

# Send a GET request to the webpage to get its HTML content
response = requests.get(url)

# Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
    print("Successfully retrieved the webpage!")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Create empty lists to store the data
iphone_names = []       # List to store iPhone names
iphone_prices = []      # List to store iPhone prices
iphone_descriptions = []  # List to store iPhone descriptions
iphone_reviews = []     # List to store iPhone reviews (if available)

# Assuming that iPhone names are in 'h2' tags with class 'product-name' (this is an assumption, you need to adjust it)
iphone_elements = soup.find_all('h2', class_='product-name')

# Loop through each iPhone element and extract data
for iphone in iphone_elements:
    # Extract the name of the iPhone
    name = iphone.get_text().strip()
    iphone_names.append(name)

    # Extract the price of the iPhone (adjust the selector as per actual HTML structure)
    # Placeholder logic because Apple usually loads prices dynamically, this part might need adjustment
    price = "Price not available in HTML"  # Placeholder for now
    iphone_prices.append(price)

    # Extract the description (adjust the selector as per actual HTML structure)
    description = iphone.find_next('p').get_text().strip()  # Assuming descriptions are in the next <p> tag
    iphone_descriptions.append(description)

    # Placeholder for reviews (Apple usually doesn't have reviews on their product pages)
    review = "Reviews not available on this page"  # Placeholder, Apple doesn't usually display reviews
    iphone_reviews.append(review)

# Create a DataFrame using the data collected
data = {
    'Name': iphone_names,
    'Price': iphone_prices,
    'Description': iphone_descriptions,
    'Reviews': iphone_reviews
}

df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('iphone_data.csv', index=False)

# Confirm the CSV file has been created
print("Data has been scraped and saved to 'iphone_data.csv'.")
