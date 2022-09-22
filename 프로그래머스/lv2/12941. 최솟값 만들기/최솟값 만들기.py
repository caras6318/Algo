def solution(A,B):
    answer = 0

    l = len(A)
    A = sorted(A)
    B = sorted(B)
    for i in range (l):
        answer += (A[i] * B[l-1-i])

    return answer