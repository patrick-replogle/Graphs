from util import Stack
import math


# Second pass solution utilizing a full graph class
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertext(self, vertext_id):
        if vertext_id not in self.vertices:
            self.vertices[vertext_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def get_oldest_ancestor(self, starting_node):
        s = Stack()
        visited = set()
        s.push([starting_node])

        oldest_ancestor = -1
        longest_path = 0

        while s.size() > 0:
            curr_path = s.pop()
            curr_node = curr_path[-1]

            if len(curr_path) > longest_path and curr_node != starting_node:
                longest_path = len(curr_path)
                oldest_ancestor = curr_node

            if curr_node not in visited:
                visited.add(curr_node)

                for neighbor in self.get_neighbors(curr_node):
                    path_copy = list(curr_path)
                    path_copy.append(neighbor)
                    s.push(path_copy)

        return oldest_ancestor


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for a in ancestors:
        g.add_vertext(a[0])
        g.add_vertext(a[1])
        g.add_edge(a[1], a[0])

    return g.get_oldest_ancestor(starting_node)


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(ancestors, 1))  # -> 10
print(earliest_ancestor(ancestors, 2))  # -> -1
print(earliest_ancestor(ancestors, 3))  # -> 10
print(earliest_ancestor(ancestors, 4))  # -> -1
print(earliest_ancestor(ancestors, 5))  # -> 4
print(earliest_ancestor(ancestors, 6))  # -> 10
print(earliest_ancestor(ancestors, 7))  # -> 4
print(earliest_ancestor(ancestors, 8))  # -> 4
print(earliest_ancestor(ancestors, 9))  # -> 4
print(earliest_ancestor(ancestors, 10))  # -> -1
print(earliest_ancestor(ancestors, 11))  # -> -1
