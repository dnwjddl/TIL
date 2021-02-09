'''나의 풀이'''

def solution(n):
    return "수박"*(n//2) + "수"*(n%2)

'''다른 참여자의 풀이'''
def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))