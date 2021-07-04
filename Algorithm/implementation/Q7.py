'''
Q7 럭키 스트레이트
'''
n = input()
leftsum, rightsum = 0, 0
for i in range(len(n)//2):
    leftsum += int(n[i])
    rightsum += int(n[-(i+1)])
if leftsum == rightsum:
    print("LUCKY")
else:
    print("READY")