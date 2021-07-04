'''
Q9 문자열 압축
'''
# solution 1 (프로그래머스 통과)
def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        temp = s
        new = []
        while True:
            #더이상 남은 문자열이 없다면 끝
            if temp[:i] == '':
                break
            block = ''.join(temp[:i])
            if len(temp[:i]) < i:
                new.append(block)
                break
            if len(new) == 0: #첫 문자열단위라면 그냥 넣기
                new.append(1)
                new.append(block)
            elif new[-1] == block: #직전 단위와 동일하다면
                new[-2] += 1
            else: #직전 단위와 다르다면
                new.append(1)
                new.append(block)
            temp = temp[i:]
        for _ in range(new.count(1)):
            new.remove(1)
        answer = min(answer, len(''.join(str(n) for n in new)))
    return answer


# solution 2 (이코테 해설 참고)
def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        prev = s[0:i]
        compressed = ""
        count = 1
        #단위 크기만큼 증가시키며 이전 문자열과 비교 ★★★
        for j in range(i, len(s), i):
            #직전 단위와 동일하다면 압축 횟수 증가 (+1)
            if prev == s[j:j+i]:
                count += 1
            #직전 단위와 다르다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+i] #직전 상태 갱신
                count = 1
        # 남아있는 문자열에 대해 처리
        compressed += str(count) + prev if count >= 2 else prev
        #만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed)) 
    return answer