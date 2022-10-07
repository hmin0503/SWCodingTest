#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Recursion #Gold5
# https://www.acmicpc.net/problem/2447
#------------------------

def get_star(n, base):
    if n == 1:
        return base
    stars = []
    # 3등분에서 첫째줄 그리기
    for b in base:
        stars.append(b*3)
    # 3등분에서 두번째줄 그리기
    for b in base:
        stars.append(b+" "*len(base)+b)
    # 3등분에서 세번째줄 그리기
    for b in base:
        stars.append(b*3)
    return get_star(n//3, stars)
 
def main():
    n = int(input())
    stars = get_star(n,"*")
    for s in stars:
        print(s)

if __name__ == '__main__':
    main()