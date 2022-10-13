#------------------------
# #BinarySearch #LongestIncreasingSubsequence
# https://www.acmicpc.net/problem/12015
#------------------------
import bisect 
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    lis = []
    cnt = 0
    for n in A:
        if len(lis) == 0:
            lis.append(n)
            cnt += 1
            continue
        
        if lis[-1] < n:
            lis.append(n)
            cnt += 1
            print("lis<n",lis)
        else:
            idx = bisect.bisect_left(lis, n)
            lis[idx] = n
            print("else",lis)
    print(cnt)
    print(lis)
