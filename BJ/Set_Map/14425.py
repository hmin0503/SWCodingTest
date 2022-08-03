#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Set #Map #Hash
# https://www.acmicpc.net/problem/14425
#------------------------

def main():
    answer = 0
    N, M = map(int, input().split())
    # set은 dictionary와 같이 hash table 구조를 사용한다. 
    # set은 dictionary에서 key만 있는 구조.
    s = set([input() for _ in range(N)])
    
    for _ in range(M):
        if input() in s:
            answer += 1
    
    return answer

if __name__ == '__main__':
    print(main())