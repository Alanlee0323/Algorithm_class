def Stern_Brocot_Tree(Numerator, Denominator):  #分子分母

    L = {'numerator': 0, 'denominator': 1}
    M = {'numerator': 1, 'denominator': 1}
    R = {'numerator': 1, 'denominator': 0}

    Fd = Numerator / Denominator
    Md = M["numerator"] / M["denominator"]

    while not (M['denominator'] == Denominator and M['numerator'] == Numerator):
        if Fd > Md: #比目前的中點大
            L['numerator'] = M['numerator']      # 中點設為新的左節點
            L['denominator'] = M['denominator']  # 中點設為新的左節點
            M['numerator'] += R['numerator']     # 計算新的中點
            M['denominator'] += R['denominator'] # 計算新的中點
            print("R", end="")
        else:
            R['numerator'] = M['numerator']      # 中點設為新的右節點
            R['denominator'] = M['denominator']
            M['numerator'] += L['numerator']
            M['denominator'] += L['denominator']
            print("L", end="")

        Md = M['numerator'] / M['denominator']
    print()

while True:
    input_line = input()  # 讀取一行輸入
    F_numerator, F_denominator = map(int, input_line.split())

    if F_numerator == 1 and F_denominator == 1:
        break  # 如果輸入為 "1 1"，終止迴圈

    # 調用函數並打印路徑
    Stern_Brocot_Tree(F_numerator, F_denominator)
    
