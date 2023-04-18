def calculate_cost(price, tip_percent):
    return price + (price / 100 * tip_percent)


def find_most_expensive(budget, prices):
    for i in range(len(prices)):
        if prices[i] <= budget:
            return i + 1
    return False


prices = [150, 100, 90]
tip_percent = float(input())
for j in range(len(prices)):
    prices[j] = calculate_cost(prices[j], tip_percent)

print(find_most_expensive(float(input()), prices))
