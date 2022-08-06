#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Queue #Silver3 #PriorityQueue
# https://www.acmicpc.net/problem/1966
#------------------------

# https://hongcoding.tistory.com/42
def main():
    from collections import deque
    T = int(input())
    for test_case in range(T):
        N, M = map(int, input().split())
        priority = deque(list(map(int, input().split())))
        idx = 0
        while priority:
            maximum = max(priority)
            q = priority.popleft()
            M -= 1
            
            if maximum == q:
                idx += 1
                if M < 0:
                    print(idx)
                    break
            else:
                priority.append(maximum)
                if M < 0:
                    M = len(priority)-1
if __name__ == '__main__':
    main()
        
