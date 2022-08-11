#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Queue #Silver4 #Queue인걸 문제만 보고 어떻게 파악하지.
# https://www.acmicpc.net/problem/2164
#------------------------

# def main():
#     N = int(input())
#     cards = [i for i in range(N, 0, -1)]
#     while len(cards) > 1:
#         cards.pop() # list.pop()은 O(1)이므로 카드를 거꾸로 담아 deque 없이 풀어보기. -> 시간초과
#         cards = [cards[-1]]+cards[:-1] # + returns the result of the expression as a new value. And list.insert(value, loc): O(N), while list.append(value): O(1)
#     print(cards[0])

def main():
    from collections import deque
    N = int(input())
    cards = deque([i for i in range(1, N+1)])
    while len(cards) > 1:
        cards.popleft()
        t = cards.popleft()
        cards.append(t)
    print(cards[0])
    
if __name__ == '__main__':
    main()
        
