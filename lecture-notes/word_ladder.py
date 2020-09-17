import string

word_set = set()

# read file and add each word to a set
with open("words.txt", "r") as f:
    for word in f:
        word_set.add(word.strip().lower())

# non-optimized queue to use BFS word search


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# BFS graph function used to find word path without actually using a graph


def BFS_find_word(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        curr_word = path[-1]

        if curr_word not in visited:
            visited.add(curr_word)

            if curr_word == end_word:
                return path

            for neighbor in get_neighbors(curr_word):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None

# helper function to find a words neighbor words


def get_neighbors(word):
    neighbors = []

    word_letters = list(word)

    for i in range(len(word_letters)):
        # import from string to access all 26 alphabet chars
        for letter in list(string.ascii_lowercase):
            # make copy of the word
            word_copy = list(word)
            # substitute the letter into the word copy
            word_copy[i] = letter
            # make the word a string
            word_str = "".join(word_copy)
            # search in word_set for word
            if word_str != word and word_str in word_set:
                neighbors.append(word_str)

    return neighbors


print(BFS_find_word("sail", "boat"))
