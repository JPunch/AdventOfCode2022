import typing as t

def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


def parse_input( input_data: t.List[str], ) -> t.List[str]:
    return input_data

def day1(input: t.List[str]) -> int:
    return 0


def day2(input: t.List[str]) -> int:
    return 0


def main():
    input = get_input("day12/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
