import itertools as it

def solution(nums):
    answer = 0;
    npr = list(it.combinations(nums, 3))

    sum = 0
    for i in npr:
        sum = i[0] + i[1] + i[2]
        if(isPrime(sum)): answer += 1
    return answer

def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

nums = [1, 2, 3, 4]
solution(nums)