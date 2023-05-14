import random
import linecache


def get_random_line(file_path):
    num_lines = sum(1 for _ in open(file_path, encoding="utf-8"))
    if num_lines == 0:
        return None

    random_line_number = random.randint(1, num_lines)
    random_line = linecache.getline(file_path, random_line_number).strip()

    return random_line


file_path = "lines.txt"

random_line = get_random_line(file_path)
if random_line is not None:
    print(random_line)
