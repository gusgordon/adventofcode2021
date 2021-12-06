from collections import deque


def main():

    window_length = 3
    current_window = deque(maxlen=window_length)
    prev_window = deque(maxlen=window_length)
    num_increased = 0
    with open("day_1_input.txt") as file:
        for line in file:
            depth = int(line)
            current_window.append(depth)
            if (
                len(current_window) == window_length
                and len(prev_window) == window_length
                and sum(current_window) > sum(prev_window)
            ):
                num_increased += 1
            prev_window.append(depth)
    print(num_increased)


if __name__ == "__main__":
    main()
