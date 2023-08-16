def depthFirstSearch(visited_nodes, graph, current_node):
    if current_node not in visited_nodes:
        print(current_node)
        visited_nodes.add(current_node)
        for neighbor in graph[current_node]:
            depthFirstSearch(visited_nodes, graph, neighbor)

my_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}
visited_set = set()
print("Depth-First Search Traversal:")
depthFirstSearch(visited_set, my_graph, 'A')
