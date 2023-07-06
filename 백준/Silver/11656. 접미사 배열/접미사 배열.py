    
def comb(s):
    sss = []
    for i in range(len(s)):
        sss.append(s[i:])
    sss = sorted(sss)
    for i in range(len(sss)):
        print(sss[i])
    
    
    
    
    
    
sss = input()
comb(sss)