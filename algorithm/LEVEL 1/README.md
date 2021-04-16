## 완전 탐색

모든 경우의 수를 전부 찾아서 답을 찾는 알고리즘

### 완전 탐색의 방법
- Brute Forece: for문과 if문을 이용하여 처음부터 끝까지 탐색하는 방법
- 비트 마스크 (AND, OR, XOR, SHIFT, NOT)
- 순열
- 백트래킹
- BFS

## python 다운 풀이
- ```divmod```
```python
(7//3, 7%3) = divmod(7,3)

a, b = divmod(n, m)
```
- ```int(x, base)``` (진법 변환 지원)
base 진법으로 구성된 str형식의 수를 10진법으로 변환
```python
answer = int(answer, 3)
```

중복 싫으면 ```set``` :단, sort도 됨  
sort하고 싶을때, sort(list)하지만(type이 다른거 나옴) sorted(list, reverse = True, key = 'person')도 가능  
```min(a,b)```, ```max(a,b)```,```sum(range(a,b))```함수들도 기억하기
