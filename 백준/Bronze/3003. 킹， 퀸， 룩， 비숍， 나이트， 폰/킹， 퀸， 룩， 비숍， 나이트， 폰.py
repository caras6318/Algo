b = [1,1,2,2,2,8]
w = list(map(int,input().split()))
for i in range (6):
    b[i] -= w[i]
    print(b[i],end=' ')