import numpy as np

# 初始化數據
X = np.array([
    [-2, 1],
    [1, 1],
    [1.5, -0.5],
    [-2, -1],
    [-1, -1.5],
    [2, -2]
])

# 添加偏置項 (1) 到每個數據點
X_bias = np.c_[np.ones(X.shape[0]), X]

# 初始化初始權重
w = np.array([0.0, 1.0, 0.0])

# 學習率
eta = 0.4

# 標籤
y = np.array([1, 1, 1, -1, -1, -1])

# Perceptron Algorithm
max_iterations = 1000
for iteration in range(max_iterations):
    misclassified = False
    print(f"Iteration {iteration + 1}:")
    for i, x in enumerate(X_bias):
        # 計算預測的類別
        y_pred = np.sign(np.dot(w, x))
        
        # 更新權重如果預測不正確
        if y_pred != y[i]:
            print(f"  Updating weights for point {i + 1}:")
            print(f"    Old weights: {w}")
            w += eta * y[i] * x.astype(float)
            print(f"    New weights: {w}")
            misclassified = True
            
    # 如果所有的例子都被正確分類，就停止迭代
    if not misclassified:
        break

# 計算分隔兩個類別的直線的斜率和截距
slope = -w[1] / w[2]
intercept = -w[0] / w[2]

print("\nFinal Equation of the separating line: y = {:.2f}x + {:.2f}".format(slope, intercept))
