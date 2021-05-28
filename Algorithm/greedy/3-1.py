'''
Greedy Algorithm
Example 3-1
거스름돈 계산

시간복잡도
화폐의 종류가 K개일 때 시간복잡도 O(K)
'''

n = 1260
count = 0

# 큰 단위 화폐부터 차례대로
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)