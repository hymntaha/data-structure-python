class AdjNode:

    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):

        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        # Adding the node to the source
        node = AdjNode(destination)
        node.next = self.graph[source]

        self.graph[source] = node

        # Adding the source node to the destination if undirected graph
        # Intentionally commented the lines
        # node = AdjNode(source)
        # node.next = self.graph[destination]
        # self.graph[destination] = node

    def print_graph(self):

        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

# V = 5  # Total vertices
# g = Graph(V)
# g.add_edge(0, 1)
# g.add_edge(0, 4)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
#
# g.print_graph()

def number_of_nodes(my_graph, level):
    source = 0

    # Mark all the vertices as not visited
    visited = [0] * (len(my_graph.graph))

    # Create a queue
    queue = []

    # Result string
    result = ""

    # Mark the source node as
    # visited and enqueue it

    queue.append(source)
    visited[source] = 1

    while queue:

        # Dequeue a vertex from queue
        source = queue.pop(0)

        # Get all adjacent vertices of the
        # dequeued vertex source. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it

        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if visited[data] == 0:
                queue.append(data)
                visited[data] = visited[source] + 1
            my_graph.graph[source]= my_graph.graph[source].next

    # Counting number of nodes at given level
    result = 0
    for i in range(len(my_graph.graph)):
        if visited[i] == level:
            result += 1
    return result

def transpose(my_graph):
    new_graph = Graph(my_graph.V)
    for source in range(my_graph.V):
        while my_graph.graph[source] is not None:
            destination = my_graph.graph[source].vertex
            # Now the source is destination and vice versa
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph

import copy # For deep copy if needed
def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    # Mark the current node as visited and store in path
    visited[source] = True
    path.append(source)

    # If current vertex is same as destination, then print
    # stores the current path in 2D list
    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex

        while graph.graph[source] is not None:
            i = graph.graph[source].vertex

            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, visited, path, paths)
            graph.graph[source] = graph.graph[source].next

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[source] = False

def find_all_paths(graph, source, destination):

    # Mark all the vertices as not visited
    visited = [False] * (graph.V)

    # Create a list to store paths
    paths = []
    path = []

    # Call the recursive helper function to find all paths
    find_all_paths_recursive(graph, source, destination, visited, path, paths)
    return paths


# V = 5
# g = Graph(V)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
#
# print(number_of_nodes(g, 2))
# V = 5
# g = Graph(V)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
#
# new_g = transpose(g)
# new_g.print_graph()

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(2, 5)

source = 0
destination = 5

paths = find_all_paths(g, source, destination)
print(paths)
