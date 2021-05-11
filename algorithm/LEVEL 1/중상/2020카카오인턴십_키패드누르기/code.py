import numpy as np

def solution(numbers, hand):
    left_hands = -1
    right_hands = -2
        
    answer = ''
    
    num = np.array([[1,2,3], [4,5,6], [7,8,9], [-1, 0 ,-2]]) 
    for number in numbers:
        if number == 1 or number == 4 or number == 7: #무조건 왼손
            answer += 'L'
            left_hands = number
        elif number == 3 or number == 6 or number == 9: #무조건 오른손
            answer += 'R'
            right_hands = number
        else:
            aIndex = np.where(num==number)
            leftIndex = np.where(num == left_hands)
            rightIndex = np.where(num == right_hands)
            
            lefts = abs(aIndex[0] - leftIndex[0]) + abs(aIndex[1] - leftIndex[1])
            rights = abs(aIndex[0] - rightIndex[0]) + abs(aIndex[1] - rightIndex[1])
            if lefts < rights:
                answer += 'L'
                left_hands  = number
            elif rights < lefts:
                answer += 'R'
                right_hands = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hands  = number
                else:
                    answer += 'R'
                    right_hands = number
    return answer
