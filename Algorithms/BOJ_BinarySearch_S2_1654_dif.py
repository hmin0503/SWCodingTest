#------------------------
# #BinarySearch #ParametricSearch
# https://www.acmicpc.net/problem/1654
#------------------------

if __name__ == '__main__':
    K, N = map(int, input().split())
    lines = [int(input()) for _ in range(K)]
    st, ed = 1, max(lines)
    while st <= ed:
        mid = (st+ed) // 2
        cnt = 0
        for l in lines:
            cnt += l // mid
        # 중간 값을 기준으로 좁혀 가면서 값을 찾음.
        if cnt < N:
            ed = mid - 1
        else:
            st = mid + 1
    print(ed)