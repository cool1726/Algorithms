# 리스트 blist, 찾는 값 x
def binary_search(blist, x):
    left, right = 0, len(blist) - 1
    res = 0

    while left <= right:
        mid = (left + right) // 2
        if x == blist[mid]: # 원하는 값 x를 발견하면 x가 발견된 인덱스(위치)를 반환
            return mid
        elif x > blist[mid]: # 찾는 값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
            left = mid + 1
        else: # 찾는 값이 더 작으면 왼쪽으로 범위를 좁혀 게속 탐색
            right = mid - 1
    return -1 # 원하는 값 x를 찾지 못했을 때 return -1

