import pandas as pd

data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)
print(purchases)

print("---------")
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)
print("---------")
fruttaDiHune = purchases.loc['June']
print(fruttaDiHune)
