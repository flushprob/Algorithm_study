# BFS (Breadth-First Search)
# Queue
from collections import deque


def bfs(graph, start, visited):
    # queue 구현
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True

    # Queue가 빌 때까지 반복
    while queue:
        # Queue에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드 연결된 정보 - 2차원 리스트
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
# 각 노드가 방문된 정보를 표현
visited = [False] * len(graph)

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
