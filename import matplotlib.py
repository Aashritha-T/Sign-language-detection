import matplotlib.pyplot as plt
from collections import deque

def draw_maze(maze, path=None, explored=None):
    """
    Draws the maze with an optional path and explored cells.
    """
    plt.figure(figsize=(6, 6))
    rows, cols = len(maze), len(maze[0])
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:  # Wall
                plt.fill_between([j, j+1], rows-i, rows-i-1, color="black")
            else:  # Path
                plt.fill_between([j, j+1], rows-i, rows-i-1, color="white")
    
    if explored:
        for (x, y) in explored:
            plt.fill_between([y, y+1], rows-x, rows-x-1, color="lightblue")
    
    if path:
        for (x, y) in path:
            plt.fill_between([y, y+1], rows-x, rows-x-1, color="green")
    
    plt.xticks([])
    plt.yticks([])
    plt.show()

def bfs(maze, start, end):
    """
    Solves the maze using BFS and visualizes the process.
    """
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([(start, [start])])
    visited = set([start])
    explored = []

    while queue:
        (x, y), path = queue.popleft()
        explored.append((x, y))
        draw_maze(maze, path=path, explored=explored)

        if (x, y) == end:
            print("BFS Path Found:", path)
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    print("No path found using BFS.")
    return None

def dfs(maze, start, end):
    """
    Solves the maze using DFS and visualizes the process.
    """
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stack = [(start, [start])]
    visited = set([start])
    explored = []

    while stack:
        (x, y), path = stack.pop()
        explored.append((x, y))
        draw_maze(maze, path=path, explored=explored)

        if (x, y) == end:
            print("DFS Path Found:", path)
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))

    print("No path found using DFS.")
    return None

# Example Usage
if __name__ == "__main__":
    # Maze Representation
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)

    print("Choose Algorithm to Solve the Maze:")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")

    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == "1":
        bfs(maze, start, end)
    elif choice == "2":
        dfs(maze, start, end)
    else:
        print("Invalid choice!")
