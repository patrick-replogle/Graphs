import random


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


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User: {self.name}>"


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_users(self):
        return self.users

    def get_friendships(self, user_id):
        if user_id in self.friendships:
            return self.friendships[user_id]

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph2(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()
        # random names to populate network with
        first_names = ["John", "Frank", "George", "Jane", "Bruce", "Patrick", "James",
                       "Superman", "Betty", "Wilma", "Michael", "Barney", "Spiderman"]

        last_names = ["Miller", "Wayne", "Rubble", "Doe", "McVey",
                      "Gonzalez", "Replogle", "Franco", "Rae", "Espinosa"]

        if num_users > avg_friendships:
            # Add users
            for _ in range(num_users):
                random_user_name = (random.choice(
                    first_names) + " " + random.choice(last_names))

                self.add_user(random_user_name)

            # Create friendships
            for user_id in self.users:
                # repeat until user has at least avg_friendships
                while len(self.friendships[user_id]) < avg_friendships:
                    random_id = random.randint(1, num_users)

                    if random_id not in self.friendships[user_id] and user_id != random_id:
                        self.add_friendship(user_id, random_id)
        else:
            print("Number of users must be larger that number of friendship links")

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        for i in range(num_users):
            self.add_user(f"User {i}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

    def populate_graph3(self, num_users, avg_friendships):
        def randomize(arr, n):
            # Start from the last element and swap one by one. We don't
            # need to run for the first element that's why i > 0
            for i in range(n-1, 0, -1):
                # Pick a random index from 0 to i
                j = random.randint(0, i+1)
                # Swap arr[i] with the element at random index
                arr[i], arr[j] = arr[j], arr[i]
            return arr

        for i in range(num_users):
            self.add_user(i)

        all_friend_combos = []
        for person in range(1, num_users):
            for friend in range(person + 1, num_users + 1):
                all_friend_combos.append((person, friend))

        shuffled_combos = randomize(all_friend_combos, len(all_friend_combos))

        total_friendships = num_users * avg_friendships
        elements_needed = total_friendships // 2
        combos_to_make = shuffled_combos[:elements_needed]

        for friendship in combos_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        if len(self.friendships) > 0:
            visited = {}
            q = Queue()
            q.enqueue([user_id])

            while q.size() > 0:
                curr_path = q.dequeue()
                curr_vertex = curr_path[-1]

                if curr_vertex not in visited:
                    visited[curr_vertex] = curr_path

                    for friend in self.friendships[curr_vertex]:
                        path_copy = curr_path[:]
                        path_copy.append(friend)
                        q.enqueue(path_copy)

            return visited

        else:
            print("There are currently no friendship paths in the network")


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("\n")
    print("Friendships: ", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("\n")
    print("Connections:", connections)
    print("\n")
