from gui import *
def main():
    # Define available maps and algorithms
    maps = ["map1.txt", "map2.txt", "map3.txt", "map4.txt"] 
    algorithms = ["DFS", "BFS", "GBFS", "Astar"]

    # Create an instance of the MainScreen
    main_screen = MainScreen(maps, algorithms)

    # Run the main screen loop
    main_screen.run()

    # Exit the program
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()