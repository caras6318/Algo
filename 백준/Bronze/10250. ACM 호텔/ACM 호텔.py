case = int(input())
for i in range(case):
    a,b,c = map(int,input().split())
    j = 1
    k = 1
    while c > j*a:
        j += 1
    while not c-a*k < a:
        k += 1
    d = c-a*k
    if a > c:
        d = c
    if d == 0:
        d = a
    if j < 10:
        print(d*10,j,sep="")
    else:
        print(d,j,sep="")