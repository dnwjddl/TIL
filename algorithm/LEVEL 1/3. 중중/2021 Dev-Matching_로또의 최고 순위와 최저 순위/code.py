def solution(lottos, win_nums):
    count = 0
    nun = 0 #0의 갯수
    answer = []

    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        if lotto == 0:
            nun += 1

    fin = nun + count

    if fin == 0 : fin = 1
    if count == 0: count = 1

    answer.append(7-fin)
    answer.append(7-count)

    return answer
