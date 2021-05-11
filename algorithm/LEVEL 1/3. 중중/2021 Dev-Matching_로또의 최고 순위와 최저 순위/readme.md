# 로또의 최고 순위와 최저 순위

https://programmers.co.kr/learn/courses/30/lessons/77484

```dictionary```활용, ```.count('?')```활용


```python
#수경이 코드
## dictionary 활용

ranking = {'6':1, '5': 2, '4':3, '3':2, '2':5}
unknown = lottos.count(0) #0을 count함
count = 0

...

high = ranking[str(count+unknown)] if (count+unknown) in [6,5,4,3,2] else 6
low = ranking[str(count)] if(count) in [6,5,4,3,2] else 6
answer = [high, low]

```
