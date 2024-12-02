import time
start_time = time.time()


def is_valid_level(level) -> bool:
    if isinstance(level, str):
        level = [int(num) for num in level.strip("\n").split(" ")]
    # print(level)
    if sorted(level) != level and sorted(level,reverse=True) != level:
        # print(f"Level is not sorted: {level}")
        return False
    for i in range(len(level)-1):
        if abs(level[i+1] - level[i]) >= 4 or level[i+1] - level[i] == 0:
            # print(f"level is {level} and i is {i}")
            return False
    return True


def part_1(file_name:str) -> int:
    all_levels = open(file_name).readlines()
    res = 0
    for level in all_levels:
        if is_valid_level(level):
            res += 1
    return res

def part_2(file_name:str) -> int:
    all_levels = open(file_name).readlines()
    res = 0
    for level in all_levels:
        if is_valid_level(level):
            # print(level)
            res += 1
        else:
            for i in range(len(level)):
                if isinstance(level, str):
                    level = [int(num) for num in level.strip("\n").split(" ")]
                # print(level[:i] + level[i+1:])
                if is_valid_level(level[:i] + level[i+1:]):
                    # print(level)
                    res += 1
                    break
    return res


print(f"The answer to part one is {part_1('day_2_input.txt')}")
print(f"The answer to part two is {part_2('day_2_input.txt')}")
print(f"Time taken is {round(time.time() - start_time,9)}s")