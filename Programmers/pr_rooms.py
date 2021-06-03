from collections  import deque

def solution(arrows):
    answer = 0
    # 각 방향별로 움직이는 좌표 저장
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    
    visited = dict()
    visited_dir = dict()
    
    # 현재 위치
    current = (0,0)
    
    # 이동한 경로 큐에 저장.    
    queue = deque()
    queue.append(current)

    for arrow in arrows:
        # X 자로 가로 지르는 경우를 파악하기 위해서 한번에 두 칸씩 이동
        for _ in range(2):
            x = current[0] + dx[arrow]
            y = current[1] + dy[arrow]
            
            # 경로 큐에 저장
            queue.append((x,y))

            # 경로 체크를 위한 dict 생성하기
            visited[(x, y)] = 0
            visited_dir[(current, (x, y))] = 0
            
            # 현재 위치 업데이트
            current = (x, y)
    current = queue.popleft()
    visited[current] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if (visited[(x, y)] == 1) and (visited_dir[(current, (x, y))]) == 0:
            answer += 1
        else :
            visited[(x, y)] = 1
        
        visited_dir[(current, (x, y))] = 1
        visited_dir[((x, y), current)] = 1
        current = (x, y)
    
    return answer
