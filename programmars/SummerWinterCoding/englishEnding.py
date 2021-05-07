# 영어 끝말잇기
# Level 2

def solution(n, words):
    answer = []
    passed = []
    
    for idx, word in enumerate(words):
        if word in passed or len(word) < 2:
            answer.append(idx % n + 1)
            answer.append(idx // n + 1)
            return answer
        elif idx > 0 and word[0] != words[idx - 1][-1]:
            answer.append(idx % n + 1)
            answer.append(idx // n + 1)
            return answer
        passed.append(word)
    return [0, 0]


def solution2(n, words):
    for p in range(1, len(words)):
    if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
        return [p % n + 1, p // n + 1]
    return [0, 0]


def main():
    n = 3
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    solution(n, words)


if __name__ == "__main__":
    main()