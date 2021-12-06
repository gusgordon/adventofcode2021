def main():
    bits = []
    with open("day_3_input.txt") as file:
        for line in file:
            for i, bit in enumerate(line):
                if bit not in ["0", "1"]:
                    continue
                if len(bits) <= i:
                    bits.append([])
                bits[i].append(bit)

    most_common_str = "".join(["1" if (x.count("1") > len(x) / 2) else "0" for x in bits])
    least_common_str = "".join(["0" if x == "1" else "1" for x in most_common_str])
    gamma = int(most_common_str, base=2)
    epsilon = int(least_common_str, base=2)
    print(most_common_str, least_common_str, gamma, epsilon)
    power_consumption = gamma * epsilon
    print(power_consumption)


if __name__ == "__main__":
    main()
