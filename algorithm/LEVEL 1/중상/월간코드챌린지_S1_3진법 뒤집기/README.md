# 문제설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예시
|n(10진법)|n(3진법)|앞뒤 반전(3진법)|10진법으로 표현|
|:--------:|:--------:|:--------:|:--------:|
|45|1200|0021|7|


## 오답

```python
def solution(n):
    # 3진법
    num = ''
    while n>2:
        n,m = divmod(n, 3)
        num += str(m)
    num += str(n)
    
    return int(num, 3)
```

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
