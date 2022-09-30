x = int(input())
i, j, cnt, flag = 1, 1, 1, 1
f = 0
a = 1
while a + f < x:
    f += 1
    a += f
    
if f % 2 == 1:
    j += f
else:
    i += f

cnt = a


while cnt < x:
    if (i == 1):
        if (j % 2 == 1):
            j += 1
            cnt += 1
        else: 
            while j > 1:
                i += 1
                j -= 1
                cnt += 1
                if cnt == x:
                    break
    elif (j == 1):
        if (i % 2 == 0):
            i += 1  
            cnt += 1
        else:
            while i > 1:
                j += 1
                i -= 1
                cnt += 1
                if cnt == x:
                    break
print(i,"/",j,sep="")