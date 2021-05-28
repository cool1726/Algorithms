'''
숫자 카드 게임
'''

n, m = map(int, input().split())
answer = 0
for _ in range(n):
    data = list(map(int, input().split()))
    answer = max(answer, min(data))
print(answer)