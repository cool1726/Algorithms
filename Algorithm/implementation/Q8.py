'''
Q8 문자열 재정렬
'''
data = input()
alphabet, num = [], []
for d in data:
    if ord(d) >= ord('A') and ord(d) <= ord('Z'):
        alphabet.append(d)
    else:
        num.append(int(d))
# 리스트 원소를 문자열로 바꾸는 함수 
# ''.join(listA + listB)
print(''.join(sorted(alphabet) + list(str(sum(num)))))
