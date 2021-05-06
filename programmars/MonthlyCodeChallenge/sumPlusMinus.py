def solution(absolutes, signs):
    answer = 0
    count = 0
    for num in absolutes:
        if signs[count]: answer += num
        else: answer -= num
        count += 1
    return answer