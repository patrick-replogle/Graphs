from util import Stack


def earliest_ancestor(ancestors, starting_node):
    # create a dict to store all ancestor nodes
    ancestor_hashmap = {}
    # { key -> node: value -> set of node's direct ancestors }
    for a in ancestors:
        # add all nodes as keys in hashmap
        if a[1] not in ancestor_hashmap:
            ancestor_hashmap[a[1]] = set()
        if a[0] not in ancestor_hashmap:
            ancestor_hashmap[a[0]] = set()
        # then add all edges of nodes to the set
        ancestor_hashmap[a[1]].add(a[0])
    # find all possible paths to oldest ancestors
    paths = find_paths_to_earliest_ancestor(starting_node, ancestor_hashmap)

    # starting_node is the earliest ancestor if no valid paths
    if len(paths) == 0:
        return -1
    # if only one valid path, return the oldest ancestor
    elif len(paths) == 1:
        return paths[0][-1]

    elif len(paths) == 2:
        # longer path of the two will be oldest
        if len(paths[0]) < len(paths[1]):
            return paths[-1][-1]
        # if path lengths are equal, return the smallest value
        elif len(paths[0]) == len(paths[1]):
            if paths[0][-1] < paths[1][-1]:
                return paths[0][-1]
            return paths[1][-1]
    # last value of last path array will be the oldest
    else:
        return paths[-1][-1]


# Depth First Traversal approach to find oldest ancestor paths
def find_paths_to_earliest_ancestor(starting_node, ancestor_hashmap):
    results = []
    visited = set()
    s = Stack()

    s.push([starting_node])

    while s.size() > 0:
        curr_path = s.pop()
        curr_node = curr_path[len(curr_path) - 1]

        if curr_node not in visited:
            # We have a valid path if curr_node has no ancestors
            if len(ancestor_hashmap[curr_node]) == 0 and curr_node != starting_node:
                results.append(curr_path)

            visited.add(curr_node)

            for neighbor in ancestor_hashmap[curr_node]:
                path_copy = list(curr_path)
                path_copy.append(neighbor)
                s.push(path_copy)
    # return all valid paths
    return results


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(ancestors, 8))

# self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
# self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
# self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
# self.assertEqual(earliest_ancestor(test_ancestors, 4), -1)
# # self.assertEqual(earliest_ancestor(test_ancestors, 5), 4)
# self.assertEqual(earliest_ancestor(test_ancestors, 6), 10)
# # self.assertEqual(earliest_ancestor(test_ancestors, 7), 4)
# # self.assertEqual(earliest_ancestor(test_ancestors, 8), 4) ===
# # self.assertEqual(earliest_ancestor(test_ancestors, 9), 4) ===
# self.assertEqual(earliest_ancestor(test_ancestors, 10), -1)
# self.assertEqual(earliest_ancestor(test_ancestors, 11), -1)
