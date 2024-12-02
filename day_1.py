import time
start_time = time.time()

def get_lists(inp_file) -> (list, list):
    with open(inp_file) as file:
        list_1, list_2 = zip(*(map(int, line.split("   ")) for line in file))
    return list_1, list_2


def part_1(inp_file) -> int:
    list_1, list_2 = get_lists(inp_file)
    list_1, list_2 = sorted(list_1), sorted(list_2)
    return sum(abs(a - b) for a, b in zip(list_1, list_2))


def convert_list_to_hashmap(list):
    d = {}
    for num in list:
        if num not in d.keys():
            d[num] = 1
        else:
            d[num] += 1
    return d

def part_2(inp_file) -> int:
    list_1, list_2 = get_lists(inp_file)
    d_2 = convert_list_to_hashmap(list_2)
    # print(d_2)
    s_1, s_2 = set(list_1), set(d_2.keys())
    overlapping = s_1 & s_2
    res = 0
    for num in overlapping:
        res += num * d_2[num]

    return res

print(f"The answer to part 1 is {part_1('day_1_input.txt')}")
print(f"The answer to part 2 is {part_2('day_1_input.txt')}")
print(f"Time taken is {round(time.time() - start_time,9)}s")
