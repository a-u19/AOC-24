import time
start_time = time.time()


def is_valid_level(level:str) -> bool:
    level = [int(num) for num in level.split(" ")]
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


print(f"The answer to part one is {part_1('day_2_input.txt')}")
print(f"Time taken is {round(time.time() - start_time,9)}s")