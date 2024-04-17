import requests
from statistics import mean
import json
from operator import itemgetter

api_url = "https://api.warframe.market/v1/items/mirage_prime_systems/orders"
response = requests.get(api_url)
data = response.json()

with open('data.json', 'w') as f:
    json.dump(data, f)

orders = data['payload']['orders']

#total = []
#for order in orders:
#   total.append(order['platinum'])

total = [order['platinum'] for order in orders]

average_price = mean(total)
print("These are the values listed for the item:\n", sorted(total))
print(f"The average price for the item is: {average_price:.2f}")