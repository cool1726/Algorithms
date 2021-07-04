def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = list_2d[i][j]
    return new

def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    
    # 4번의 회전 key 모두 확인
    for rotate in range(4):
        key = rotate_2d(key)
        # 전체 new_lock과 key 비교하며 찾기
        for x in range(n * 2):
            for y in range(n * 2):
                # key가 겹쳐진 부분에 대해 new_lock + key
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 자물쇠의 중간부분이 1인지 체크
                if check(new_lock):
                    return True
                # new_lock - key
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False