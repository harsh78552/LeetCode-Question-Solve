def BuySellStock(prices):
    more_profit = 0
    min_price = prices[0]
    for num in prices:
        more_profit = max(more_profit, num - min_price)
        min_price = min(min_price, num)
    return more_profit


print(BuySellStock([7, 1, 5, 3, 6, 4]))
print(BuySellStock([7, 6, 4, 3, 1]))
