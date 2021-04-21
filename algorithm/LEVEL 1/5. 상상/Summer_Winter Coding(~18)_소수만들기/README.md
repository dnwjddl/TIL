## 문제설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.  
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

|nums|result|
|----|-----|
|[1,2,3,4]|1|
|[1,2,7,6,4]|4|

### 1번. list에서 세개의 숫자만 뽑아서 합치기
```python
from itertools import combinations
# arr에 3개의 요소끼리 합칠 수 있음
arr = list(combinations(nums, 3)
```


### 2번. 합친 숫자가 소수인지 확인하기
```python
def is_prime_number(x):
  for i in range(2, x):
    if x & i == 0:
      return False
  return True
```
