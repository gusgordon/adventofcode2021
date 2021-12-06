def get_line_value(line):
    return int(line.split(" ")[1])


def main():
    horizontal_position = 0
    aim = 0
    depth = 0
    with open("day_2_input.txt") as file:
        for line in file:
            if line.startswith("forward"):
                line_value = get_line_value(line)
                horizontal_position += line_value
                depth += aim * line_value
            elif line.startswith("up"):
                aim -= get_line_value(line)
            elif line.startswith("down"):
                aim += get_line_value(line)
    print(horizontal_position, depth, horizontal_position * depth)


if __name__ == "__main__":
    main()
