# 6032
n = int(input())
print(-n)

# 6033
n = ord(input())
print(chr(n+1))

6034
a, b = input().split()
c = int(a) - int(b)
print(c)

# 6035
f1, f2 = input().split()
c = float(f1) * float(f2)
print(c)

# 6036
w, n = input().split()
print(w * int(n))

#6037
n = int(input())
s = input()
print(n * s)

# 6038
a, b = input().split()
c = int(a) ** int(b)
print(c)

# 6039
f1, f2 = input().split()
c = float(f1) ** float(f2)
print(c)

# 6040
a, b = input().split()
print(int(a) // int(b))

# 6041
a, b = input().split()
print(int(a) % int(b))

# 6042
# 소수점 아래 3번째 자리에서 반올림한 값
f = float(input())
print(format(f, ".2f"))

# 6043
f1, f2 = input().split()
f1, f2 = float(f1), float(f2)
print(format(f1 / f2, ".3f"))

# 6044
a, b = input().split()
a, b = int(a), int(b)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))

# 6045
a, b, c = input().split()
s = int(a) + int(b) + int(c)
m = float(s) / 3
print(s, format(m, ".2f"))

# 6046
# 2배 곱해 출력하기
n = int(input())
print(n << 1)

# 6047
x, y = input().split()
print(int(x) << int(y))

# 6048
a, b = input().split()
print(int(a) < int(b))

# 6049
a, b = input().split()
print(int(a) == int(b))

# 6050
a, b = input().split()
print(int(b) >= int(a))

# 6051
a, b = input().split()
print(int(a) != int(b))

# 6052
n = int(input())
print(bool(n))

# 6053
n = bool(int(input()))
print(not n)

# 6054
a, b = input().split()
print(bool(int(a) and bool(int(b))))

# 6055
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 6056
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and not b) or (not a and b))

# 6057
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or (not a and not b))

# 6058
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not a and not b)

# 6059
# bit 단위 0 -> 1, 1 -> 0 연산
n = int(input())
print(~n)

# 6060
# bit 단위 and 연산
a, b = input().split()
print(int(a) & int(b))

# 6061
# bit 단위 or 연산
a, b = input().split()
print(int(a) | int(b))

# 6062
# bit 단위 xor 연산
a, b = input().split()
print(int(a) ^ int(b))

# 6063
# 3항 연산: x if C else y
a, b = input().split()
a = int(a)
b = int(b)
c = a if (a >= b) else b
print(c)

# 6064
# 3항 연산 (세 정수 중 가장 작은 값 출력)
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
print((a if a < b else b) if (a if a < b else b) < c else c)
