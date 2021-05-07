# 스킬트리
# Level 2
# skill을 기준으로 pointer 변수를 사용해 skills 문자열 내 순서를 확인함 (포인터를 쓸 수 밖에 없는 이유)
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        pointer = -1
        for a in range(0, len(skill)):
            if skill[a] not in skills: pointer = 30
            else: 
                if pointer < skills.index(skill[a]): pointer = skills.index(skill[a])
                else: 
                    answer -= 1
                    break
        else:
            answer += 1

    return answer

# skills를 기준으로 skill의 문자가 순서대로 존재하는지 확인 (for-else)
def solution2(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1