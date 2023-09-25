def push(queue, n):
    queue.append(n)
    return queue

def pop(queue):
    if queue:
        top = queue[0]
        queue = queue[1:]
        print(top)
    else:
        print(-1)
def size(queue):
    print(len(queue))

def empty(queue):
    if queue:
        print(0)
    else:
        print(1)

def front(queue):
    if queue:
        top = queue[0]
        print(top)
    else:
        print(-1)

def back(queue):
    if queue:
        back = queue[-1]
        print(back)
    else:
        print(-1)

N = int(input())
queue = []
for _ in range(N):
    c = input()
    if "push" in c:
        n = c.split()[-1]
        queue = push(queue,int(n))

    if 'front' in c:
        front(queue)
    
    if 'back' in c:
        back(queue)

    if 'size' in c:
        size(queue)
    
    if 'pop' in c:
        pop(queue)
    
    if 'empty' in c:
        empty(queue)
