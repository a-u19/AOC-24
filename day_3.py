import time
start_time = time.time_ns()
import re


def part_1(inp_str:str) -> int:
    regex = r'mul\(\d*,\d*\)'
    matches = re.findall(regex,inp_str)
    res = 0
    for match in matches:
        nums = match[4:-1].split(",")
        res += int(nums[0]) * int(nums[1])
    return res


def part_2(inp_str:str) -> int:
    regex = r'do(?:n\'t)?\(\)|mul\(\d*,\d*\)'
    matches = re.findall(regex,inp_str)
    res = 0
    do = True
    for match in matches:
        # print(match)
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        if do and match[:3] == "mul":
            nums = match[4:-1].split(",")
            # print(nums)
            res += int(nums[0]) * int(nums[1])
    return res


inp_str = "".join(line for line in open('day_3_input.txt').readlines())
print(f"The answer to part one is {part_1(inp_str)}")
print(f"The answer to part two is {part_2(inp_str)}")
print(f"Time taken is {time.time_ns() - start_time} nanoseconds = {(time.time_ns() - start_time)/1e+9} seconds")