#------------------------
# #BinarySearch #ParametricSearch #pypy3
# https://www.acmicpc.net/problem/2805
#------------------------

if __name__ == '__main__':
    N, M = map(int, input().split())
    trees = list(map(int,input().split()))

    st, ed = 1, max(trees)
    while True:
        if st > ed:
            print(ed)
            break
        cnt = 0
        mid = (st + ed) // 2
        for t in trees:
            cnt += max(t-mid, 0)
        if cnt < M:
            ed = mid - 1
        else:
            st = mid + 1

