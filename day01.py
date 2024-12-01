def parse_input(lines):
    first = sorted(int(line.split()[0]) for line in lines)
    second = sorted(int(line.split()[1]) for line in lines)
    return first, second

def part1(first, second):
    distance = sum(abs(a - b) for a, b in zip(first, second))
    print(distance)


def part2(first, second):
    similar = sum(f * second.count(f) for f in first)
    print(similar)

if __name__ == "__main__":
    with open("input/day01", "r") as f:
        lines = f.readlines()

    first, second = parse_input(lines)
    part1(first, second)
    part2(first, second)