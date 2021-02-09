'''나의 풀이'''

'''에라토스테네스의 체 사용
1. 1제거
2. 2제외 2의 배수 제거
3. 3제외 3의 배수 제거
4. 4제외 4의 배수 제거...
'''

def solution(n):
    a = [False, False] + [True] *(n-1) #초기화
    primes = []
    for i in range(2, n+1):
        if a[i]: #True일때
            primes.append(i)
            for j in range(2*i, n+1, i): # i배수 만큼 False로
                a[j] = False
    return len(primes)

'''다른 참여자들의 풀이'''
def solution1(n): #차집합을 사용
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

'''나의 이전 풀이'''
'''효율성 테스트 실패'''
def numberOfPrime(n):
    count=0
    for n in range(2,n+1):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            count+=1
    return count



print(numberOfPrime(10))