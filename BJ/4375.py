#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Math
# https://www.acmicpc.net/problem/4375
#------------------------

def solution():
    # 테스트케이스 개수가 주어지지 않음.
    while True:
        try:
            n = int(input())
            i = 0
            x = 0
            while True:
                x += 10**i
                if x % n == 0:
                    break
                i += 1
            print(len(str(x)))
        except :
            return
if __name__ == '__main__':
    solution()
