def main():
    answer = 0
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                case = nums[i]+nums[j]+nums[k]
                if case <= M:
                    if case > answer:
                        answer = case
    print(answer)
                