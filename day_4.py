import time
start_time = time.time_ns()
import re

def part_1(inp_filepath:str) -> int:
    data = open(inp_filepath).readlines()
    res = 0
    res += check_horizontal(data)
    print(res)
    res += check_diag(data)
    res += check_vert(data)
    return res

def check_horizontal(data:list[str]) -> int:
    horiz_res = 0
    for line in data:
        horiz_res += len(re.findall('XMAS|SAMX',line))

    return horiz_res


def check_diag(data:list[str]) -> int:
    diag_res = 0
    for i in range(len(data) - 3):
        for j in range(len(data[i]) - 3):
            if data[i][j] == "X" and data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
                # print(i,j)
                diag_res += 1
            elif data[i][j] == "S" and data[i+1][j+1] == "A" and data[i+2][j+2] == "M" and data[i+3][j+3] == "X":
                diag_res += 1
            elif data[i][j] == "X" and data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
                diag_res += 1
            elif data[i][j] == "S" and data[i - 1][j - 1] == "A" and data[i - 2][j - 2] == "M" and data[i - 3][
                    j - 3] == "X":
                diag_res += 1
#                 print(i,j)
    return diag_res


def check_vert(data:list[str]) -> int:
    vert_res = 0
    for i in range(len(data) - 3):
        for j in range(len(data[i])):
            if data[i][j] == "X" and data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
#                 print(i,j)
                vert_res += 1
            elif data[i][j] == "S" and data[i+1][j] == "A" and data[i+2][j] == "M" and data[i+3][j] == "X":
                vert_res += 1
    return vert_res

print(f"The answer to part one is {part_1('sample.txt')}")
# print(f"The answer to part two is {part_2()}")
print(f"Time taken is {time.time_ns() - start_time} nanoseconds = {(time.time_ns() - start_time)/1e+9} seconds")