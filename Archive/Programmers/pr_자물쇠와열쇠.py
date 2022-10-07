def expandMatrix(lock):
    n = len(lock)
    new_n = 3 * n - 2
    lock = [[0] * n] * (n - 1) + lock + [[0] * n] * (n - 1)
    lock = [[0] * (n - 1) + l + [0] * (n - 1) for l in lock]
    return lock

def squeezeMatrix(lock):
    new_n = len(lock)
    n = (new_n + 2) // 3
    lock = [l[(n - 1):(2 * n - 1)] for l in lock]
    lock = lock[(n - 1):(2 * n - 1)]
    return lock

def rotate90(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result

def solution(key, lock):
    # 혹시 자물쇠 없이도 열리는 경우
    lock_cp = sum(lock,[])
    if min(lock_cp) == 1 & max(lock_cp) == 1:
        return True
    
    n = len(lock)
    m = len(key)
    
    new_lock = expandMatrix(lock)
    for _ in range(4):
        key = rotate90(key)
        for x in range(2 * n - 1):
            for y in range(2 * n - 1):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                lockWithKey = sum(squeezeMatrix(new_lock), [])
                if min(lockWithKey) == 1 & max(lockWithKey) ==  1 :
                    return True
                new_lock = expandMatrix(lock)
    return False
