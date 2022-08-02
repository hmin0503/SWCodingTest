#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Sort # Counting sort
# https://www.acmicpc.net/problem/2108
#------------------------
def solution():
    import sys
    N = int(input())
    lst = {k:0 for k in range(-4001, 4001)}
    nums = []
    for _ in range(N):
        n = int(sys.stdin.readline())
        lst[n] += 1
        nums.append(n)
    
    nums = sorted(nums)
    lst = sorted(lst.items(), key = lambda x : x[1], reverse = True)
    # 1.산술평균
    print(round(sum(nums)/N)) # -0.3 을 반올림 할 때, 자리수를 지정해주면 음수가 나온다.
    # 2. 중앙값
    print(nums[len(nums)//2])
    # 3. 최빈값
    if lst[0][1] != lst[1][1]:
        print(lst[0][0])
    else:
        print(lst[1][0])
    # 4. 범위
    print(max(nums) - min(nums))
        
if __name__ == '__main__':
    solution()