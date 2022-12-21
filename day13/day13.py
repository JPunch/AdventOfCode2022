import typing as t
from copy import deepcopy
from enum import Enum
from functools import cmp_to_key


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


def parse_input_day2(input_data: t.List[str]) -> t.List:
    parsed = [eval(i.strip()) for i in input_data.split("\n") if i != ""]
    return parsed


def day1(input_data: t.List) -> int:
    indexs = []
    for index, val in enumerate(input_data):
        if compare(*val) > 0:
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


def compare_element(left: int, right: int):
    if left > right:
        return -1
    elif left < right:
        return 1
    return 0


def compare_list(left, right):
    left_len, right_len = len(left), len(right)
    for i in range(len(right)):
        # Check the value, if equal continue looping
        if i >= left_len:
            return 1
        if (ret := compare(left[i], right[i])) != 0:
            return ret
    # if it reaches here, all must be equal for length of right
    if left_len > right_len:
        return -1
    return 0


def day2(input_data: t.List) -> int:
    input_data.extend([[[2]], [[6]]])
    a = deepcopy(input_data)
    changes = 0
    # sorted(a, key=cmp_to_key(compare))
    sorting_complete = False
    while not sorting_complete:
        for i in range(len(a) - 1):
            if (ret := compare(a[i], a[i + 1])) > 0:
                # in the correct order
                pass
            elif ret < 0:
                # in reverse order
                a[i], a[i + 1] = a[i + 1], a[i]
                changes += 1
            else:
                ...
        if changes == 0:
            sorting_complete = True
        else:
            changes = 0
    return (a.index([[2]]) + 1) * (a.index([[6]]) + 1)


def main():
    input = get_input("day13/input.txt")
    parsed_input = parse_input(input)
    day1_result = 0  # day1(parsed_input)
    parsed_input = parse_input_day2(input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
