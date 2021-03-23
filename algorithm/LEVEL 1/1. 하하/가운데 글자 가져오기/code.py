def solution(s):
    b = len(s) // 2
    if len(s) % 2 == 0:
        answer = s[b-1:b+1]
    else:
        answer = s[b]
    return answer
