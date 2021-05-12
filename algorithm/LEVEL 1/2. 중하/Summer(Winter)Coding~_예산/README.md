# 예산


https://programmers.co.kr/learn/courses/30/lessons/12982

```python
# sum을 하면 시간 복잡도가 O(n^2)가 되니까 원소를 빼는 편 O(n)이 낫다
# for과 if을 쓰지않고 while로 한번에 가능

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
```

```python
#나의 풀이

def solution(d, budget):
    answer = 0
    sum_ = 0
    for i in sorted(d) :
        sum_+=i
        if sum_ <= budget :
            answer+=1
        else :
            break

    return answer
```
