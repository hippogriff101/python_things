import requests
import time
import random

# API key
api_key = ''

# URL
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP'

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Choose a random target currency
    target_currency = random.choice(list(data['conversion_rates'].keys()))

    # Amount to convert
    amount = 100
    print("I'ma think of a random curency and tell you what its equalt to!")
    time.sleep(2)  # Pause for 1 second

    # Check if the target currency is in the conversion rates
    if target_currency in data['conversion_rates']:
        converted_amount = amount * data['conversion_rates'][target_currency]
        print(f"{amount} GBP is equal to {converted_amount:.2f} {target_currency}")
    else:
        print("Currency not found!")
else:
    print(f"Failed to retrieve data: {response.status_code}")
