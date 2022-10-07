#%%
#------------------------
# #DP #Bag #Kanpsack
#------------------------
def main():
    N, K = map(int, input().split())
    weights = []
    values = []
    for _ in range(N):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)
    bag = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1,K+1):
            w, v = weights[i-1], values[i-1]
            if j < w:
                bag[i][j] = bag[i-1][j]
            else:
                bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)
    print(bag[N][K])
if __name__ == '__main__':
    main()

# %%
