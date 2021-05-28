'''
문자열 뒤집기
'''

binarystr = str(input())
answer = 1
for i in range(1, len(binarystr)):
    if binarystr[i-1] != binarystr[i]:
        answer += 1
print(answer // 2)