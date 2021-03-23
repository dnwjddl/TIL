'''나의 풀이'''
def solution(s):
    answer = True
    if len(s) != 4 & len(s) != 6:
        answer = False
    else:
        answer = s.isdigit()

    return answer

'''다른 참여자들의 풀이'''
def solution1(s):
    return s.isdigit() and len(s) in (4,6)

def solution2(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6