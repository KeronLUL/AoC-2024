import argparse
import aocd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Advent of Code helper')
    
    parser.add_argument('-d', '--day', type=int, help='Day of the month (1-25)')
    parser.add_argument('-y', '--year', type=int, help='Year (2015-2024)')
    parser.add_argument('-a', '--answer', type=int, help='Answer to submit (int)')

    args = parser.parse_args()

    if args.answer:
        if args.year:
            aocd.submit(args.answer, day=args.day, year=args.year)
        else:
            aocd.submit(args.answer, day=args.day)
    else:
        file = open(f"input/day{args.day:02d}", "w")
        file.write(aocd.get_data(day=args.day, year=args.year))
