# Python program to print BFS traversal of a graph 
# starting from a given source node
# Sourced from geeksforgeeks.org

from collections import defaultdict

# This class represents a graph in adjacency list form: 
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        # Difference between default dict and regular
        # Is that types of values specified in instantiation
        self.graph = defaultdict(list)

    # Function to add an edge to a graph
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    # Function to print BFD of graph
    def BFS(self, source_node):

        # Mark all vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(source_node)
        visited[source_node] = True

        while queue:

            # Dequeue a vertex from the queue and print it
            source_node = queue.pop(0)
            print(source_node, end = " ")

            # Get all adjacent vertices of the dequeued vertex source_node
            # If an adjacent hasn't been visited, mark it visited and enqueue it
            for node in self.graph[source_node]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True


if __name__ == "__main__":
    my_graph = Graph()
    my_graph.addEdge(0, 1)
    my_graph.addEdge(0, 2)
    my_graph.addEdge(1, 2)
    my_graph.addEdge(2, 0)
    my_graph.addEdge(2, 3)
    my_graph.addEdge(3, 3)

    print("The following is the BFS starting from vertex 2")

    my_graph.BFS(2)
    
    