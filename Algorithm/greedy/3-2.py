''' 
2. 큰 수의 법칙
'''
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

answer = first * k * (m // k) + second * (m % k)
print(answer)