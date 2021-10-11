from Tree import maxheap

n = int(input())
cmds = []
res = []

for i in range(n):
    cmds.append(int(input()))

for cmd in cmds:
    if(cmd > 0):
        res.append(cmd)
    else:
        if len(res) == 0:
            print(0)
        else:
            res = maxheap.build_heap(res)
            print(res[0])
            res = res[1:]



