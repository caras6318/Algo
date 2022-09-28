a,b = map(int,input().split())
al= list(str(a))
bl= list(str(b))
tmp = al[0]
al[0] = al[2]
al[2] = tmp
tmp = bl[0]
bl[0] = bl[2]
bl[2] = tmp

ai = int(al[0])*100+int(al[1])*10+int(al[2]) 
bi = int(bl[0])*100+int(bl[1])*10+int(bl[2])
if ai < bi:
    print(bi)
else:
    print(ai)