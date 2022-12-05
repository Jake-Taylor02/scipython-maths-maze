from df_maze import Maze
from search_tree import SearchTree

# Maze dimensions (ncols, nrows)
nx, ny = 15, 15
# Maze entry position
##ix, iy = 0, 0

#maze = Maze(nx, ny, ix, iy)
maze = Maze(nx, ny)
maze.add_begin_end = True
maze.add_treasure = False
maze.make_maze()


dfs = SearchTree(maze)
myPath = dfs.getPath()

#print(maze)

# Draw maze to file
maze.write_svg('maze.svg', myPath)
