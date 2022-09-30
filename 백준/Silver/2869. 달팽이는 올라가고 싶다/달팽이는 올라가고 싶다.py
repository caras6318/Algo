import math

a,b,c = map(int,input().split())
cnt = int(math.ceil((c-a)/(a-b)))
    
print(cnt+1)