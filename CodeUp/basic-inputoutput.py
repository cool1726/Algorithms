# 6009
a = input()
print(a)

# 6010
n = int(input())
print(n)

# 6011
f = float(input())
print(f)

# 6012
a = input()
b = input()
print(a)
print(b)

# 6013
a = input()
b = input()
print(b)
print(a)

# 6014
f = float(input())
print(f) 
print(f) 
print(f) 

# 6015
a, b = input().split()
print(a)
print(b)

# 6016
c1, c2 = input().split()
print(c2, c1)

# 6017
s = input()
print(s, s, s)

# 6018
h, t = input().split(':')
print(h, t, sep=":")

# 6019
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 6020
c1, c2 = input().split('-')
print(c1, c2, sep='')

# 6021
s = input()
for i in s:
    print(i)

# 6022
s = input()
print(s[0:2], s[2:4], s[4:6])

# 6023
h, m, s = input().split(':')
print(m)

# 6024
w1, w2 = input().split()
s = w1 + w2
print(s)

# 6025
a, b = input().split()
c = int(a) + int(b)
print(c)

# 6026
x = float(input())
y = float(input())
print(x + y)

# 6027
a = int(input())
print('%x' % a)

# 6028
a = int(input())
print('%X' % a)

# 6029
a = int(input(), 16) # 입력된 수를 16진수로 인식해 변수 a에 저장
print('%o' % a)

# 6030
n = ord(input()) # 입력받은 문자를 10진수 유니코드 값으로 변환 (아스키)
print(n)

# 6031
# chr() 정수값 -> 문자(유니코드)
# ord() 문자 -> 정수값(아스키)
c = int(input())
print(chr(c)) # 정수 c를 유니코드 문자(character)로 변환
