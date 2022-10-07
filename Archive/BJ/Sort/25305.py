#------------------------
# #Sort #Bronze2
# https://www.acmicpc.net/problem/25305
#------------------------

def main():
    N, k = map(int, input().split())
    x = list(map(int, input().split()))
    x = sorted(x)
    print(x[-k])
    
if __name__ == '__main__':
    main()
            
            
        
        
    