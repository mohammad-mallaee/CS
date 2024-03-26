coins = {1, 4, 5}
sum = 500

def count_ways(coins, sum):
    if sum == 0:
        return 1
    ways = 0
    for coin in coins:
        if sum >= coin:
            ways += count_ways(coins, sum - coin)
    return ways

def count_ways_2(coins, sum):
    memo = [0] * (sum + 1)
    memo[0] = 1
    for i in range(1, sum + 1):
        memo[i] = 0
        for coin in coins:
            if sum >= coin:
                memo[i] = memo[i] + memo[i - coin]
    return memo[sum]
print(count_ways_2(coins, sum))