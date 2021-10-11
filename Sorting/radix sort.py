n = int(input())
nums = input()
num = nums.split()
max_digit = 0
max = 0

for i in range(n):
    if(len(num[i]) > max_digit):
        max_digit = len(num[i])

for i in range(n):
    if(len(num[i])<max_digit):
        for j in range(max_digit-len(num[i])):
            num[i] = '0' + num[i]

for i in range(max_digit-1, -1, -1):
    num_next = []
    dict_digit = {}
    for tmp in range(10):
        dict_digit[tmp] = []
    for j in range(n):
        tmp_num = num[j]
        dict_digit[int(tmp_num[i])].append(tmp_num)
    for key in dict_digit:
        for k in range(len(dict_digit[key])):
            num_next.append(dict_digit[key][k])
    num = num_next

for i in range(n):
    print(num[i], end=' ')
