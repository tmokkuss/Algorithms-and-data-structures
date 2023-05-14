import linecache


def find_longest_decreasing_sequence(file_path):
    longest_sequence_length = 1
    longest_sequence_start = ""
    current_sequence_length = 1

    line_number = 1
    current_line = linecache.getline(file_path, line_number).rstrip()
    next_line = linecache.getline(file_path, line_number + 1).rstrip()

    while current_line:
        current_data = current_line.split(";")
        next_data = next_line.split(";")

        if int(next_data[2]) <= int(current_data[2]):
            current_sequence_length += 1
            if current_sequence_length > longest_sequence_length:
                longest_sequence_length = current_sequence_length
                longest_sequence_start = current_data[0] + " " + current_data[1]
        else:
            current_sequence_length = 1

        line_number += 1
        current_line = next_line
        next_line = linecache.getline(file_path, line_number + 1).rstrip()

    return longest_sequence_length, longest_sequence_start


file_path = "alpha_oriona.csv"
longest_sequence_length, longest_sequence_start = find_longest_decreasing_sequence(file_path)

output_file_path = "result.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(str(longest_sequence_length) + "\n")
    output_file.write(longest_sequence_start)
