prices = [7, 1, 5, 3, 6, 4]

minimum = prices[0]
maximum_profit = 0

for i in range(1, len(prices)):
    profit = prices[i] - minimum

    if profit > maximum_profit:
        maximum_profit = profit

    if prices[i] < minimum:
        minimum = prices[i]

print(maximum_profit)