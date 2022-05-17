import sys
sys.stdin = open("input.txt", "r")

# 중위 순회
def inorder(idx):
    if idx > N or idx == 0:
        return
    else:
        if (len(ans) >= 3) and (ans[-1] in ["+","-","*","/"]):
            c = ans.pop()
            b = ans.pop()
            a = ans.pop()
            if b == "+":
                ans.append(float(a) + float(c))
            elif b == "*":
                ans.append(float(a) * float(c))
            elif b == "-":
                ans.append(float(a) - float(c))
            elif b == "/":
                ans.append(float(a) / float(c))
        inorder(left[idx])
        ans.append(root[idx])
        inorder(right[idx])



def postorder(idx):
    if idx > N or idx == 0:
        return
    else:
        # if left node exists
        postorder(left[idx])
        # if right node exists
        postorder(right[idx])
        # append node value to ans
        ans.append(root[idx])
        if (ans[-1] in ["+","-","*","/"]) and (len(ans) >= 3):
            c = ans.pop()
            b = ans.pop()
            a = ans.pop()
            if c == "+":
                ans.append(float(a) + float(b))
            elif c == "*":
                ans.append(float(a) * float(b))
            elif c == "-":
                results = float(a) - float(b)
                ans.append(results)
            elif c == "/":
                results = float(a) / float(b)
                ans.append(results)

T = 10
for test_case in range(1, T+1):

    N = int(input())
    # 이진 트리 중위 순회 
    root = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for _ in range(N):
        leafs = list(input().split())
        if len(leafs) == 4:
            root_idx = int(leafs[0])
            root_val = leafs[1]
            left_idx = int(leafs[2])
            right_idx = int(leafs[3])
            root[root_idx] = root_val
            left[root_idx] = left_idx
            right[root_idx] = right_idx
        else:
            root_idx = int(leafs[0])
            root_val = leafs[1]
            root[root_idx] = root_val
    ans = []
    postorder(1)
    print("#{:d} {:d}".format(test_case, int(ans[-1])))
'''
    icp = {"*" : 2, "/" : 2, "+" : 1, "-":1, "(":0} # in-coming priority
	# 중위 -> 후위표현식
    stack = []
    results = []
    for n in ans:
        if n not in icp and n != ")":
            results.append(n)
        else:
            if not stack :
                stack.append(n)
            elif n == "(":
                stack.append(n)
            elif n == ")":
                while stack and stack[-1] != "(":
                    results.append(stack.pop())
                stack.pop()
            else:
                while stack and icp[n] <= icp[stack[-1]]:
                    results.append(stack.pop())
                stack.append(n)
    while stack:
        results.append(stack.pop())
    stack = []
    for n in results:
        if n not in icp:
            stack.append(int(n))
        else:
            if n == "*":
                post = stack.pop()
                pre = stack.pop()
                stack.append(pre + post)
            elif n == "+":
                post = stack.pop()
                pre = stack.pop()
                stack.append(pre + post)
            elif n == "/":
                post = stack.pop()
                pre = stack.pop()
                stack.append(pre + post)
            elif n == "-":
                post = stack.pop()
                pre = stack.pop()
                stack.append(pre + post)
    print("#{:d} {:d}".format(test_case, stack[-1]))
'''