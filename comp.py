import networkx as nx
import time

def build(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def dfs(start):
    stack = [start]
    while stack:
        u = stack.pop()
        if u in not_visited:
            not_visited.remove(u)
            for x in g[u]:
                if x in not_visited:
                    stack.append(x)


def count_by_networkx(n, edges):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    return nx.number_connected_components(G)


with open("input.txt", "r") as f:
    t = int(f.readline())
    ans = []

    total_dfs_time = 0
    total_nx_time = 0

    for _ in range(t):
        n, k = map(int, f.readline().split())
        edges = []

        for _ in range(k):
            u, v = map(int, f.readline().split())
            if 0 <= u < n and 0 <= v < n:
                edges.append((u, v))

        g = build(n, edges)
        not_visited = set(range(n))

        start_dfs = time.time()

        count = 0
        while not_visited:
            y = not_visited.pop()
            not_visited.add(y)
            dfs(y)
            count += 1

        end_dfs = time.time()
        total_dfs_time += (end_dfs - start_dfs)

        start_nx = time.time()

        nx_count = count_by_networkx(n, edges)

        end_nx = time.time()
        total_nx_time += (end_nx - start_nx)

        ans.append(f"DFS: {count}, NetworkX: {nx_count}")

    ans.append(f"\nTotal DFS time: {total_dfs_time:.6f}s")
    ans.append(f"Total NetworkX time: {total_nx_time:.6f}s")


with open("output.txt", "w") as file:
    file.write("\n".join(ans))