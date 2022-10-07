def main():
    N = int(input())
    for n in range(N):
        num = n + sum(list(map(int, str(n))))
        if num == N:
            return n
    return 0
print(main())