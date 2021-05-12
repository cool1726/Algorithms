# 6065
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
if a % 2 == 0: print(a)
if b % 2 == 0: print(b)
if c % 2 == 0: print(c)

# 6066
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
if a % 2: print("odd")
else: print("even")
if b % 2: print("odd")
else: print("even")
if c % 2: print("odd")
else: print("even")

# 6067
n = int(input())
if n > 0:
    print("D" if n % 2 else "C")
else:
    print("B" if n % 2 else "A")

# 6068
n = int(input())
if n >= 90: print('A')
elif n >= 70: print('B')
elif n >= 40: print('C')
else: print('D')

# 6069
n = input()
if n == 'A': print('best!!!')
elif n == 'B': print('good!!')
elif n == 'C': print('run!')
elif n == 'D': print('slowly~')
else: print('what?')

# 6070
n = int(input())
if n // 3 == 1: print('spring')
elif n // 3 == 2: print('summer')
elif n // 3 == 3: print('fall')
else: print('winter')

# 6071
n = -1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)

# 6072
n = int(input())
while n > 0:
    print(n)
    n -= 1

# 6073
n = int(input())
while n > 0:
    print(n - 1)
    n -= 1

# 6074
c = ord(input())
t = ord('a')
while t <= c:
    print(chr(t), end = ' ')
    t += 1

# 6075
n = int(input())
s = 0
while s <= n:
    print(s)
    s += 1

# 6076
n = int(input())
for i in range(n+1):
    print(i)

# 6077
n = int(input())
sum = 0
for i in range(0, n + 1, 2):
    sum += i
print(sum)

# 6078
c = ''
while c != 'q':
    c = input()
    print(c)

# 6079
n = int(input())
count = 0
sum = 0
while 1:
    count += 1
    sum += count
    if sum >= n:
        print(count)
        break

# 6080
n, m = input().split()
n, m = int(n), int(m)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)

# 6081
n = int(input(), 16)
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 6082
n = int(input())
for i in range(1, n + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end=' ')
    else:
        print(i, end=' ')

# 6083
# 파이썬 입출력 속도
# print('%d %d %d' %(i, j, k))
# print(i, j, k)
# print(i, k, k, sep=' ')
import itertools as it
r, g, b = map(int, input().split())
sum = r*g*b
for i in range(r):
    for j in range(g):
        for k in range(b):
            print('%d %d %d' %(i, j, k))
print(sum)

# 6084
h, b, c, s = map(int, input().split())
print(format(h * b * c * s / 1024 / 1024 / 8, ".1f"), "MB")

# 6085
w, h, b = map(int, input().split())
print(format(w * h * b / 8 / 1024 / 1024, '.2f'), "MB")

# 6086
n = int(input())
sum = 0
i = 0
while True:
    i += 1
    sum += i
    if sum >= n:
        print(sum)
        break

# 6087
n = int(input())
for i in range(1, n + 1):
    if i % 3:
        print(i, end=' ')

# 6088
# 등차수열
a, d, n = map(int, input().split())
print(a + d * (n - 1))

# 6089
# 등비수열
a, r, n = map(int, input().split())
print(a * (r ** (n-1)))

# 6090
a, m, d, n = map(int, input().split())
s = a
for i in range(1, n):
    s = s * m + d
print(s)

# 6091
a, b, c = map(int, input().split())
d = 1
while True:
    if d % a == 0 and d % b == 0 and d % c == 0:
        print(d)
        break
    d += 1

# 6092
n = int(input())
call = input().split()
d = [0 for i in range(24)]
for i in range(n):
    d[int(call[i])] += 1
for i in range(1, 24):
    print(d[i], end=' ')

# 6093
n = int(input())
call = input().split()
for i in range(n-1, -1, -1):
    print(call[i], end=' ')

# 6094
n = int(input())
s = 0
call = input().split()
for i in range(n):
    call[i] = int(call[i])
print(min(call))

# 6095
n = int(input())
d = [[0 for j in range(19)] for i in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()

# 6096
d = [list(map(int, input().split())) for _ in range(19)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        d[x-1][j] = 0 if d[x-1][j] else 1
        d[j][y-1] = 0 if d[j][y-1] else 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()

# 6097
h, w = map(int, input().split())
n = int(input())
coords = [[0 for j in range(w)] for i in range(h)]
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 1:
        for j in range(l):
            coords[x-1+j][y-1] = 1
    else:
        for j in range(l):
            coords[x-1][y-1+j] = 1
for i in range(h):
    for j in range(w):
        print(coords[i][j], end=' ')
    print()

# 6098
dx = [-1, 1, 0, 0] #좌, 우, 상, 하
dy = [0, 0, -1, 1]

def BFS(g):
    isMarked = [[False for j in range(10)] for i in range(10)]
    isinQueue = [[False for j in range(10)] for i in range(10)]
    q = [(1, 1)]
    while len(q) > 0:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 1 or nx > 10 or ny < 1 or ny > 10: continue
            if g[nx][ny] == 1: continue
            if g[nx][ny] == 0:
                g[nx][ny] = 9
                q.append((nx, ny))
            if g[nx][ny] == 2:

                break

g = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1
while g[x][y] != 1:
    if (x == 8 and y == 8) or g[x][y] == 2:
        g[x][y] = 9
        break
    elif g[x][y] == 0:
        g[x][y] = 9
    # 오른쪽 or 아래로 이동
    if g[x][y+1] != 1:
        y += 1
    elif g[x+1][y] != 1:
        x += 1
    else:
        break

for i in range(10):
    for j in range(10):
        print(g[i][j], end=' ')
    print()