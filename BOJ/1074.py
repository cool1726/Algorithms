n, r, c = map(int, input().split())

loc = [[0, 1], [2, 3]]
size = 2 ** n
answer = 0

while size >= 2:
    size = size // 2  # N > 1이므로 2^(N-1) * 2^(N-1)으로 4등분
    nr = r // size
    nc = c // size
    now = loc[nr][nc]
    r %= size
    c %= size
    answer += size * size * now
print(answer)