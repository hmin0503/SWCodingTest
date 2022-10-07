#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Recursion #Bronze2
# https://www.acmicpc.net/problem/10870
#------------------------
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1)+fibo(n-2)

def main():
    n = int(input())
    print(fibo(n))

    
if __name__ == '__main__':
    main()