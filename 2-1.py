def get_line_value(line):
    return int(line.split(" ")[1])


def main():
    horizontal_position = 0
    depth = 0
    with open("day_2_input.txt") as file:
        for line in file:
            if line.startswith("forward"):
                horizontal_position += get_line_value(line)
            elif line.startswith("up"):
                depth -= get_line_value(line)
            elif line.startswith("down"):
                depth += get_line_value(line)
    print(horizontal_position, depth, horizontal_position * depth)


if __name__ == "__main__":
    main()
