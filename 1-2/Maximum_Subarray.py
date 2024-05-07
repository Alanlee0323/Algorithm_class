# A 為要操作的 list
import sys

# 找到跨越中點的最大子陣列
def Find_MAX_Crossing_Subarray(A, low, mid, high):
    # 初始化左半部分的最大總和為負無窮大
    left_sum = float('-inf')
    sum = 0
    
    # 從中點向左遍歷，找到最大左子陣列的結束位置
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
 
    # 初始化右半部分的最大總和為負無窮大
    right_sum = float('-inf')
    sum = 0

    # 從中點向右遍歷，找到最大右子陣列的結束位置
    for j in range(mid+1, high+1, 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    # 返回跨越中點的最大子陣列的起始位置、結束位置和總和
    return(max_left, max_right, left_sum + right_sum)

# 找到最大子陣列
def Find_Maximum_Subarray(A, low, high):
    # 如果陣列中只有一個元素，則直接返回該元素的索引和值
    if high == low:
        return(low, high, A[low])
    
    else:
        # 計算中點
        mid = (low + high) // 2
        # 遞歸地找到左半部分的最大子陣列
        left_low, left_high, left_sum = Find_Maximum_Subarray(A, low, mid)
        # 遞歸地找到右半部分的最大子陣列
        right_low, right_high, right_sum = Find_Maximum_Subarray(A, mid+1, high)
        # 找到跨越中點的最大子陣列
        cross_low, cross_high, cross_sum = Find_MAX_Crossing_Subarray(A, low, mid, high)

    # 返回左半部分、右半部分和跨越中點的最大子陣列中總和最大的那個
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

    # 找到最大子陣列的總和並輸出
    max_sum = Find_Maximum_Subarray(input_numbers, 0, len(input_numbers) - 1)[2]
    print(max_sum)
    break
