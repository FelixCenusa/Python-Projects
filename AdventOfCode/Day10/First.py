p_i = open("/root/dbwebb-kurser/python/me/000-Personal/AdventOfCode/Day10/puzzle_input.txt","r")
from_where = "null"

def find_starting_point(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                print("Found S proof:",maze[i][j+1])
                return (i, j+1)

def is_valid_move(maze, visited, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and not visited[row][col] and maze[row][col] != '.'

def dfs(maze, visited, row, col, distance):
    if not is_valid_move(maze, visited, row, col):
        return distance

    visited[row][col] = True
    if maze[row][col] == '|':
        if from_where == "up":
            moves = [(-1, 0)]
        if from_where == "down":
            moves = [(1, 0)]

    
    elif maze[row][col] == '-':
        moves = [(0, 1), (0, -1)]
        if from_where == "up":
            moves = [(-1, 0)]
            from_where = "up"
        if from_where == "down":
            moves = [(1, 0)]
    elif maze[row][col] == 'L':
        moves = [(-1, 0), (0, 1)]
        if from_where == "up":
            moves = [(-1, 0)]
        if from_where == "down":
            moves = [(1, 0)]
    elif maze[row][col] == 'J':
        moves = [(-1, 0), (0, -1)]
        if from_where == "up":
            moves = [(-1, 0)]
        if from_where == "down":
            moves = [(1, 0)]
    elif maze[row][col] == '7':
        moves = [(1, 0), (0, -1)]
        if from_where == "up":
            moves = [(-1, 0)]
        if from_where == "down":
            moves = [(1, 0)]
    elif maze[row][col] == 'F':
        moves = [(1, 0), (0, 1)]
        if from_where == "up":
            moves = [(-1, 0)]
        if from_where == "down":
            moves = [(1, 0)]
    else:
        moves = []
    max_distance = distance
    for move in moves:
        row, col = row + move[0], col + move[1]
        max_distance = max(max_distance, dfs(maze, visited, row, col, distance + 1))

    visited[row][col] = False
    return max_distance

def find_farthest_point(maze):
    start_row, start_col = find_starting_point(maze)
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    return dfs(maze, visited, start_row, start_col, 0)

# Example usage:
maze = []
line = "lol"
while line != "":
    line = p_i.readline()
    maze.append(line)

result = find_farthest_point(maze)
print(result)


