#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Stack #Silver4
# https://www.acmicpc.net/problem/10828
#------------------------

def main():
    import sys
    N = int(input())
    stack = []
    for _ in range(N):
        cmt = sys.stdin.readline().rstrip() #시간 초과 해결
        if " " in cmt:
            cmt, v = cmt.split()
            
        if cmt == "push":
            stack.append(v)
        elif cmt == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif cmt == "size":
            print(len(stack))
        elif cmt == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif cmt == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        
        
if __name__ == '__main__':
    main()