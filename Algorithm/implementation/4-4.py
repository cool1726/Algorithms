'''
구현
실전문제: 게임개발
'''
n, m = map(int, input().split())
x, y, d = map(int, input().split())
# d : 0 1 2 3 (북 동 남 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

answer = 1
while True:
    maps[x][y] = 2
    flag = 0
    for i in range(4):
        # 1. 왼쪽으로 회전
        if d == 0:
            d = 3
        else:
            d -= 1
        nx = x + dx[d]
        ny = y + dy[d]
        # 유효한 범위가 아니라면 패스
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        # 2. d 방향으로 한 칸 이동한 곳이 (방문한 적 없는) 육지일 때 이동 확정
        if maps[nx][ny] == 0:
            x = nx
            y = ny
            answer += 1
            break
        nx = x + dx[(d + 2) % 4]
        ny = y + dy[(d + 2) % 4]
        # 3. 네 방향 모두 가본 칸이라면 뒤로 가기
        if i == 3 and maps[nx][ny] == 2:
            x = nx
            y = ny
        # 3. 네 방향 모두 갈 수 없고 뒤가 바다라면
        elif i == 3 and maps[nx][ny] == 1:
            flag = 1
    if flag == 1:
        break
print(answer)