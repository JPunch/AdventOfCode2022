import typing as t


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


def day1(input: t.List) -> int:
    return 0


def list_recurse(ls: t.List):
    for element in ls:
        if isinstance(element, list):
            return list_recurse(element)
        else:
            element


def day2(input: t.List[str]) -> int:
    return 0


def main():
    input = get_input("day13/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
