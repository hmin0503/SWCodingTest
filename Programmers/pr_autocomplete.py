# 맨 처음 작성한 코드 --> 시간 초과로 계속 실패

def solution(words):
    answer = 0
    eng_dict = {}
    for word in words:
        for i in range(len(word)):
            if word[:(i+1)] in eng_dict.keys():
                eng_dict[word[:(i+1)]] += 1
            else:
                eng_dict[word[:(i+1)]] = 1

    for word in words:
        for i in range(len(word)):
            if eng_dict[word[:(i+1)]] != 1:
                answer += 1
            else :
                answer += 1
                break
    return answer
 

# 구글링을 해보니
# Trie 구조를 활용해서 풀면 쉽다고 한다.
# http://tedware.kr/posts/487
