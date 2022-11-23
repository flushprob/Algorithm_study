# DFS
# Depth First Search


def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        # 현재 방문하지 않았다면 DFS 재귀함수 실행
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * len(graph)

dfs(graph, 1, visited)
