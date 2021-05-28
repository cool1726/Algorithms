'''
만들 수 없는 금액
'''

# solution 1 
# 화폐 단위가 큰 것부터(내림차순) 만들 수 있는 금액 계산
n = int(input())
coin = list(map(int, input().split()))
answer = 1
coin.sort(reverse=True)
while True:
    temp = answer
    for i in coin:
        if temp >= i:
            temp -= i
    if temp == 0:
        answer += 1
    else:
        break
print(answer)

# solution 2 ★★★
# 화폐 단위가 작은 것부터(오름차순) 만들 수 있는 (최고)금액을 갱신해 나가는 것
# 1부터 answer -1 까지의 모든 금액을 만들 수 있는지 확인
n = int(input())
coin = list(map(int, input().split()))
coin.sort()

answer = 1
for x in coin:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if answer < x:
        break
    answer += x
print(answer)