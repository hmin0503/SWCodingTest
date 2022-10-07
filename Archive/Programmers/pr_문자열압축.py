# 이 문제는 처음에 1개 단위부터 봐도 될까 생각했는데, 그래도 됐었다. 
# 생각한 내용은 동일한데 이를 어떻게 코드로 구현하는지가 틀려서 못 풀었다.
def solution(s):
    answer = len(s)
# 1개 단위부터 하나씩 늘려가면서 가장 짧은 길이의 문자 찾아가기.
for i in range(1, len(s)//2 + 1):
        # 압축된 문자열 저장
        compressed = ""
        # 연속으로 등장한 횟수
        c = 1
        # 맨 처음 비교할 문자열
        prev = s[:i]
        # 문자열 처음부터 비교해가기
        for j in range(i, len(s), i):
            post = s[j:(j+i)]
            if prev == post:
                c += 1
            else :
                compressed += str(c) + prev if c >= 2 else prev
                c = 1
                prev = post
        # 마지막으로 남은 것 더해주기
    	compressed += str(c) + prev if c >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
