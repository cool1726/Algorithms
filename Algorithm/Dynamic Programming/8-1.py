# 한 번 계산된 결과를 메모이제이션하기 위한 리스트
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(4))

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]