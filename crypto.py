import requests
import csv
import os
import subprocess

# Step 1: Fetch the data
url = 'http://api.coincap.io/v2/assets'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers)
myjson = response.json()

# Step 2: Prepare data for CSV
ourdata = []
csvheader = ['Symbol', 'Name', 'price_USD']

# Ensure 'data' is a list of dictionaries
if isinstance(myjson.get('data'), list):
    for x in myjson['data']:
        if isinstance(x, dict):  # Ensure that each item in the list is a dictionary
            listing = [x.get('symbol'), x.get('name'), x.get('priceUsd')]
            ourdata.append(listing)
        else:
            print(f"Warning: Expected a dictionary but found {type(x)}")
else:
    print("Error: 'data' is not a list.")

# Step 3: Save CSV in the repo directory
repo_dir = r'Insert Local Repo Path'  # Path to your repo
file_path = os.path.join(repo_dir, 'crypto.csv')  # Save CSV directly in the repo

with open(file_path, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    for listing in ourdata:
        writer.writerow(listing)

print('CSV file created locally at:', file_path)