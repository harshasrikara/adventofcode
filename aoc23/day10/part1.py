import sys

def parse(file: str):
    maze = []
    for line in file.readlines():
        line = line.strip('\n')
        print(line)

        line = [l for l in line]

        maze.append(line)

    return maze

def get_start_index(maze: list[list[str]]) -> [int, int]:
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return i,j

def get_next_step(maze: list[list[str]], i: int, j: int, prev_i: int, prev_j: int) -> [int, int]:

    step_1 = []
    step_2 = []

    key = maze[i][j]
    if key == "S":
        key = "F"
    
    if key == "F":
        step_1 = [i+1, j]
        step_2 = [i, j+1]
    
    if key == "7":
        step_1 = [i+1, j]
        step_2 = [i, j-1]

    if key == "J":
        step_1 = [i-1, j]
        step_2 = [i, j-1]

    if key == "L":
        step_1 = [i-1, j]
        step_2 = [i, j+1]

    if key == "|":
        step_1 = [i+1, j]
        step_2 = [i-1, j]
    
    if key == "-":
        step_1 = [i, j+1]
        step_2 = [i, j-1]
    
    if step_1 == [prev_i, prev_j]:
        return step_2
    
    return step_1

def traverse(maze: list[list[str]], prev_i: int, prev_j: int):
    i, j = get_start_index(maze)
    iterations = 1

    curr_i, curr_j = i, j
    next_i, next_j = get_next_step(maze, curr_i, curr_j, prev_i, prev_j)

    curr_i = next_i
    curr_j = next_j

    while(curr_i != i or curr_j != j):
        n_i, n_j = get_next_step(maze, next_i, next_j, curr_i, curr_j)
        iterations = iterations + 1

        curr_i = next_i
        curr_j = next_j

        next_i = n_i
        next_j = n_j
    
    return iterations

def main() -> int:
    f = open("/Users/harshasrikara/aoc23/day10/input.txt")

    maze = parse(f)

    # S is actually over an F
    print(traverse(maze, 43, 8))
    
    return 0


if __name__ == '__main__':
    sys.exit(main())