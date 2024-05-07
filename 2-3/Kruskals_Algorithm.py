class UnionFind:
    def __init__(self, n):
        # 初始化方法，接受一個整數參數 n，表示要初始化的元素數量
        self.parent = list(range(n))  # 初始化每個元素的父節點為自己，形成初始的不相交集合
        self.rank = [0] * n  # 用於保存每個集合的秩或高度，初始值全部為 0

    def find(self, i):
        # 找到元素 i 所在集合的根節點的方法
        if self.parent[i] != i:
            # 如果 i 的父節點不是自己，則遞迴地找尋 i 的父節點，並將 i 所在集合的所有節點的父節點直接設為根節點，以優化查找效率
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        # 合併兩個集合的方法
        root_a = self.find(a)  # 找到元素 a 所在集合的根節點
        root_b = self.find(b)  # 找到元素 b 所在集合的根節點
        if root_a == root_b:
            # 如果兩個元素已經在同一集合中，無需再合併，直接返回 False
            return False
        if self.rank[root_a] < self.rank[root_b]:
            # 按秩合併：將秩較小的集合合併到秩較大的集合中
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            # 如果兩個集合的秩相同，則將其中一個集合的根節點指向另一個集合的根節點，並將後者的秩加 1
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        return True


def kruskal(edges, num_vertices):
    # 使用 Kruskal 算法來找到最小生成樹
    # 初始化一個 UnionFind 物件，並指定頂點的數量
    uf = UnionFind(num_vertices)
    # 初始化一個空的最小生成樹列表
    minimum_spanning_tree = []
    # 初始化總成本
    cost = 0
    # 將邊依照權重排序
    edges.sort(key=lambda x: (x[2], x[0], x[1]))  # 函式在排序時，會根據這個元組中的第一個值（權重）、第二個值（起始頂點）、第三個值（終止頂點）來決定排序的優先順序

    # 遍歷排序後的邊
    for edge in edges:
        # 提取邊的起始頂點、終止頂點和權重
        u, v, weight = edge
        # 如果將當前的邊加入最小生成樹不會形成環路
        if uf.union(u, v):
            # 將當前邊加入最小生成樹
            minimum_spanning_tree.append((u, v))
            # 增加總成本
            cost += weight
    # 返回最小生成樹和成本
    return minimum_spanning_tree, cost

def create_adjacency_list(mst, num_vertices):
    # 創建一個鄰接表表示最小生成樹

    # 創建一個字典包含 o 到 (n-1) nodes 的所有節點作為字典的keys,對應值為空列表用來儲存鄰居節點
    adj_list = {i: [] for i in range(num_vertices)}
    # 遍歷最小生成樹中的每條邊
    for u, v in mst:
        print(f"Adding edge ({u}, {v}) to adjacency list")
        # 將邊的兩個頂點加入彼此的鄰接表中
        if v not in adj_list[u]:
            adj_list[u].append(v)
        if u not in adj_list[v]:
            adj_list[v].append(u)
    for i in range(num_vertices):
        adj_list[i].sort()  # 对邻接顶点进行排序
    # 返回最小生成樹的鄰接表
    return adj_list

def main():
    # 讀取輸入
    edges = []
    num_vertices = 0
    while True:
        try:
            u, v, weight = map(int, input().split('\t'))
            edges.append((u, v, weight))
            num_vertices = max(num_vertices, u, v)
        except EOFError:
            break

    num_vertices += 1  # 因為頂點從 0 開始

    # 使用 Kruskal 算法找到最小生成樹
    mst, cost = kruskal(edges, num_vertices)

    # 創建鄰接表
    adj_list = create_adjacency_list(mst, num_vertices)

    # 輸出鄰接表
    print("Adjacency list:")
    for vertex in sorted(adj_list.keys()):
        print(f"{vertex}: {' -> '.join(map(str, adj_list[vertex]))} -> end")
    print()

    # 輸出 minimum spanning tree 的所有邊及其最小成本
    print("minimum spanning tree:")
    for edge in sorted(mst):
        if len(edge) == 3:
            u, v, weight = edge
            print(f"{weight}: <{u},{v}>")
        else:
            u, v = edge
            print(f"<{u},{v}>")
    print(f"\nThe cost of minimum spanning tree: {cost}")


if __name__ == "__main__":
    main()


