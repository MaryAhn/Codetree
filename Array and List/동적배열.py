n = int(input())
arr = []

for _ in range(n):
    tmp = input()
    tmp_arr = tmp.split()
    print(tmp_arr)
    if(len(tmp_arr) == 1):
        if(tmp_arr[0] == 'size'):
            print(len(arr))
        else:
            arr.pop()
    elif(len(tmp_arr)== 2):
        if(tmp_arr[0]=='push_back'):
            arr.append(tmp_arr[1])
        else:
            print(arr[int(tmp_arr[1])-1])
