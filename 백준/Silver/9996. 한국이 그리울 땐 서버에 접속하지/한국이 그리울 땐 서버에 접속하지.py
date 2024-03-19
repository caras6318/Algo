case = int(input())
pattern = input().split("*")
for _ in range(case):
    text = input()
    if len(pattern[0])+len(pattern[1]) > len(text):
        print("NE")
    else:
        print("DA") if (pattern[0] == text[:len(pattern[0])]) and (pattern[1] == text[-1*len(pattern[1]):]) else print("NE")