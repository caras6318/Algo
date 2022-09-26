import sys
case = int(input())
i = 0
while i < case:
    a,b = map(int,sys.stdin.readline().split())
    print(a + b)
    i += 1