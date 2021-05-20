#########################################################################
"""
5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
"""
#########################################################################

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    matrix = []
    N = int(input())
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
	
    # Column을 기준으로 최소비용 계산하기
    for i in range(N):
        for j in range(N):
			# 시작점은 움직이지 않으니 아무것도 하지 않음.
            if i == j == 0 :
                continue
            # 첫번째 Column인 경우에는 위에서만 내려올 수 있기 때문에 위의 값을 더해줌.
            if i == 0 and j > 0 :
               	matrix[j][i] += matrix[j - 1][i]
            # 첫번째 Row인 경우에는 왼쪽에서만 올 수 있기 때문에 왼쪽의 값을 더해줌.
            elif j == 0 and i > 0 :
                matrix[j][i] += matrix[j][i - 1]
            # 위의 두 경우도 아닐땐 왼쪽과 위쪽 값 중 최소값을 더해줌.
            elif i > 0 and j > 0 :
                matrix[j][i] += min(matrix[j - 1][i], matrix[j][i - 1])
                
    print("#{} {}".format(test_case, matrix[N-1][N-1]))
