import typing as t
from copy import deepcopy
from enum import Enum
from functools import cmp_to_key


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    data = [line.strip() for line in data]
    return data


def parse_input(input_data: t.List[str]) -> t.List:
    parsed = []
    pairs = [i.strip() for i in input_data.split("\n\n")]
    for pair in pairs:
        left, right = pair.split("\n")
        parsed.append((eval(left), eval(right)))
    return parsed


def day1(input_data: t.List) -> int:
    return 0


def day2(input_data: t.List) -> int:
    return 0


def main():
    input = get_input("day13/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
