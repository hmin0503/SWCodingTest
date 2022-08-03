#!/home/hmin/anaconda3/envs/tensor-gpu/bin/python3.8
#------------------------
# #Set #Map #Hash
# https://www.acmicpc.net/problem/11478
#------------------------

def main():
    string = input()
    answer = []
    for i in range(1, len(string)+1):
        for j in range(len(string)+1-i):
            answer.append(string[j:j+i])
    print(len(set(answer)))
if __name__ == '__main__':
    main()