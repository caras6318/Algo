res = [-1]*26
case = list(str(input()))
for i in range(len(case)):
    for j in range (26):
        if case[i] == chr(97+j):
            if res[j] == -1:
                res[j] += i+1
for i in range(26):
    print(res[i],end=" ")