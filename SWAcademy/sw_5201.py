https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


"""
5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
"""

T = int(input())
for test_case in range(1,T+1):
    result = 0
    N,M = map(int,input().split())
    Weight = list(map(int,input().split()))
    Weight.sort(reverse = True)
    Truck = list(map(int,input().split()))
    Truck.sort(reverse = True)
    for i in Truck:
        for j in range(len(Weight)) :
            if i >= Weight[j] :
                result += Weight[j]
                del Weight[j]
                break
    print("#%d %d" % (test_case,result))
