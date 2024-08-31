import requests
import time

#API key
api_key = ''

# URL
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP'


    
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    

amount = int(input("Please enter a whole number that I will convert from GBP to a curency of your choise: "))
time.sleep(1)
target_currency = input("Please enter a curency code: ")

if target_currency in data['conversion_rates']:
    converted_amount = amount * data['conversion_rates'][target_currency]
    print(f"{amount} GBP is equal to {converted_amount:.2f} {target_currency}")
else:
    print("Currency not found!")




