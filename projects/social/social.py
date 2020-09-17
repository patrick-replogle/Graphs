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

    def __str__(self):
        return f"{self.name}"


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
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_friendships(self, user_id):
        if user_id in self.friendships:
            return self.friendships[user_id]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
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
                while len(self.friendships[user_id]) < 2:
                    random_id = random.randint(1, num_users)

                    if random_id not in self.friendships[user_id] and user_id != random_id:
                        self.add_friendship(user_id, random_id)
        else:
            print("Number of users must be larger that number of friendship links")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        if len(self.friendships) > 0:
            # Store all network connection paths in a dictionary
            # {key -> friend_id, value -> [shortest friendship path between friend and user_id]}
            results = {}
            # Iterate thru social network
            for user in self.users:
                # Ignore the user that was passed into the function
                if user != user_id:
                    # BFS to find shortest path of connections to get back to the user_id
                    q = Queue()
                    visited = set()

                    q.enqueue([user])

                    while q.size() > 0:
                        curr_path = q.dequeue()
                        curr_user = curr_path[-1]

                        if curr_user not in visited:
                            if curr_user == user_id:
                                results[user] = curr_path

                            visited.add(curr_user)

                            for friend in self.get_friendships(curr_user):
                                path_copy = curr_path[:]
                                path_copy.append(friend)
                                q.enqueue(path_copy)

            return results

        else:
            print("There are currently no social paths in the network")


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("\n")
    print("Friendships: ", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("\n")
    print("Connections:", connections)
    print("\n")
