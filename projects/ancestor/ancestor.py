from util import Stack


# First pass solution utilizing graph-like structure without an actual graph class
def earliest_ancestor(ancestors, starting_node):
    # create a hashmap to store all nodes
    ancestor_hashmap = {}
    # { key -> node: value -> set of node's direct ancestors }
    for a in ancestors:
        if a[1] not in ancestor_hashmap:
            ancestor_hashmap[a[1]] = set()
        if a[0] not in ancestor_hashmap:
            ancestor_hashmap[a[0]] = set()

        ancestor_hashmap[a[1]].add(a[0])
    # Use DFS helper function to find oldest node or return -1 if starting_node is oldest
    return DFT(starting_node, ancestor_hashmap)


def DFT(starting_node, ancestor_hashmap):
    s = Stack()
    visited = set()
    s.push([starting_node])

    oldest_ancestor = -1
    longest_path = 0

    while s.size() > 0:
        curr_path = s.pop()
        curr_node = curr_path[-1]
        print(curr_node)

        if len(curr_path) > longest_path and curr_node != starting_node:
            longest_path = len(curr_path)
            oldest_ancestor = curr_node

        if curr_node not in visited:
            visited.add(curr_node)

            for neighbor in ancestor_hashmap[curr_node]:
                path_copy = list(curr_path)
                path_copy.append(neighbor)
                s.push(path_copy)

    return oldest_ancestor


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(ancestors, 8))
