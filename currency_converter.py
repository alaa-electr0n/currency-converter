import requests

# ask the user to Enter The Data 

def get_data():
  while True:  
    try:
      #get input from the user
      from_currency = input("Enter The Currency You Have: ").upper()
      to_currency= input("Enter The Currency You Want To Convert To: ").upper()
      amount = float(input("How Much To Convert: "))
      #validate the user input 
      if len(from_currency) !=3 or len(to_currency)!= 3:
         raise ValueError("Please, Enter just 3 letters for Currency! like USD, EGP, EUR ...")
      if amount < 0 :
        raise ValueError("That's Not A Valid Amount of Money!")
      # if ok return the values and break the loop and exit function 
      return from_currency, to_currency, amount
    except ValueError as err:
        print(err)
    


def converter (to, from_, amount ):

  
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

  payload = {}
  headers= {
    "apikey": "xdcZh3idQNn1iqbpjmqn4C2jnEDIMmSE"
  }

  response = requests.request("GET", url, headers=headers, data = payload)

  status_code = response.status_code
  # print(status_code)
  if status_code != 200:
      print ("Please Try Again Later")
  else:
# printing result 

    result = response.json()
    user_result = result["result"]
    # print (user_result)
    print (f"Today : {result['date']}")
    print (f"{amount} {from_} = {user_result} {to}")


#calling the functions and preserving the scope

(to, from_, amount) = get_data()
converter(to, from_ , amount)