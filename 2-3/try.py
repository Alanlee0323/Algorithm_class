class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_v] += 1
            return True
        return False

def kruskal(nodes, edges):
    forest = UnionFind(nodes)
    mst = []
    cost = 0
    
    for edge in sorted(edges, key=lambda e: (e[2], e[0], e[1])):
        u, v, weight = edge
        if forest.union(u, v):
            mst.append((u, v))
            cost += weight
    
    return mst, cost

def create_adjacency_list(mst, nodes):
    adj_list = {i: [] for i in range(nodes)}
    for u, v in mst:
        print(f"Adding edge ({u}, {v}) to adjacency list")
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list



# 示例數據
edges = [
    (0, 1, 28), (0, 5, 10), (1, 2, 16), (1, 6, 14),
    (2, 3, 12), (3, 4, 22), (3, 6, 18), (4, 5, 25), (4, 6, 24)
]
nodes = 7

mst, total_cost = kruskal(nodes, edges)
adj_list = create_adjacency_list(mst, nodes)

# 輸出鄰接表
print("Adjacency list:")
for node, neighbours in adj_list.items():
    print(f"{node}: {' -> '.join(map(str, sorted(neighbours)))} -> end")

# 輸出最小生成樹
print("\nminimum spanning tree:")
for i, (u, v) in enumerate(sorted(mst, key=lambda edge: edge[2]), start=1):
    print(f"{i}: <{u},{v}> (weight: {edge[2]})")



# 輸出最小成本
print(f"\nThe cost of minimum spanning tree: {total_cost}")
