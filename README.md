# Tree-Based Search Visualization

Pygame visualization of classic AI search algorithms (DFS, BFS, GBFS, A*) on grid maps.

## 📌 Overview
This project demonstrates how different **tree-based search algorithms** explore a map and find paths from a start node to a goal node.  
The program uses **Pygame** for visualization, making the search process easier to understand.

## 🔍 Implemented Algorithms
- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Greedy Best-First Search (GBFS)**
- **A*** (A-Star Search)

## 🎮 Features
- Interactive visualization built with **Pygame**
- Real-time exploration of nodes during the search process
- Highlights visited nodes and the final path
- Modular code structure:
  - `map.py` → grid/map handling
  - `search.py` → search algorithms (DFS, BFS, GBFS, A*)
  - `main.py` → visualization with Pygame

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/phongvunz1406/TreeBasedSearch.git
   ```
2. Install dependencies:
   ```bash
   pip install pygame
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## 📷 Example (Visualization)
<img width="641" height="677" alt="image" src="https://github.com/user-attachments/assets/fd321a52-bd33-4aff-9a55-e114bfd3b6a1" />

## 🎯 Purpose
This project was developed as part of an **Artificial Intelligence exercise** to compare the performance of **uninformed** (DFS, BFS) and **informed** (GBFS, A*) search algorithms.  
The Pygame-based visualization helps learners observe how each algorithm explores the search space.
