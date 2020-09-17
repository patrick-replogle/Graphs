"""
Simple graph implementation
"""
from util import Stack, Queue


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Nonexistant vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("Nonexistent vertex")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        if starting_vertex in self.vertices:
            q = Queue()
            visited = set()

            q.enqueue(starting_vertex)

            while q.size() > 0:
                curr_vert = q.dequeue()

                if curr_vert not in visited:
                    print(curr_vert)
                    visited.add(curr_vert)

                    for neighbor in self.get_neighbors(curr_vert):
                        q.enqueue(neighbor)
        else:
            print("Nonexistent vertex")

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if starting_vertex in self.vertices:
            s = Stack()
            visited = set()

            s.push(starting_vertex)

            while s.size() > 0:
                curr_vert = s.pop()

                if curr_vert not in visited:
                    print(curr_vert)
                    visited.add(curr_vert)

                    for neighbor in self.get_neighbors(curr_vert):
                        s.push(neighbor)

        else:
            print("Nonexistent vertex")

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enque the PATH TO starting_vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # Create an empty set to track visited verticies
        visited = set()

        # while the queue is not empty:
        while q.size() > 0:
            # get the current vertex PATH (deque from queue)
            curr_path = q.dequeue()
            # set the current vertex to the LAST elememnt of the PATH
            curr_vertex = curr_path[len(curr_path) - 1]
            # Check if the current vertex has not been visited:
            if curr_vertex not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION:
                if curr_vertex == destination_vertex:
                    # IF IT IS, STOP AND RETURN
                    return curr_path
                # Mark the current vertex as visited
                visited.add(curr_vertex)
                # Queue up NEW Paths with each neighbor
                for neighbor in self.get_neighbors(curr_vertex):
                    # take current path
                    arr = curr_path[:]
                    # append the neighbor to it
                    arr.append(neighbor)
                    # queue up NEW path
                    q.enqueue(arr)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push the PATH TO starting_vertex
        s = Stack()
        s.push([starting_vertex])
        # Create an empty set to track visited verticies
        visited = set()

        # while the stack is not empty:
        while s.size() > 0:
            # get the current vertex PATH (pop from stack)
            curr_path = s.pop()
            # set the current vertex to the LAST elememnt of the PATH
            curr_vertex = curr_path[len(curr_path) - 1]
            # Check if the current vertex has not been visited:
            if curr_vertex not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION:
                if curr_vertex == destination_vertex:
                    # IF IT IS, STOP AND RETURN
                    return curr_path
                # Mark the current vertex as visited
                visited.add(curr_vertex)
                # Push NEW Paths with each neighbor onto stack
                for neighbor in self.get_neighbors(curr_vertex):
                    # take current path
                    arr = curr_path[:]
                    # append the neighbor to it
                    arr.append(neighbor)
                    # push NEW path to stack
                    s.push(arr)

    # third pass solution
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None and path is None:
            visited = set()
            path = []

        visited.add(starting_vertex)
        path = list(path)
        path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(path[-1]):
            if neighbor not in visited:
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)

                if new_path is not None:
                    return new_path

        return None

    # second pass solution
    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     if visited is None:
    #         visited = set()
    #         starting_vertex = [starting_vertex]

    #     curr_vertex = starting_vertex[-1]

    #     if curr_vertex == destination_vertex:
    #         return starting_vertex

    #     if curr_vertex not in visited:
    #         visited.add(curr_vertex)

    #         for neighbor in self.get_neighbors(curr_vertex):
    #             starting_vertex.append(neighbor)

    #             path = self.dfs_recursive(
    #                 starting_vertex, destination_vertex, visited)

    #             if path is not None:
    #                 return path

    #             starting_vertex.pop()

    # first pass solution
    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     if visited is None:
    #         visited = set()
    #         starting_vertex = [starting_vertex]

    #     curr_vertex = starting_vertex[len(starting_vertex) - 1]

    #     if curr_vertex == destination_vertex:
    #         return starting_vertex

    #     if curr_vertex not in visited:
    #         visited.add(curr_vertex)

    #         arr = []
    #         for neighbor in self.get_neighbors(curr_vertex):
    #             arr = starting_vertex[:]
    #             arr.append(neighbor)
    #         return self.dfs_recursive(arr, destination_vertex, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("bft")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''

    print("dft")
    graph.dft(1)

    print("dft recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS")
    print(graph.dfs(1, 6))
    print("DFS Rescursive")
    print(graph.dfs_recursive(1, 6))
