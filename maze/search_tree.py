
from df_maze import Maze, Cell

path = []# Contains the path back to the start once the goal is reached

class Node:

    # Adds current node to path then recurses with parent node until
    # the first node is reached.
    def addNodeToPath(self):
        path.append(self.cell)

        if self.root != None:# if parent is is null, the first node has been reached
            self.root.addNodeToPath()
        

    def __init__(self, maze: Maze, cell: Cell, root):

        self.root = root
        self.cell = cell

        # Contains the Cells surrounding current cell.
        # Will remain null is a wall blocks path to next cell.
        self.north = None
        self.south = None
        self.east = None
        self.west = None

        # Prevent a cell from being visited more than once
        self.cell.visited = True

        # If the current cell is the goal, mark the path to the goal.
        if self.cell.x == maze.nx -1 and self.cell.y == maze.ny -1:
            self.addNodeToPath()
            print("Goal has been found")
            return
    
        newNorth = None
        # If the cell is not blocked by a wall and it hasn't been visited,
        # search the adjacent node.
        if not cell.walls['N'] and not maze.cell_at(cell.x, cell.y - 1).visited:
            newNorth = maze.cell_at(cell.x, cell.y - 1)
            self.north = Node(maze, newNorth, self)

        newSouth = None
        if not cell.walls['S'] and not maze.cell_at(cell.x, cell.y + 1).visited:
            newSouth = maze.cell_at(cell.x, cell.y + 1)
            self.south = Node(maze, newSouth, self)

        newWest = None
        if not cell.walls['W'] and not maze.cell_at(cell.x - 1, cell.y).visited:
            newWest = maze.cell_at(cell.x - 1, cell.y)
            self.west = Node(maze, newWest, self)

        newEast = None
        if not cell.walls['E'] and not maze.cell_at(cell.x + 1, cell.y ).visited:
            newEast = maze.cell_at(cell.x + 1, cell.y)
            self.east = Node(maze, newEast, self)
    



class SearchTree:
    # Takes a maze and starts the depth-first search
    def __init__(self, maze: Maze):
        self.maze = maze
        self.head = Node(self.maze, self.maze.cell_at(0, 0), None)

    #Reaturn the list of nodes that lead to the goal.
    def getPath(self):
        return path
        

