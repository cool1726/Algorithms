n = int(input())
numbers = list(map(int, input().split()))

answer = [0 for _ in range(n)]

# n개의 정수로 이루어진 수열 numlist는 연속된 최대 n개의 수를 더할 수 있다
for i in range(n):
    answer[i] = max(numbers[i], answer[i - 1] + numbers[i])

print(max(answer))
