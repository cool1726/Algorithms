# 점프와 순간 이동
# Level 2

# 나눴을 때 홀수가 나오면 (+나머지), 짝수가 나오면 킵고잉
def solution(n):
    ans = 0

    while n > 0:
        ans += n % 2
        n = n // 2

    return ans

# 2진법 사용하기
def solution2(n):
    return bin(n).count('1')