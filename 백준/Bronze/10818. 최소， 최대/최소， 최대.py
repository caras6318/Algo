a = int(input())
arr = input().split()
l = len(arr)
i = 0
while i < l:
    arr[i] = int(arr[i])
    i += 1
arr.sort()
print(arr[0],arr[l-1])