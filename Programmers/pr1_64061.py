'''
https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
memo : 왜 틀렸다고 나오지?
'''
#%%
def solution(board, moves):
    answer = 0
    board = [list(x) for x in zip(*board)]
    stack = []
    while moves :
        m = moves.pop(0) - 1
        while board[m]:
            q = board[m].pop(0)
            if q != 0 :
                break
        stack.append(q) 
        if (len(stack)>1) :
            if stack[-1] == stack[-2]:
                del stack[-2:]
                answer += 1
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])

# %%
