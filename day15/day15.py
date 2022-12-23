import typing as t
import copy


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    data = [line.strip() for line in data]
    return data


def parse_input(input_data: t.List[str]) -> t.List:
    return input_data


def day1(grid: t.List) -> int:
    return 0


def day2(grid: t.List) -> int:
    return 0


def main():
    input = get_input("day15/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(copy.deepcopy(parsed_input))
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
