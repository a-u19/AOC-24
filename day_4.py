import time
import regex as re

def part_1(inp_filepath: str) -> int:
    # Read input file into a 2D list
    data = [line.strip() for line in open(inp_filepath).readlines()]
    total_matches = 0

    # Check all directions for "XMAS"
    total_matches += check_pattern(data, "XMAS")

    return total_matches


def check_pattern(data: list[str], pattern: str) -> int:
    rows, cols = len(data), len(data[0])
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]
    matches = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if match_word(data, pattern, i, j, dx, dy):
                    matches += 1

    return matches


def match_word(data: list[str], word: str, x: int, y: int, dx: int, dy: int) -> bool:
    rows, cols = len(data), len(data[0])

    for k in range(len(word)):
        nx, ny = x + k * dx, y + k * dy
        if not (0 <= nx < rows and 0 <= ny < cols) or data[nx][ny] != word[k]:
            return False

    return True


def part_2(inp_filepath:str) -> int:
    data = [line.strip() for line in open(inp_filepath).readlines()]
    total_matches = 0
    patterns = [tuple((r'M.S', r'M.S')), tuple((r'S.S', r'M.M')), tuple((r'S.M', r'S.M')), tuple((r'M.M', r'S.S'))]
    for pattern in patterns:
        for line_idx, line in enumerate(data):
            # print(pattern, line_idx, line)
            try:
                matches = re.finditer(pattern[0], line, overlapped=True)
                for match in matches:
                    # print(line_idx, match.span())
                    if re.match(r".A.", data[line_idx+1][match.start():match.end()]) and re.match(pattern[1], data[line_idx+2][match.start():match.end()]):
                        total_matches += 1
                        # print(line_idx, match.span(), pattern)
            except IndexError:
                pass
        # data = [''.join(reversed(col)) for col in zip(*data)]

    return total_matches

# Run the program
start_time = time.time_ns()
print(f"The answer to part one is {part_1('day_4_input.txt')}")
print(f"The answer to part two is {part_2('day_4_input.txt')}")
print(f"Time taken: {time.time_ns() - start_time} nanoseconds = {(time.time_ns() - start_time)/1e+9} seconds")
