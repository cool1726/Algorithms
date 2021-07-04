import sys

n, m = map(int, sys.stdin.readline().split())
airport = [int(sys.stdin.readline()) for _ in range(n)]

left, right = 0, max(airport) * m
res = 0

while left <= right:
    mid = (left + right) // 2
    t = sum([mid // a for a in airport]) # m초 동안 입국심사를 완료할 수 있는 인원 수
    
    if t >= m: # 총 인원수 m보다 크다면 아직 시간이 여유로움 (end = mid - 1)
        res = mid
        right = mid - 1
    else: # 총 인원수 m보다 작아 시간이 부족하다면 (start = mid + 1)
        left = mid + 1
print(res)