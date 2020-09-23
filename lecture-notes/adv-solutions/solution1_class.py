from player import Player


class Graph:
    def __init__(self, starting_room, maze, maze_length):
        self.player = Player(starting_room)
        self.maze = maze
        self.maze_length = maze_length
        self.visited = {}
        self.final_directions = []
        self.reverse_directions = []

    def get_current_exits(self):
        return self.player.current_room.get_exits()

    def get_visited_length(self):
        return len(self.visited)

    def get_maze_length(self):
        return self.maze_length

    def get_current_room(self):
        return self.player.current_room

    def get_current_room_id(self):
        return self.player.current_room.id

    def get_final_directions(self):
        return self.final_directions

    def move_player(self, direction):
        self.player.travel(direction)

    def convert_direction(self, direction):
        if direction == "n":
            return "s"
        if direction == "s":
            return "n"
        if direction == "w":
            return "e"
        if direction == "e":
            return "w"

    def get_number_of_unexplored_paths(self, room):
        exits_left = 0

        for direction in room:
            if room[direction] == "?":
                exits_left += 1

        return exits_left

    def build_initial_dict_entry_value(self, room):
        exits = room.get_exits()

        self.visited[room.id] = {}

        for move in exits:
            self.visited[room.id][move] = "?"

    def get_traversal_directions(self):
        # Create an entry for the starting room in the visited dict
        self.build_initial_dict_entry_value(
            self.get_current_room())
        # Loop will run until all rooms have been visited
        while self.get_visited_length() < self.get_maze_length():
            # Loop thru available exits in current room
            for move in self.get_current_exits():
                # If exit is unexplored
                if self.visited[self.get_current_room_id()][move] == "?":
                    # Store current room id to fill in visited[next_room_id] = { reverse_of_move : prev_room_id }
                    prev_room_id = self.get_current_room_id()
                    # Store the opposite of each movement in reverse_directions array to simplify backtracking
                    backtrack_move = self.convert_direction(move)
                    # Move player
                    self.move_player(move)
                    # Append the opposite of the move to reverse_directions arr
                    self.final_directions.append(move)
                    # Append the actual move into the final_directions arr
                    self.reverse_directions.append(
                        self.convert_direction(move))
                    # Replace the question mark at visited[prev_room_id] = { move: new_room_id }
                    self.visited[prev_room_id][move] = self.get_current_room_id()
                    # Check if the new room has been visited already
                    if self.get_current_room_id() not in self.visited:
                        # If not, create an entry for it in the visited dict and then break out of loop
                        self.build_initial_dict_entry_value(
                            self.get_current_room())
                        self.visited[self.get_current_room_id(
                        )][backtrack_move] = prev_room_id
                        break

            # If there are no unexplored exits in the current room, it's time to backtrack to a room with unexplored exits
            if self.get_number_of_unexplored_paths(self.visited[self.get_current_room_id()]) == 0 and self.get_visited_length() < self.get_maze_length():
                # Last element of backtrack_array will be next move
                backtrack_move = self.reverse_directions.pop()
                # Move player back to the previous room
                self.move_player(backtrack_move)
                # Append the backtrack move to the final_directions arr
                self.final_directions.append(backtrack_move)
        # Return final directions array
        return self.get_final_directions()
