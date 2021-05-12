def solution(d, budget):
    answer = 0
    sum_ = 0
    for i in sorted(d) :
        sum_+=i
        if sum_ <= budget :
            answer+=1
    return answer
