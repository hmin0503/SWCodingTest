#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Queue #Silver4 
# https://www.acmicpc.net/problem/10866
#------------------------

def main():
    import sys
    from collections import deque
    N = int(input())
    queue = deque([]) #시간 초과 해결
    
    for _ in range(N):
        cmt = sys.stdin.readline().rstrip() #시간 초과 해결
        
        if " " in cmt:
            cmt, v = cmt.split()
            
        if cmt == "push_front":
            queue.appendleft(v) # queue 앞에 삽입
            
        elif cmt == "push_back":
            queue.append(v) # queue 뒤에 삽입
            
        elif cmt == "pop_front":
            if queue:
                print(queue.popleft()) # queue 앞에 출력 및 삭제
            else:
                print(-1)
        elif cmt == "pop_back":
            if queue:
                print(queue.pop()) # queue 뒤에 출력 및 삭제
            else:
                print(-1)
        elif cmt == "size":
            print(len(queue))
            
        elif cmt == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif cmt == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif cmt == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
        
        
if __name__ == '__main__':
    main()