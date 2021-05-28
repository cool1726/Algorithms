'''
1이 될 때까지
'''

# sol1: N이 K의 배수가 될 때까지 반복해 1을 빼거나, K의 배수가 되면 K로 나누기
n, k = map(int, input().split())
count = 0
while n > 0:
    if n == 1:
        break
    if n % k:
        n -= 1
    else:
        n //= k
    count += 1
print(count)

# sol2: N이 K의 배수가 될 때까지의 수를 한번에 빼는 것 (반복문 실행횟수를 줄여줌)
n, k = map(int, input().split())
count = 0
while n > 0:
    if n == 1:
        break
    target = n % k
    count += target
    n -= target
    n //= k
    count += 1
print(count)