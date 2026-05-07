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


with open("input.txt", "r") as f:
    t = int(f.readline())
    ans = []

    for _ in range(t):
        n, k = map(int, f.readline().split())
        edges = []

        for _ in range(k):
            u, v = map(int, f.readline().split())
            if 0 <= u < n and 0 <= v < n:
                edges.append((u, v))

        g = build(n, edges)
        not_visited = set(range(n))

        count = 0
        while not_visited:
           y=not_visited.pop()
           not_visited.add(y)
           dfs(y)
           count+=1

        ans.append(f"graph {len(ans)+1}: {count}")


with open("output.txt", "w") as file:
    file.write("\n".join(ans))