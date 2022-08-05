#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Stack #Gold4
# https://www.acmicpc.net/problem/17298
#------------------------

def main(): #시간초과
    N = int(input())
    seq = list(map(int,input().split()))
    answer = [-1]*(N+1)
    stack = []
    for idx in range(N, 0, -1):
        n = seq.pop()
        if stack:
            for i in range(len(stack)-1, -1, -1):
                if stack[i] > n:
                    answer[idx] = stack[i]
                    break
        stack.append(n)
    print(*answer[1:])
    

"""
https://hongcoding.tistory.com/40
"""
def main():
    N = int(input())
    seq = list(map(int,input().split()))
    answer = [-1]*N
    stack = [0] # index 0 부터 push
    for i in range(1, N):
        # index 1과 stack[-1] 값을 비교해 index 1의 값이 클 경우 stack[-1]를 pop하고 stack[-1] 정답을 index 1의 값으로 업데이트.
        # index 1 의 값이 stack[-1] 값 보다 작을 경우 stack에 index 1 push.
        # index 2 의 값이 stack[-1] 값 보다 작을 경우 stack에 index 2 push.
        # index 3의 값이 stack[-1]의 값보다 클 경우, stack[-1]를 pop 하고 stack[-1] 정답을 index 3 의 값으로 업데이트. -> index 3의 값이 stack[-1]의 값 보다 작을 때 까지 반복.
        while stack and seq[stack[-1]] < seq[i]:
            answer[stack.pop()] = seq[i]
        stack.append(i)
        
    
    print(*answer)
if __name__ == '__main__':
    main()