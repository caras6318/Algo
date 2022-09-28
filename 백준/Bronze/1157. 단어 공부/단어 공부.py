alp = []
cnt = [0]*26
max = 0
for i in range (26):
    alp.append(chr(65+i))
s = list(str(input()).upper())
for i in range(len(s)):
    for j in range (26):
        if s[i] == alp[j]:
            cnt[j] += 1
            if cnt[j] > max:
                max = cnt[j]
                most = j
                flag = 0
            elif cnt[j] == max:
                flag = 1
if flag != 1:
    print(alp[most])
else:
    print("?")