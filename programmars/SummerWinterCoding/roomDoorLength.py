def solution(dirs):
    answer = 0
    dx = {'U':0, 'D':0, 'R':1, 'L':-1}
    dy = {'U':1, 'D':-1, 'R':0, 'L':0}
    prev = (0, 0)
    l = set()
    for d in dirs:
        _x, _y = prev
        x = _x + dx[d]
        y = _y + dy[d]
        
        if abs(x) <= 5 and abs(y) <= 5:
            r = tuple(sorted([(_x, _y), (x, y)]))
            l.add(r)
            prev = (x, y)
    answer = len(l)
    return answer