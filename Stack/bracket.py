def push(stack, num):
    stack.append(num)
    return stack

def pop(stack):
    if len(stack) == 0:
        return False, stack
    else:
        res = stack[len(stack) - 1]
        stack = stack[:len(stack)-1]
        return res, stack

def size(stack):
    return len(stack)

def empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def top(stack):
    return stack[len(stack) - 1]

brckt = input()
brckts = list(brckt)

stack = []
n = len(brckts)
res = True

for i in range(n):
    if brckts[i] == '(':
        stack = push(stack, '(')
    else:
        tmp, stack = pop(stack)
        if tmp is False:
            res = False


if empty(stack) and res:
    print('Yes')
else:
    print('No')