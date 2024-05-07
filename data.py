import numpy as np

# 定義初始中心點
initial_centers = np.array([[2, 1], [3, 1]])

# 定義數據
data = np.array([
    [2, 1],
    [3, 1],
    [4, 3],
    [6, 9],
    [2, 4],
    [7, 8]
])

# 定義 k-means 函數
def k_means(data, initial_centers, k, max_iter=100):
    centers = initial_centers.copy()
    
    for iter in range(max_iter):
        # 計算每個點到中心點的距離
        distances = np.linalg.norm(data[:, None, :] - centers, axis=2)
        
        # 將每個點分配到距離最近的中心點所對應的群組
        labels = np.argmin(distances, axis=1)
        
        # 輸出每次分類每個點與中心點的距離
        print(f"Iteration {iter + 1}:")
        for i in range(len(data)):
            print(f"Point {i + 1} - Distance to center 1: {distances[i][0]}, Distance to center 2: {distances[i][1]}")
        
        # 更新中心點的位置為每個群組的平均值
        new_centers = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # 打印每次迭代生成的新中心點
        print(f"New centers after iteration {iter + 1}:")
        for i, center in enumerate(new_centers):
            print(f"Center {i + 1}: {center}")
        
        # 如果中心點位置不再改變，則停止迭代
        if np.all(centers == new_centers):
            break
        
        centers = new_centers
    
    return labels, centers

# 執行 k-means 算法
labels, centers = k_means(data, initial_centers, k=2)

# 輸出分類結果
print("\nFinal Group 1:", data[labels == 0])
print("Final Group 2:", data[labels == 1])
