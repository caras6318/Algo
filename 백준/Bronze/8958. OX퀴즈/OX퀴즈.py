case = int(input())
c = [0]*case
for  i in range (case):
    c[i] = list(input())
for i in range (case):
    total = 0
    score = 1
    for j in range (len(c[i])):
        if c[i][j] == "O":
            total += score
            score += 1
        elif c[i][j] == "X":
            score = 1
    print(total)