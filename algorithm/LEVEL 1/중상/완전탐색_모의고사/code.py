def solution(answers):
    a=0
    b=0
    c=0
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []

    for i in range(0, len(answers)):
        if n1[(int(i%5))] == answers[i]:
            a += 1
        if n2[(int(i%8))] == answers[i]:
            b += 1
        if n3[(int(i%10))] == answers[i]:
            c += 1

    max_ = max(a, b, c)
    if a == max_:
        answer.append(1)
    if b == max_:
        answer.append(2)
    if c == max_:
        answer.append(3)   

    return answer
