'''
모험가 길드
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()
# solution 1 (mine)
answer = 0
index = 0 #현재 가리키고 있는 모험가
while True:
    if len(data[index:]) < data[index]: #현재 그룹에 포함된 모험가 수가 현재의 공포도 이하라면 모험가 계속 추가
        index += 1
        continue
    for i in range(data[index]): #현재 공포도만큼 모험가 인원 설정
        index += 1
    if index >= len(data): #마지막 모험가까지 살펴봤다면 끝
        break
    answer += 1
print(answer)

# solution 2
answer = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수
for i in data: #공포도를 낮은 것부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        answer += 1 #총 그룹 수 증가, 현재 그룹에 포함된 모함가의 수 초기화
        count = 0
print(answer)