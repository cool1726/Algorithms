dx = [-1, 1, 0, 0] # 좌 우 상 하
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

def BFS(G):
    queue = [(0, 0)] # 시작 위치 [0][0]

    while len(queue) > 0:
        cur = queue.pop(0) # 현재 위치 [cur_r, cur_c]
        for i in range(4): # 상하좌우로 한 칸씩 움직일 위치 nr, nc
            nr = cur[0] + dx[i]
            nc = cur[1] + dy[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m: # 미로 범위를 넘어가면 무시하기
                continue
            # 이미 지나온 길이면 무시하기 (2 이상일 경우)
            if G[nr][nc] == 0: continue # 0은 이동할 수 없는 칸
            if G[nr][nc] == 1: # 1은 이동할 수 있는 칸
                G[nr][nc] = G[cur[0]][cur[1]] + 1
                queue.append([nr, nc])
            
    return G[n-1][m-1]

print(BFS(maze))