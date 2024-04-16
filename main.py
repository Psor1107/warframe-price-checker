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

total = {}

length = len(orders)
for x in range(length):
   total[x] = orders[x]['platinum']

average_price = mean(total.values())

print("These are the values listed for the item:\n", sorted(total.values()))
print("The average price for the item is: %.2f" % average_price)