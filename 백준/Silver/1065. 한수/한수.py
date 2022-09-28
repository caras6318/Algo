a = int(input())
cnt = 0
if a <= 99:
    print(a)
else:
    for i in range(100,a+1):
        tmp = list(map(int, str(i)))
        if (tmp[0] - tmp[1]) == (tmp[1] - tmp[2]):
            cnt += 1
    print(cnt+99)