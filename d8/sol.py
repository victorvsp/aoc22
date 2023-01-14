
class Tree:
    def __init__(self, height):
        self.height = height
        self.max_top = -1
        self.max_bottom = -1
        self.max_left = -1
        self.max_right = -1

        self.view_top = 0
        self.view_bottom = 0
        self.view_left = 0
        self.view_right = 0

    def __repr__(self):
        return str(self.scenicScore())

    def isVisible(self):
        return self.height > min(self.max_top,
                                self.max_bottom,
                                self.max_left,
                                self.max_right)
    def scenicScore(self):
        return self.view_bottom*self.view_left*self.view_right*self.view_top

def solutionPartOne(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])

    # Compute max_top
    for j in range(grid_width):
        for i in range(1, grid_height):
            grid[i][j].max_top = max(grid[i-1][j].height, grid[i-1][j].max_top)

    # Compute max_bottom
    for j in range(grid_width):
        for i in range(grid_height-2, -1, -1):
            grid[i][j].max_bottom = max(grid[i+1][j].height, grid[i+1][j].max_bottom)
    
    # Compute max_left
    for i in range(grid_height):
        for j in range(1,grid_width):
            grid[i][j].max_left = max(grid[i][j-1].height, grid[i][j-1].max_left)

    # Compute max_right
    for i in range(grid_height):
        for j in range(grid_width-2,-1,-1):
            grid[i][j].max_right = max(grid[i][j+1].height, grid[i][j+1].max_right)

    print(sum(sum(int(tree.isVisible()) for tree in row) for row in grid))


def viewLenght(grid, position, direction):
    grid_height = len(grid)
    grid_width = len(grid[0])
    starting_tree = grid[position[0]][position[1]]
    view_length = 0
    (i,j) = (position[0] + direction[0], position[1] + direction[1]) 
    while i >= 0 and i < grid_height and j >= 0 and j < grid_width:
        view_length += 1
        if grid[i][j].height >= starting_tree.height:
            break
        i += direction[0]
        j += direction[1]
    return view_length

    

def solutionPartTwo(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    for i in range(grid_height):
        for j in range(grid_width):
            tree = grid[i][j]
            tree.view_top = viewLenght(grid, (i,j), (-1,0))
            tree.view_bottom = viewLenght(grid, (i,j), (1,0))
            tree.view_left = viewLenght(grid, (i,j), (0,-1))
            tree.view_right = viewLenght(grid, (i,j), (0,1))

    print(max(max(int(tree.scenicScore()) for tree in row) for row in grid))


##### Main #####

grid = []
with open("input.txt", "r") as input_file:
    for line in input_file:
        tree_list = [Tree(int(c)) for c in line.strip()]
        grid.append(tree_list)

solutionPartOne(grid)
solutionPartTwo(grid)                                                