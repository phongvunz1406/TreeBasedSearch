import re

class Map:
    def __init__(self, filename):
        self.grid_size, self.initial_state, self.goal_states, self.walls = self.map_info(filename)
        self.validate_position()
        self.wall_set = self.make_wall_set()   # corrected
        self.path_set = self.make_path_set(self.grid_size, self.wall_set)  # corrected

    def map_info(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Get grid size (rows, cols)
            grid_size = tuple(map(int, lines[0].strip()[1:-1].split(',')))

            # Get initial state 
            initial_state = tuple(map(int, lines[1].strip()[1:-1].split(',')))

            # Get goal states
            goal_states = []
            for coord in lines[2].strip().split('|'):
                coord_clean = coord.strip()[1:-1]
                points = coord_clean.split(',')
                coord_tuple = tuple(map(int, points))
                goal_states.append(coord_tuple)

            # Get walls (x,y,w,h)
            walls = []
            for coord in lines[3:]:
                coord_clean = coord.strip()[1:-1]
                points = coord_clean.split(',')
                coord_tuple = tuple(map(int, points))
                walls.append(coord_tuple)

        return grid_size, initial_state, goal_states, walls

    def validate_position(self):
        rows, cols = self.grid_size

        # Validate initial state
        if not (0 <= self.initial_state[0] < cols and 0 <= self.initial_state[1] < rows):
            raise ValueError(f'Initial state {self.initial_state} is out of bounds!')

        # Validate goal states
        for goal_state in self.goal_states:
            if not (0 <= goal_state[0] < cols and 0 <= goal_state[1] < rows):
                raise ValueError(f'Goal state {goal_state} is out of bounds!')

        # Validate walls
        for wall in self.walls:
            x, y, w, h = wall
            if not (0 <= x < cols and 0 <= y < rows):
                raise ValueError(f'Wall {wall} is out of bounds!')

    def make_wall_set(self):
        wall_set = set()
        for x, y, w, h in self.walls:
            for i in range(w):
                for j in range(h):
                    wall_set.add((x+i, y+j))
        return wall_set

    def make_path_set(self, grid_size, wall_set):
        rows, cols = grid_size
        path_set = set()
        for x in range(cols):
            for y in range(rows):
                if (x, y) not in wall_set:
                    path_set.add((x, y))
        return path_set
    
    def get_neighbors(self,position):
        x,y = position
        potential_moves =[
            (x, y - 1),   # Up
            (x - 1, y),   # Left
            (x, y + 1),   # Down
            (x + 1, y),   # Right
        ]

        valid_move = []
        for move in potential_moves:
            if move in self.path_set:
                valid_move.append(move)
        return valid_move


