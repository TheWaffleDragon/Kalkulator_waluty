#from flask import Flask,render_template
#czesc I : odczyt kursow ze strony
import csv
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
d = data[0]
rates = d['rates']

with open('rates.csv','w', encoding="utf-8", newline='') as csvfile:
    headers = ['currency', 'code', 'bid', 'ask']
    write = csv.DictWriter(csvfile, fieldnames= headers, delimiter = ';' )
    write.writeheader()
    for x in rates:
        write.writerow({'currency': x.get('currency'), 'code':x.get('code'),'bid': x.get('bid'), 'ask':x.get('ask')})
