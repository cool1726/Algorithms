# 예산
# Level 1

# 정렬

def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in d:
        sum += i
        if sum > budget: 
            break
        elif sum == budget:
            answer += 1
            break
        else: 
            answer += 1
    
    return answer