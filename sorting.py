stocks = {
    'GOOGLE' : 520.25, 
    'FACEBOOK' : 56.34,
    'APPLE' : 78.30,
    'AMAZON' : 293.35,
    'YAHOO' : 46.30,
}

print(sorted(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(min(zip(stocks.values(), stocks.keys())))