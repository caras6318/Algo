d = list(range(1,10000))
l = []

for i in range(1,10000):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result <= 10000:
        l.append(result)
l.sort()
# print(l)
for j in d:
    if j not in l:
        print(j)