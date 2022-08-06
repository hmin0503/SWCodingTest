#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Queue #Silver4 #Queue인걸 문제만 보고 어떻게 파악하지.
# https://www.acmicpc.net/problem/5430
#------------------------

def main():
    from collections import deque
    T = int(input())
    for test_case in range(T):
        p = deque(list(input().rstrip()))
        n = int(input())
        seq = deque(map(str, eval(input().rstrip())))
        reverse = 1
        
        if "D" in p and p.count("D") > n:
            print("error")
        else:
            while p:
                q = p.popleft()
                if q == "R":
                    reverse *= -1  

                elif q == "D" :
                    if reverse == -1:
                        seq.pop()
                    else:
                        seq.popleft()
                        
            if reverse == -1:
                print("["+",".join(list(seq)[::-1])+"]") # 출력 부분 신경쓰기, 반례 잘 찾기
            else:
                print("["+",".join(list(seq))+"]")
                    
if __name__ == '__main__':
    main()
        
