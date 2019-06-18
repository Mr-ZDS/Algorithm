graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def BFS(graph, start):
    visit = [start]  # 存放已经放到队列中的元素
    queue = [start]
    path = {start: None}  # 字典记录每个结点的上一个结点，可用于求最短路径
    while len(queue) > 0:
        node1 = queue.pop(0)
        node2 = graph[node1]
        for i in node2:
            if i not in visit:
                queue.append(i)
                visit.append(i)
                path[i] = node1
        print(node1)
    return path


path = BFS(graph, 'A')
for keys, values in path.items():
    print(keys, values)


def DFS(graph, start):
    visit = [start]  # 存放已经放到队列中的元素
    stack = [start]
    while len(stack) > 0:
        node1 = stack.pop()
        node2 = graph[node1]
        for i in node2:
            if i not in visit:
                stack.append(i)
                visit.append(i)
        print(node1)
