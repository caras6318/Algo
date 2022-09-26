import sys
ins = sys.stdin.readline
c = int(input())
i = 0
while i < c:
    a,b = map(int,ins().split())
    print("Case #",i+1,": " ,a+b,sep="")
    i += 1
