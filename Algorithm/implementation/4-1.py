'''
구현문제
예제 4-1. 상하좌우
'''

n = int(input())
data = input().split()

# L R U D
dd = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]  
dy = [-1, 1, 0, 0]
cur_x, cur_y = 1, 1
for d in data:
    i = dd.index(d)
    nx = cur_x + dx[i]
    ny = cur_y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    cur_x, cur_y = nx, ny
print(cur_x,  cur_y)