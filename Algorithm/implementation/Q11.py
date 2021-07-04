n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
board = [[0] * (n + 1) for _ in range(n + 1)] # 사과가 있는 칸은 1, 나머지는 0
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1
l = int(input())
changeL = []
for _ in range(l):
    x, c = input().split()
    changeL.append([x, c])

x, y = 1, 1
d = 1 # 현재 방향: 북동남서 0, 1, 2, 3
queue = [(1, 1)] # 현재 뱀의 몸이 있는 부분
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]
count = 0
while True:
    count += 1
    if len(changeL) > 0 and int(changeL[0][0]) == count - 1: # 방향전환
        _, c = changeL.pop(0)
        if c == 'L':
            d = (d - 1) % 4
        elif c == 'D':
            d = (d + 1) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 1 or nx > n or ny < 1 or ny > n or (nx, ny) in queue:
        break
    queue.append((nx, ny))
    if board[nx][ny]: # 사과가 있을 때
        board[nx][ny] = 0
    else:             # 사과가 없을 때
        queue.pop(0)
    x, y = nx, ny
    # print(queue)
print(count)