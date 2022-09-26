a = int(input())
af = 0
ao = a
cnt = 0
while True:
    if a < 10:
        a *= 10
        f,b  = a // 10, a % 10 
        af =((f + b)%10) + (f+b)* 10
    else:
        f,b  = a // 10, a % 10 
        af =((f + b)%10) + b* 10
    cnt += 1
    if af == ao:
        break
    a = af
print(cnt)