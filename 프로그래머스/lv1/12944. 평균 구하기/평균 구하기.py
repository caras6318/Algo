def solution(arr):
    answer = 0
    for i in range (len(arr)):
        answer += arr[i]
    answer /= int(len(arr))
    return answer