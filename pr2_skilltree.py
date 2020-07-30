'''
https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3#fnref1
'''
#%%
def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        skills = [999]*len(skill)
        sk = list(sk)
        for i in range(len(skills)):
            try:
                skills[i] = sk.index(skill[i])
            except ValueError:
                continue
        if skills == sorted(skills):
            answer+=1
    return answer
###
solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])
