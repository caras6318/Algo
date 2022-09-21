a= list(map(int,input().split()))
b = 0
for i in range(5):
    b += a[i]*a[i]
b %= 10
print(b)