'''
https://programmers.co.kr/learn/courses/30/lessons/62049
'''
#%%
def solution(n):
    answer = [0]
    if n == 1 :
        return answer
    else :
        for _ in range(n-1):
            answer = answer + [0] + [1-x for x in reversed(answer)]
        return answer
solution(1)
#%%
solution(2)
#%%
solution(3)
# %%
