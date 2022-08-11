#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Recursion #Bronze5
# https://www.acmicpc.net/problem/10872
#------------------------

def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)
    
def main():
    n = int(input())
    print(factorial(n))
    
if __name__ == '__main__':
    main()