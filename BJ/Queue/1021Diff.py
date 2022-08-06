#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Queue #Silver4 #Queue인걸 문제만 보고 어떻게 파악하지.
# https://www.acmicpc.net/problem/1021
# https://velog.io/@goplanit/Algorithm-%EB%B0%B1%EC%A4%80-1021%EB%B2%88-%ED%9A%8C%EC%A0%84%ED%95%98%EB%8A%94-%ED%81%90%ED%8C%8C%EC%9D%B4%EC%8D%AC
#------------------------

def main():
    from collections import deque
    
    N, M = map(int, input().split())
    targets = deque(list(map(int, input().split())))
    
    queue = deque([i for i in range(1, N + 1)])
    cnt = 0
    for t in targets:
        while True:
            if queue[0] == t:
                queue.popleft()
                break
            else :
                # 현재 뽑고자 하는 수의 위치를 먼저 파악하는 것이 핵심.
                if queue.index(t) < len(queue)/2: # 뽑고자 하는 수의 위치가 중간 기준 왼쪽.
                    while queue[0] != t:
                        queue.append(queue.popleft())
                        cnt += 1
                else:  # 뽑고자 하는 수의 위치가 중간 기준 오른쪽쪽.
                    while queue[0] != t:
                        queue.appendleft(queue.pop())
                        cnt += 1
    print(cnt)
              
if __name__ == '__main__':
    main()
        
