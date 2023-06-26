def solution(name, yearning, photo):
    a = {}
    sum = 0
    answer = []
    for i in range(len(name)):
        a[name[i]] = yearning[i]
    for j in range(len(photo)):
        for i in range(len(photo[j])):
            if photo[j][i] in a: 
                sum += a[photo[j][i]]
        answer.append(sum)
        sum = 0
    
    return answer