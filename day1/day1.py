import typing as t


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


def parse_input(input_data: t.List[str]) -> t.List[t.Tuple[int]]:
    parsed = []
    temp = []
    for line in input_data:
        if line != "":
            temp.append(int(line))  # str to int
        else:
            parsed.append(tuple(temp))
            temp.clear()
            continue
    parsed.append(tuple(temp))
    return parsed


def day1(input: t.List[t.Tuple[int]]) -> int:
    maximum_snack = max([sum(snacks) for snacks in input])
    return maximum_snack


def day2(input: t.List[t.Tuple[int]]) -> int:
    total_snack_list = [sum(snacks) for snacks in input]
    total_snack_list.sort()
    return sum(total_snack_list[-3:])


def main():
    input = get_input("day1/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)
    ...


if __name__ == "__main__":
    main()
