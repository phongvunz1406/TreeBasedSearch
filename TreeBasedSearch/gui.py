import pygame
import sys 
import time
from search import bfs,dfs,a_star_search,greedy_best_first_search
from map import Map

class MainScreen:
    def __init__(self, maps, algorithms):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 625))
        pygame.display.set_caption("Robot Navigation Program")
        self.clock = pygame.time.Clock()

        self.maps = maps  # List of maps
        self.algorithms = algorithms  # List of algorithms

        self.selected_map = None
        self.selected_algorithm = None

        # Button positions and sizes
        self.map_buttons = self.create_buttons(maps, (50, 50), (100, 30))
        self.algorithm_buttons = self.create_buttons(algorithms, (350, 50), (200, 30))

    def create_buttons(self, labels, start_pos, size):
        buttons = []
        x, y = start_pos
        for label in labels:
            rect = pygame.Rect(x, y, size[0], size[1])
            buttons.append((label, rect))
            y += size[1] + 10
        return buttons

    def draw_buttons(self, buttons):
        for label, rect in buttons:
            pygame.draw.rect(self.screen, (0, 0, 255), rect)  # Blue buttons
            font = pygame.font.Font(None, 24)
            text = font.render(label, True, (255, 255, 255))
            self.screen.blit(text, (rect.x + 10, rect.y + 5))

    def get_button_click(self, buttons, pos):
        for label, rect in buttons:
            if rect.collidepoint(pos):
                return label
        return None

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Black background

            # Draw buttons
            self.draw_buttons(self.map_buttons)
            self.draw_buttons(self.algorithm_buttons)

            font = pygame.font.Font(None, 36)
            if self.selected_map:
                map_text = font.render(f"Selected Map: {self.selected_map}", True, (255, 255, 255))
                self.screen.blit(map_text, (300, 300))

            if self.selected_algorithm:
                alg_text = font.render(f"Selected Algorithm: {self.selected_algorithm}", True, (255, 255, 255))
                self.screen.blit(alg_text, (300, 350))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # Check if map or algorithm is selected
                    selected_map = self.get_button_click(self.map_buttons, pos)
                    selected_algorithm = self.get_button_click(self.algorithm_buttons, pos)

                    if selected_map:
                        self.selected_map = selected_map
                    if selected_algorithm:
                        self.selected_algorithm = selected_algorithm

                    # If both map and algorithm are selected, proceed
                    if self.selected_map and self.selected_algorithm:
                        self.run_search(self.selected_map, self.selected_algorithm)
                        return  # Exit the main screen loop after selection

            self.clock.tick(60)

    def run_search(self, map_name, algorithm_name):
        print(f"Running search on {map_name} using {algorithm_name}...")
        map_obj = Map(map_name)  # Load the selected map

        if algorithm_name == "DFS":
            path = dfs(map_obj)
        elif algorithm_name == "BFS":
            path = bfs(map_obj)
        elif algorithm_name == "GBFS":
            path = greedy_best_first_search(map_obj)
        elif algorithm_name == "Astar":
            path = a_star_search(map_obj)

        
        visited_nodes = []  

        # Run the visualizer
        visualizer = Visualizer(map_obj)
        visualizer.run(visited_nodes, path)

        

class Visualizer:
    def __init__(self, map_obj):
        pygame.init()
        self.map = map_obj
        self.cell_size = 50
        self.screen_height = self.map.grid_size[0] * self.cell_size
        self.screen_width = self.map.grid_size[1] * self.cell_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("104486950_COS30019_Assignment01")

    def draw_grid(self):
        for x in range(0, self.screen_width, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (self.screen_width, y))

    def draw_static_map(self):
        # Fill background with white
        self.screen.fill((255, 255, 255))
        self.draw_grid()

        # Draw grey walls
        for wall_x, wall_y in self.map.wall_set:
            pygame.draw.rect(self.screen, (127, 127, 127), 
                             (wall_x * self.cell_size, wall_y * self.cell_size, self.cell_size, self.cell_size))

        # Draw goal states in green
        for goal_x, goal_y in self.map.goal_states:
            pygame.draw.rect(self.screen, (0, 255, 0), 
                             (goal_x * self.cell_size, goal_y * self.cell_size, self.cell_size, self.cell_size))

        # Draw the initial state as a red square
        init_x, init_y = self.map.initial_state
        pygame.draw.rect(self.screen, (255, 0, 0), 
                         (init_x * self.cell_size, init_y * self.cell_size, self.cell_size, self.cell_size))

        pygame.display.flip()

    def draw_node(self, position, color):
        x, y = position
        pygame.draw.rect(self.screen, color, 
                         (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        pygame.display.flip()

    def run(self, explored_cells, solution_path):
        self.draw_static_map()
        explored_index = 0
        path_index = 0
        drawing_path = False
        running = True
        initial_state = self.map.initial_state  


        while running:
            self.clock.tick(60)  # Limit to 60 FPS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    running = False

            if not drawing_path and explored_index < len(explored_cells):
                # Draw the next explored node
                current_node = explored_cells[explored_index]

                # Ensure the explored node doesn't overwrite the green goal state
                if current_node != initial_state and current_node not in self.map.goal_states:
                    self.draw_node(current_node, (255, 255, 0))  # Yellow
                explored_index += 1

            elif not drawing_path and explored_index >= len(explored_cells):
                # Finished exploring, start drawing the path
                drawing_path = True

            elif drawing_path and path_index < len(solution_path):
                # Draw the next node in the solution path, but skip goal states
                current_path_node = solution_path[path_index]
                if current_path_node != initial_state and current_path_node not in self.map.goal_states:
                    self.draw_node(current_path_node, (0, 0, 255))  # Blue
                path_index += 1

            elif drawing_path and path_index >= len(solution_path):
                # Finished drawing the path
                pass
            time.sleep(0.3)

        pygame.quit()
