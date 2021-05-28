'''
무지의 먹방 라이브
'''

# solution 4 (mine)
# 우선순위 큐(최소힙) 이용한 방법
# 모든 음식을 우선순위 큐에 (음식 시간, 음식 번호) 형태로 삽입한다
# k 값에서 먹은 시간을 빼는 방법
import heapq

def solution(food_times, k):
    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    #시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    n = len(food_times)
    for i in range(n):
        heapq.heappush(q, (food_times[i], i + 1)) #(음식시간, 음식번호) 형태로 삽입
        
    #사이클 돌면서 k에서 (사이클길이(len) * 최소음식시간)을 빼준다
    previous = 0 #직전에 다 먹은 음식 시간
    while (q[0][0] - previous) * n <= k:
        k -= (q[0][0] - previous) * n
        previous = heapq.heappop(q)[0]
        n -= 1
    q.sort(key=lambda x: x[1]) #음식번호 기준 정렬
    answer = q[k % n][1]
    return answer
        

# solution 3 (이코테)
# k값을 바꾸지 않고 sum_value를 활용
import heapq

def solution(food_times, k):
    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    #시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    n = len(food_times)
    for i in range(n):
        heapq.heappush(q, (food_times[i], i + 1)) #(음식시간, 음식번호) 형태로 삽입
    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간
    length = len(food_times) #남은 음식 개수
    
    #(sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수)와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 #다 먹은 음식 제외
        previous = now #이전 음식 시간 재설정
    
    #남은 음식 중에서 몇 번째 음식인지 확인해 출력
    answer = sorted(q, key=lambda x: x[1]) #음식번호 기준 정렬
    return answer[(k - sum_value) % length][1]
    

'''
def solution(food_times, k):
    cycle = k // len(food_times)
    target = k % len(food_times)
    r = 0
    for index, food in enumerate(food_times):
        temp = 0
        if index < target:
            temp = 1
        # 일찍 빈 접시가 된 케이스 카운트
        if food < (cycle + temp):
            r += (cycle + temp - food)
        food_times[index] -= (cycle + temp)
        
    k = 0
    p = 0
    for i in range(r):
        while True:
            # 마지막 N번 -> 1번으로 회전
            if p >= len(food_times) - 1:
                p = 0
            # 일반 K번 -> K+1번으로
            else:
                p += 1
            if food_times[p]:
                    break
            k += 1
            if k == r:
                return -1
    return p
    
    
def solution(food_times, k):
    p = 0
    for i in range(k):
        food_times[p] -= 1
        
        k = 0
        # 빈 접시라면 다음 접시로 넘어가기
        while True:
            # 마지막 N번 -> 1번으로 회전
            if p >= len(food_times) - 1:
                p = 0
            # 일반 K번 -> K+1번으로
            else:
                p += 1
            if food_times[p]:
                break
            k += 1
            if k == len(food_times):
                return -1
    return p + 1
'''