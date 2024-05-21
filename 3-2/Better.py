def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # 創建一個二維表格來存儲子問題的解
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 填充表格，逐步解決子問題
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 返回最長共同子序列的長度
    return dp[m][n]

# 讀取輸入的兩個字符串
X = input().strip()
Y = input().strip()

# 計算最長共同子序列的長度並輸出
print(longest_common_subsequence(X, Y))
