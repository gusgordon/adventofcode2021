def main():

    prev_depth = None
    num_increased = 0
    with open("day_1_input.txt") as file:
        for line in file:
            depth = int(line)
            if prev_depth is not None and depth > prev_depth:
                num_increased += 1
            prev_depth = depth
    print(num_increased)


if __name__ == "__main__":
    main()
