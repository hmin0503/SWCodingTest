#------------------------
# #BinarySearch #ParametricSearch
# https://www.acmicpc.net/problem/1300
#------------------------

if __name__ == '__main__':
    N = int(input())
    k = int(input())
    st, ed = 0, N*N
    
    # 틀린 이유: 범위 주의
    while st <= ed:
        cnt = 0
        mid = (st+ed)//2
        for r in range(1, N+1):
            cnt += min(mid//r, N)
        if cnt < k:
            st = mid + 1
        else:
            ed = mid - 1
    print(st)
