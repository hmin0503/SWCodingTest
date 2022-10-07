'''
triple step 
어떤 아이가 n개의 계단을 오른다. 
한 번에 1계단 오르기도 하고, 2계단이나 3계단을 오르기도 한다. 
계단을 오르는 방법이 몇 가지나 있는지 계산하는 메서드를 구하라.
'''

# Brute force
def solution1(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return solution1(n-1) + solution1(n-2) + solution1(n-3)
    

# memoiztion
def solution2(n):
    if n == 0:
        return 1
    else:
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]

if __name__ == '__main__':
    n = int(input())
    print(solution1(n))
    
    memo = [1]*(n+1)
    print(solution2(n))
    