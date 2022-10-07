https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

"""
5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
"""

T = int(input())
for test_case in range(1,T+1) :
    N = int(input())
    Start = []
    End = []
    start = 0
    result = 0
    for i in range(N):
        s,e = map(int,input().split())
        Start.append(s)
        End.append(e)
    for i in range(N):
        min_end_idx = End.index(min(End))
        if start <= Start[min_end_idx] :
            start = min(End)
            result += 1
        del End[min_end_idx]
        del Start[min_end_idx]
    print("#%d %d" % (test_case,result))
           
            
