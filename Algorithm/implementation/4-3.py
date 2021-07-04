'''
구현
실전문제: 왕실의 나이트
'''

n = input()
row = int(n[1])
col = int(ord(n[0]) - ord('a')) + 1

# (r, c) : 행, 열 순서 8가지
# 방향 상관없이 모든 경우를 따져야 하므로 row, col 순서 상관 없음
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)] 

answer = 0
for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if nrow < 1 or ncol < 1 or nrow > 8 or ncol > 8:
        continue
    answer += 1
print(answer)