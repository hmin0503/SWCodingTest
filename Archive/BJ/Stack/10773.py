#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Stack #Silver4
# https://www.acmicpc.net/problem/10773
#------------------------

def main():
    import sys
    N = int(input())
    stack = []
    for _ in range(N):
        # n = int(sys.stdin.readline().rstrip())
        n = int(input())
        if n == 0:
            stack.pop()
        else:
            stack.append(n)
    print(sum(stack))
        
if __name__ == '__main__':
    main()