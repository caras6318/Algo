a = list(map(str,input()))
s = [0]*len(a)
for i in range(len(a)):
    if ord(a[i]) <= 90 and ord(a[i]) >= 65:
        a[i] = ord(a[i]) + 32
    else: 
        a[i] = ord(a[i]) - 32
for i in range (len(a)):
    print(chr(a[i]),end="")