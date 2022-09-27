case = int(input())
c = [0]*case
cnt = 0
lc = []
for  i in range (case):
    c[i] = list(map(int,input().split()))
    lc.append(len(c[i]))
for i in range (case):
    rev = 0
    for j in range (lc[i]-1):
        rev += c[i][j+1]
    for j in range (lc[i]-1): 
        if rev/(lc[i]-1) < c[i][j+1]:
            cnt += 1
    print(format(cnt/(lc[i]-1)*100,".3f"),"%",sep="")
    cnt = 0