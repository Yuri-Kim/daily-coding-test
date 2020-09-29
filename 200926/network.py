def dfs(graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit


def solution(n, computers):
    graph = {node: [] for node in range(n)}
    print(graph)
    for i, computer in enumerate(computers):
        print(i, computer)
        for j, conn in enumerate(computer):
            if i != j and conn == 1:
                graph[i].append(j)
                print(graph)
    paths = map(sorted, [dfs(graph, node) for node in graph])

    return len(set(["".join(map(str, path)) for path in paths]))


def test_solution():
    # assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1
