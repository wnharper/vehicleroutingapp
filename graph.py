# Function to build the graph
from collections import defaultdict

graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2}, 'd':{'e':7}, 'e':{'d':9}}

def build_graph():
    edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)

    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]

        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph


if __name__ == "__main__":
    graph = build_graph()

    print(graph)