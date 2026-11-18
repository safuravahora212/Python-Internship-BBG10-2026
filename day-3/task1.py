prices = [299,599,888,799,199,1499,1299,799,699,799]
average = sum(prices) / len(prices)

above_avg = [p for p in prices if p > average]

print("Average:", average)
print("Prices above average:", above_avg)