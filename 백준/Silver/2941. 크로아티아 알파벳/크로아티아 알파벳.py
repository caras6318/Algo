alp = list(str(input()))
cnt = len(alp)
for i in range(1,cnt):
    if alp[i] == "j" and (alp[i-1] == "l" or alp[i-1] == "n"):
        cnt -= 1
    elif alp[i] == "-" and (alp[i-1] == "c" or alp[i-1] == "d"):
        cnt -= 1
    elif alp[i] == "=" and (alp[i-1] == "c" or alp[i-1] == "s"):
        cnt -= 1
    elif alp[i] == "=" and alp[i-1] == "z":
        if cnt > 2 and alp[i-2] == "d": 
            cnt -= 2
        else:
            cnt -= 1
print(cnt)