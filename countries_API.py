import requests
import pandas as pd

# API endpoint
url = 'https://restcountries.com/v3.1/all'

# Make the request
response = requests.get(url)
data = response.json()