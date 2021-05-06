# Function implements a version of Dijkstra's algorithm in order to calculate
# the distance and shortest path between two nodes
def shortest_route(graph, start, destination):
    shortest_distance = {}
    predecessor = {}
    unvisited_nodes = graph.copy()
    infinity = 99999999
    path = []
    for node in unvisited_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unvisited_nodes:
        min_node = None
        for node in unvisited_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for childNode, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[min_node]
                predecessor[childNode] = min_node
        unvisited_nodes.pop(min_node)

    current_node = destination
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[destination] != infinity:
        # print('The shortest distance is ' + str(shortest_distance[destination]))
        # print('The route is ' + str(path))
        return shortest_distance[destination]


# Function uses shortest_route (Dijkstra's algorithm) to determine a route order
# based on a greedy algorithm (next closest node)
def calculate_route(packages, graph, start):
    closest = 9999
    package_order = []
    next_package = None

    while packages.num_elements != 0:

        for package in packages:
            current_distance = shortest_route(graph, start, package.address)
            if current_distance < closest:
                next_package = package
                closest = current_distance

        package_order.append(next_package)
        start = next_package.address
        closest = 9999
        del packages[next_package.id]

    return package_order
