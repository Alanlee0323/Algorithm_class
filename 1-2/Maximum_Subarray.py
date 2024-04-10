# A 為要操作的list
import sys


def Find_MAX_Crossing_Subarray(A, low, mid, high):
    
    left_sum = float('-inf')
    sum = 0
    
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
 
    right_sum = float('-inf')
    sum = 0

    for j in range(mid+1, high+1, 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return(max_left, max_right, left_sum + right_sum)


def Find_Maximum_Subarray(A, low, high):

    if high == low:
        return(low, high, A[low])
    
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = Find_Maximum_Subarray(A, low, mid)
        right_low, right_high, right_sum = Find_Maximum_Subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = Find_MAX_Crossing_Subarray(A, low, mid, high)

    if (left_sum >= right_sum) and (left_sum >= cross_sum):
        return(left_low, left_high, left_sum)
    
    elif (right_sum >= left_sum) and (right_sum >= cross_sum):
        return(right_low, right_high, right_sum)
    
    else:
        return(cross_low, cross_high, cross_sum)
    

while True:
# 讀取直到EOF的輸入
    input_numbers = []
    for line in sys.stdin:
        input_numbers.extend(map(int, line.split()))

    max_sum = Find_Maximum_Subarray(input_numbers, 0, len(input_numbers) - 1)[2]
    print(max_sum)
    break