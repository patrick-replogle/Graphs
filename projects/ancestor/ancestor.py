from util import Stack


def earliest_ancestor(ancestors, starting_node):
    # create a dict to store all nodes and their immediate neighbors
    ancestor_hashmap = {}

    for a in ancestors:
        if a[1] not in ancestor_hashmap:
            ancestor_hashmap[a[1]] = set()
        if a[0] not in ancestor_hashmap:
            ancestor_hashmap[a[0]] = set()
            ancestor_hashmap[a[1]].add(a[0])
        else:
            ancestor_hashmap[a[1]].add(a[0])

    paths = find_ancestors(starting_node, ancestor_hashmap)
    print(paths)

    if len(paths) == 1:
        if paths[0][-1] == starting_node:
            return -1
        else:
            return paths[0][-1]

    elif len(paths) == 2:
        if len(paths[0]) < len(paths[1]):
            return paths[-1][-1]
        elif len(paths[0]) == len(paths[1]):
            if paths[0][-1] < paths[1][-1]:
                return paths[0][-1]
            return paths[1][-1]

    elif len(paths) > 2:
        return paths[-1][-1]


def find_ancestors(starting_vertex, dict):
    s = Stack()
    s.push([starting_vertex])
    results = []

    visited = set()

    while s.size() > 0:

        curr_path = s.pop()

        curr_vertex = curr_path[len(curr_path) - 1]

        if curr_vertex not in visited:
            if len(dict[curr_vertex]) == 0:
                results.append(curr_path)

            visited.add(curr_vertex)

            for neighbor in dict[curr_vertex]:
                arr = curr_path[:]
                arr.append(neighbor)
                s.push(arr)

    return results


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(ancestors, 6))

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
