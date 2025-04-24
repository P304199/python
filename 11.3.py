import pandas as pd

asking_prices = pd.Series([10000, 15000, 12000, 25000, 18000])
fair_prices = pd.Series([12000, 14000, 15000, 23000, 19000])

good_deals = asking_prices[asking_prices < fair_prices].index

print("Good deals (indices of cars where asking price < fair price):")
print(good_deals)
