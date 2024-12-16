import time


def part_one():
    moves = [[-1,0], [0,1], [1,0], [0,-1]]
    dirs = ["N", "E", "S", "W"]
    sample = 1
    map = [list(row) for row in (open('sample.txt').read().strip().splitlines() if sample else open('day_6_input.txt').read().strip().splitlines())]
    dir = "N"

    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] in tuple(("<", ">", "v", "^")):
                pos = (i, j)
                break


    travelled_pos = set()
    travelled_pos.add(tuple(pos))

    while (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[pos[0]])):

        curr_move = moves[dirs.index(dir)]

        if map[pos[0]][pos[1]] == ".":
            map[pos[0]][pos[1]] = "X"
            travelled_pos.add(tuple(pos))
        new_y, new_x = pos[0] + curr_move[0], pos[1] + curr_move[1]
        new_dir = dirs[(dirs.index(dir) + 1) % 4]

        if new_y < 0 or new_y >= len(map) or new_x < 0 or new_x >= len(map[0]):
            pos = [new_y, new_x]
            continue
        elif map[new_y][new_x] == "#":
            dir = new_dir
            continue
        pos = [new_y, new_x]
        # print(pos)

    return len(travelled_pos)

def is_valid(map, pos, dir, temp_pos) -> bool:
    dirs = ["^", ">", "v", "<"]
    moves = [[-1,0], [0,1], [1,0], [0,-1]]
    visited = set()

    while (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[pos[0]])):
        curr_move = moves[dirs.index(dir)]
        visited.add((pos[0], pos[1], dir))
        new_y, new_x = pos[0] + curr_move[0], pos[1] + curr_move[1]
        new_dir = dirs[(dirs.index(dir) + 1) % 4]
        if (new_y, new_x, dir) in visited:
            return True

        if new_y < 0 or new_y >= len(map) or new_x < 0 or new_x >= len(map[0]):
            pos = [new_y, new_x]
            continue
        elif map[new_y][new_x] == "#" or (new_y, new_x) == temp_pos:
            dir = new_dir
            continue
        pos = [new_y, new_x]
        # print(pos)

    return False


def part_two():
    moves = [[-1,0], [0,1], [1,0], [0,-1]]
    dirs = ["^", ">", "v", "<"]
    sample = 0
    map = [list(row) for row in (open('sample.txt').read().strip().splitlines() if sample else open('day_6_input.txt').read().strip().splitlines())]

    pos = (0, 0)
    dir = ""
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] in dirs:
                pos = (i, j)
                dir = map[i][j]
                break

    init_pos, init_dir = pos, dir

    travelled_pos = set()
    travelled_pos.add(tuple(pos))

    while (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[pos[0]])):

        curr_move = moves[dirs.index(dir)]

        if map[pos[0]][pos[1]] == ".":
            map[pos[0]][pos[1]] = "X"
            travelled_pos.add(tuple(pos))
        new_y, new_x = pos[0] + curr_move[0], pos[1] + curr_move[1]
        new_dir = dirs[(dirs.index(dir) + 1) % 4]

        if new_y < 0 or new_y >= len(map) or new_x < 0 or new_x >= len(map[0]):
            pos = [new_y, new_x]
            continue
        elif map[new_y][new_x] == "#":
            dir = new_dir
            continue
        pos = [new_y, new_x]
        # print(pos)
    # print(travelled_pos)
    res = 0
    for temp_pos in travelled_pos:
        if is_valid(map, init_pos, init_dir, temp_pos):
            res += 1
    return res

start_time = time.time_ns()
print("answer to part one is", part_one())
print("answer to part two is", part_two())
print(f"Time taken: {time.time_ns() - start_time} nanoseconds = {(time.time_ns() - start_time)/1e+9} seconds")