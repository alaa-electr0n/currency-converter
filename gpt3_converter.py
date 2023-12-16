import requests

def currency_converter():
    from_currency = input("Enter the source currency code: ")
    to_currency = input("Enter the target currency code: ")
    amount = float(input("Enter the amount to convert: "))

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {
        "apikey": "xdcZh3idQNn1iqbpjmqn4C2jnEDIMmSE"  
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            conversion_data = response.json()
            converted_amount = conversion_data['result']
            print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        else:
            print("Failed to retrieve data. Please check your request.")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

# Call the function to start the currency converter
currency_converter()
