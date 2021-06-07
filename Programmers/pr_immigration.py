"""
https://wwlee94.github.io/category/algorithm/binary-search/immigration/
이분 블로그를 보고 문제를 이해했다.
 

문제 해결 방법 초점을 "사람"이 아니라 "시간"에 두는 것이 요점이다.
먼저 정답이 될만한 시간 범위를 구한다.
여기서는 [1, max(times) * (n + 1)] 를 시간 범위로 정한다.

이후부터 중앙값을 찾아 중앙값을 answer라고 예상했을 때,
answer 시간 내에 입국심사 처리가 가능한가? 
를 확인하는 부분이 while 문 이다.
만약, 주어진 입국 심사 내에 처리가 가능하다면, 시간 범위를 줄여준다. 
즉, 중앙값이 작아진다. (right 값을 mid - 1)

그러나 만약 주어진 입국 심사 내에 처리가 불가능 하면, 시간 범위를 늘여준다.
즉, 중앙값이 커진다. (left 값을 mid + 1)

이렇게 하다 보면 결국 시간 범위는 점점 줄어들게 되어, left가 right 값보다 같거나 커지는 지점이 생기는데,
그 값이 결국 정답이다.
"""

def solution(n, times):
    answer = 0
    
    left = 1
    right = (n + 1) * max(times)
    
    while left <= right:
        mid = (left + right) // 2
        
        count = 0
        for time in times:
            count += mid // time
            if count >= n :
                break
        
        if count >= n:
            answer = mid
            right = mid - 1
        
        elif count < n:
            left = mid + 1
    return answer
