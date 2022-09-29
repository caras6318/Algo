import sys
sys.setrecursionlimit(10**6)
def bee(a, cnt):
    if a <= 0:
        print(cnt)
        return 
    else:
        a -= 6 * cnt
        cnt += 1
        bee(a, cnt)
a = int(input())
i = 1
if a == 1:
    print(1)
else:
    bee(a-1,i)