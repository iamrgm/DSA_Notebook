# Python3 Program to print BFS traversal
from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):

        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Driver code

# Create a graph
grph = Graph()
grph.addEdge(0, 1)
grph.addEdge(0, 2)
grph.addEdge(1, 2)
grph.addEdge(2, 0)
grph.addEdge(2, 3)
grph.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
grph.BFS(2)