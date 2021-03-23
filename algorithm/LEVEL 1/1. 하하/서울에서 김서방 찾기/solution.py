'''나의 풀이'''
def solution(seoul):
    x = seoul.index('Kim')
    return ("김서방은 %d에 있다" % (x))

'''다른 참여자들의 풀이'''
def solution1(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))