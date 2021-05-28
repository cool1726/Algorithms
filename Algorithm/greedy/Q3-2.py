'''
곱하기 혹은 더하기
'''

# solution 1 (0만 + 해주면 된다고 생각한 잘못된 코드)
data = input()
answer = int(data[0])
for i in range(1, len(data)):
    if answer == 0 or int(data[i]) == 0: # 이 부분만 바꿔주면 됨!
        answer += int(data[i])
    else:
        answer *= int(data[i])
print(answer)

# solution 2
# 두 수 중 하나라도 '0' or '1'인 경우 더하기(+)
# 두 수가 모두 2 이상일 때는 곱하기(x)
# 현재까지의 계산결과를 result에 담아 계속 연산 수행하기
# result가 1 이하이거나 현재 처리하고 있는 숫자가 1 이하이면 더하기(+)
# result가 2 이상이면 곱하기(x) 수행
data = input()
answer = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if answer <= 1 or num <= 1:
        answer += num
    else:
        answer *= num