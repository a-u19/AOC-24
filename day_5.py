import time
import re

def valid_line(curr_line:list[int], sec1:str) -> bool:
    for i in range(1, len(curr_line)):
        pattern = fr'{curr_line[i]}\|{curr_line[i-1]}'
        if re.search(pattern, sec1):
            return False
    return True

def main(filepath:str) -> int:
    sec1, sec2 = open(filepath).read().split("\n\n")
    res = 0
    for line in sec2.splitlines():
        curr_line = [int(x) for x in line.split(",")]
        if valid_line(curr_line, sec1):
            # print(f"{curr_line} is valid line")
            res += curr_line[len(curr_line)//2]
    return res


def reorder_invalid_line(curr_line:list[int], sec1:str) -> int:
    orig_line = curr_line.copy()
    for i in range(1, len(curr_line)):
        pattern = fr'{curr_line[i]}\|{curr_line[i - 1]}'
        if re.search(pattern, sec1):
            # print(curr_line, pattern, "exists so not a valid line")
            for j in range(i, len(curr_line)):
                curr_line = orig_line.copy()
                curr_line.insert(j, curr_line.pop(i - 1))
                if valid_line(curr_line, sec1):
                    # print("this is a valid line", curr_line)
                    return curr_line[len(curr_line)//2]
                return reorder_invalid_line(curr_line, sec1)
    return 0


def main_part_2(filepath:str) -> int:
    sec1, sec2 = open(filepath).read().split("\n\n")
    res = 0
    for line in sec2.splitlines():
        curr_line = [int(x) for x in line.split(",")]
        # print(res)
        res += reorder_invalid_line(curr_line, sec1)
    return res

start_time = time.time_ns()
# print(f"The answer to part one is {main('sample.txt')}")
print(f"The answer to part one is {main('day_5_input.txt')}")
print(f"The answer to part two is {main_part_2('day_5_input.txt')}")
# print(f"The answer to part two is {main_part_2('sample.txt')}")
print(f"Time taken: {time.time_ns() - start_time} nanoseconds = {(time.time_ns() - start_time)/1e+9} seconds")