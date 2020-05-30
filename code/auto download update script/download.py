import requests
from time import time
from tickets import tickets

time_now = round(time())
total = len(tickets)

for index,ticket in enumerate(tickets):
    response = requests.get(f'https://query1.finance.yahoo.com/v7/finance/download/{ticket}?period1=0&period2={time_now}&interval=1d&events=history')
    print(f'downloading ticket:{ticket}, {index}/{total}... cmd+c or ctrl+c to stop.')
    with open(f'{ticket}.csv', 'wb') as file:
        file.write(response.content)

print('download complete.')