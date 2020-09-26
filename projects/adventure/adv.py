
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
# Create new player to start world
player = Player(world.starting_room)


# Dictionary to reverse movement of each direction
convert_direction = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}


# Function to retrieve the number of unexplored exits for a room
def get_number_of_unexplored_paths(room):
    unexplored_exits_count = 0

    for direction in room:
        if room[direction] == "?":
            unexplored_exits_count += 1

    return unexplored_exits_count


# Function to build initial visited dict entry. Ex ouput -> visited[room_id] = { "n": ?, "s": ?, "e": ?, "w": ? }
def build_initial_dict_entry_value(visited, room):
    possible_room_exits = room.get_exits()

    visited[room.id] = {}

    for move in possible_room_exits:
        visited[room.id][move] = "?"


def get_traversal_directions(world, player):
    visited = set()
    directions = []
    backtrack_directions = []
    new_player = Player(player.current_room)
    visited.add(new_player.current_room.id)

    while len(visited) < len(room_graph):
        next_move = None
        for move in new_player.current_room.get_exits():
            if new_player.current_room.get_room_in_direction(move).id not in visited:
                next_move = move
                break

        if next_move is not None:
            directions.append(move)
            backtrack_directions.append(convert_direction[move])
            new_player.travel(move)
            visited.add(new_player.current_room.id)

        else:
            next_move = backtrack_directions.pop()
            new_player.travel(next_move)
            directions.append(next_move)

    return directions


# traversal_path = ['n', 'n']
traversal_path = get_traversal_directions(world, player)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
