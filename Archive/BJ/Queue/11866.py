#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Queue #Silver5 #Queue인걸 문제만 보고 어떻게 파악하지.
# https://www.acmicpc.net/problem/11866
#------------------------

def main():
    from collections import deque
    N, K = map(int, input().split())
    cards = deque([i for i in range(1, N+1)])
    print("<", end="")
    
    # 카드가 한장 남을 때까지 반복.
    while len(cards) > 1:
        # 먼저 K-1번째 사람까지 leftpop을 해주고, append를 함으로써 가장 아래로 보냄.
        for _ in range(K-1):
            n = cards.popleft()
            cards.append(n)
        # K번째 사람 leftpop
        print(cards.popleft(), end=", ")
    print(cards[0], end ="")
    print(">")
if __name__ == '__main__':
    main()
        
