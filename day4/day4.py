import typing as t


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


def parse_input(
    input_data: t.List[str],
) -> t.List[t.Tuple[int, int, int, int]]:
    parsed = []
    for line in input_data:
        elf1, elf2 = line.split(",")[0].split("-"), line.split(",")[1].split("-")

        parsed.append((int(elf1[0]), int(elf1[1]), int(elf2[0]), int(elf2[1])))
    return parsed


def day1(input: t.List[t.Tuple[int, int, int, int]]) -> int:
    count = 0
    for assignments in input:
        # assignment1 = {i for i in range(assignments[0], assignments[1] + 1)}
        # assignment2 = {i for i in range(assignments[2], assignments[3] + 1)}
        # if assignment1 > assignment2 or assignment2 > assignment1:
        #     count += 1
        cond1 = assignments[0] >= assignments[2] and assignments[1] <= assignments[3]
        cond2 = assignments[2] >= assignments[0] and assignments[3] <= assignments[1]
        if cond1 or cond2:
            count += 1
    return count


def day2(input: t.List[t.Tuple[int, int, int, int]]) -> int:
    count = 0
    for assignments in input:
        assignment1 = {i for i in range(assignments[0], assignments[1] + 1)}
        assignment2 = {i for i in range(assignments[2], assignments[3] + 1)}
        if assignment1 & assignment2:
            count += 1
    return count


def main():
    input = get_input("day4/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)
    # 423 is wrong, too low


if __name__ == "__main__":
    main()
