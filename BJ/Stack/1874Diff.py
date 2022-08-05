#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Stack #Silver2
# https://www.acmicpc.net/problem/1874
#------------------------

def main():
    N = int(input())
    idx = 1
    stack = []
    cmt = []
    flag = 1
    for i in range(1, N+1):
        n = int(input())
        while idx <= n:
            stack.append(idx)
            idx += 1
            cmt.append("+")
        if stack[-1] == n:
            stack.pop()
            cmt.append("-")
        else:
            print("NO")
            return
    print(*cmt, sep = "\n")
            

if __name__ == '__main__':
    main()