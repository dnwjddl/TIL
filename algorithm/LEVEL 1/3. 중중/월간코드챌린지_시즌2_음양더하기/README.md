## 문제설명

absolutes와 sign의 같은 길이의 list가 주어짐
True이면 absolutes을 더해주고  
False면 absolutes를 빼줌  

|absolutes|signs|result|
|---------|------|-----|
|[4, 7, 12]|[true, false, true]|9|
|[1,2,3]|[false, false, true]|0|


```python
def solution(absolutes, signs): 
  return sum(absolutes[i] * (1 if signs[i] else -1) for i in range(len(signs)))
  
# 어차피 True면 if가 성립됨
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
```
