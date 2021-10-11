def push(stack, num):
    stack.append(num)
    return stack

def pop(stack):
    if len(stack) == 0:
        return False
    else:
        res = stack[len(stack) - 1]
        stack = stack[:len(stack)-1]
        return res, stack

def size(stack):
    return len(stack)

def empty(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0

def top(stack):
    return stack[len(stack) - 1]

n = int(input())
res = []
stack = []

for i in range(n):
    tmp = input()
    cmd = tmp.split()

    if cmd[0] == 'push':
        stack = push(stack, int(cmd[1]))

    elif cmd[0] == 'pop':
        tmp, stack = pop(stack)
        res.append(tmp)

    elif cmd[0] == 'size':
        res.append(size(stack))

    elif cmd[0] == 'empty':
        res.append(empty(stack))

    elif cmd[0] == 'top':
        res.append(top(stack))

for i in range(len(res)):
    print(res[i])
