
S = int(input())
nums = list(map(int, input().split()))
mem = [0]*(sum(nums)+2)

def dfs(lst, st):
    global mem
    total = sum([nums[idx] for idx in lst])
    mem[total] = 1
    for i in range(st, len(nums)):
        if i not in lst:
            lst.append(i)
            dfs(lst, i+1)
            lst.pop()

dfs([], 0)
print(mem.index(0))


# short coding
#------------------
# N=int(input())
# L=sorted(list(map(int,input().split())))
# num=1
# for i in L:
#     if num<i:
#         break
#     num+=i
#     print(i, num)
# print(num)
