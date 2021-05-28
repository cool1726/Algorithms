'''
볼링공 고르기
'''
n, m = map(int, input().split())
data = list(map(int, input().split()))
weight = [0] * 10  # [0 for _ in range(m)]과 같은 표현
for i in data:
    weight[i - 1] += 1
answer = 0
for i in range(m):
    n -= weight[i] #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    answer += weight[i] * n #B가 선택하는 경우의 수와 곱하기
print(answer)