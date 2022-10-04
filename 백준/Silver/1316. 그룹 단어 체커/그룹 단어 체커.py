t = int (input())
case = [0] * t
a = []
cnt = 0
for i in range (t):
    case[i] = list(map(str,input()))
    a = ''.join(dict.fromkeys(case[i]))
    a = list(map(str,a))
    ck = []
    for j in range (len(case[i])-1):
        if case[i][j] != case[i][j+1]:
            ck.append(case[i][j])
    if len(case[i]) != 1:
        ck.append(case[i][j+1])
    elif len(case[i]) == 1:
        cnt +=1
    if len(a) == len(ck):
        cnt +=1 
    
print(cnt)