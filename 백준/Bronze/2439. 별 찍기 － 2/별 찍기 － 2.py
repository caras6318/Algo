c = int(input())
i = 0
while i < c:
    for j in range(c-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    i += 1
    print()
