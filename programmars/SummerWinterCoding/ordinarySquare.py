def solution(w,h):
    if w == h:
        return w * h - w
    elif w == 1 or h == 1:
        return 0
    else:
        answer = 0
        p = gcd(w, h)
        ww = w // p
        hh = h // p
        l = hh / ww
        for i in range(0, ww):
            answer += int(i * l)
        return w * h - (p * (ww*hh - answer*2))

# 규칙을 찾자!
# 최대공약수 접근은 좋았는데.. 너비, 높이 각각 입장에서 대각선이 지나는 걸 하나씩 빼고 겹치는걸 더해준다
# 겹치는 부분이 바로 gcd(w, h) => 최대공약수 횟수만큼 겹치기 때문
def solution2(w,h):
    return w * h - w - h + gcd(w, h)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
