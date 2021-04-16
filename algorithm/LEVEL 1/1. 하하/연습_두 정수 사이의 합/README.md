## 문제 설명

두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.  
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.


```python
# 나의 풀이
for i in range(min(a, b), max(a,b)+1):
  answer += i

# 간단한 풀이
return sum(range(min(a,b),max(a,b)+1))
```

## 오답
for문을 사용하지 않아도 ```sum```함수로 간단하게 range 안의 수들을 합해줄 수 있다.
