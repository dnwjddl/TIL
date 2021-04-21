def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

from itertools import combinations
def solution(nums):
    count = 0
    for arr in list(combinations(nums, 3)):
        if is_prime_number(sum(arr)):
            count += 1
        else:
            continue

    return count
