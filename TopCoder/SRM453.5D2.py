# SRM453.5D2 MazeMaker

# dfs보다 bfs가 더 효율적
def dfs(x, y, cnt):
    global ans
    if 0 > x or x >= len(maze) or 0 > y or y >= len(maze[0]) or maze[x][y] == 'X':
        return
    else:
        maze[x][y] = 'X'
        maze_min[x][y] = min(maze_min[x][y], cnt)

    for i in range(len(moveRow)):
        dfs(x+moveRow[i], y+moveCol[i], cnt+1)
    maze[x][y] = '.'


# maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
# startRow = 0
# startCol = 1
# moveRow = [1, 0, -1, 0]
# moveCol = [0, 1, 0, -1]

# maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
# startRow = 0
# startCol = 1
# moveRow = [1, 0, -1, 0, 1, 1, -1, -1]
# moveCol = [0, 1, 0, -1, 1, -1, 1, -1]

# maze = [['X', '.', 'X'], ['.', '.', '.'], ['X', 'X', 'X'], ['X', '.', 'X']]
# startRow = 0
# startCol = 1
# moveRow = [1, 0, -1, 0]
# moveCol = [0, 1, 0, -1]

# maze = [['.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', '.'], ['X', 'X', 'X', '.', '.', '.', 'X'],
#         ['.', '.', '.', '.', 'X', '.', '.'], ['X', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.']]
# startRow = 5
# startCol = 0
# moveRow = [1, 0, -1, 0, -2, 1]
# moveCol = [0, -1, 0, 1, 3, 0]

# maze = [['.', '.', '.', '.', '.', '.', '.']]
# startRow = 0
# startCol = 0
# moveRow = [1, 0, 1, 0, 1, 0]
# moveCol = [0, 1, 0, 1, 0, 1]

maze = [['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.']]
startRow = 0
startCol = 0
moveRow = [2, 0, -2, 0]
moveCol = [0, 2, 0, -2]

maze_min = []
for i in range(len(maze)):
    maze_min.append([])
    for j in range(len(maze[0])):
        if maze[i][j] == '.':
            maze_min[i].append(float('inf'))
        else:
            maze_min[i].append(0)

dfs(startRow, startCol, 0)
ans = max([max(n) for n in maze_min])
if ans == float('inf'):
    print(-1)
else:
    print(ans)
