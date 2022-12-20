from enum import Enum
from functools import cmp_to_key
import typing as t


class ComparisonOutcome(Enum):
    Right = True
    Left = False
    Neither = None


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.read()
    return data


def parse_input(input_data: t.List[str]) -> t.List:
    parsed = []
    pairs = [i.strip() for i in input_data.split("\n\n")]
    for pair in pairs:
        left, right = pair.split("\n")
        parsed.append((eval(left), eval(right)))
    return parsed


def day1(input_data: t.List) -> int:
    indexs = []
    for index, val in enumerate(input_data):
        if compare(*val) == ComparisonOutcome.Right:
            indexs.append(index + 1)
    return sum(indexs)


def compare(left, right):
    if isinstance(left, list) and isinstance(right, int):
        return compare_list(left, [right])
    elif isinstance(right, list) and isinstance(left, int):
        return compare_list([left], right)
    elif isinstance(left, list) and isinstance(right, list):
        return compare_list(left, right)
    else:  # int int
        return compare_element(left, right)


def compare_element(left: int, right: int) -> ComparisonOutcome:
    if left > right:
        return ComparisonOutcome.Left
    elif left < right:
        return ComparisonOutcome.Right
    return ComparisonOutcome.Neither


def compare_list(left, right):
    left_len, right_len = len(left), len(right)
    for i in range(len(right)):
        # Check the value, if equal continue looping
        if i >= left_len:
            return ComparisonOutcome.Right
        if (ret := compare(left[i], right[i])) != ComparisonOutcome.Neither:
            return ret
    # if it reaches here, all must be equal for length of right
    if left_len > right_len:
        return ComparisonOutcome.Left
    return ComparisonOutcome.Neither


def day2(input_data: t.List) -> int:
    input_data.extend([[[2]], [[6]]])
    sorted(input_data, key=cmp_to_key(compare))
    return 0


def main():
    input = get_input("day13/input2.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
