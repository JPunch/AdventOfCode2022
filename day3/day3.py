import typing as t


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


POINTS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def day1(input: t.List[str]) -> int:
    points = 0
    for backpack in input:
        length = len(backpack)
        first_compartment, second_compartment = set(backpack[0 : int(length / 2)]), set(
            backpack[int(length / 2) :]
        )

        common = first_compartment.intersection(second_compartment)
        points += POINTS.index("".join(common)) + 1

    return points


def day2(input: t.List[str]) -> int:
    assert (len(input) % 3) == 0
    points = 0
    lots_of_3 = int(len(input) / 3)
    for i in range(lots_of_3):
        # get next 3
        backpacks = input[i * 3 : i * 3 + 3]
        (b1, b2, b3) = (set(backpack) for backpack in backpacks)
        common = b1 & b2 & b3
        points += POINTS.index("".join(common)) + 1

    return points


def main():
    input = get_input("day3/input.txt")
    # parsed_input = parse_input(input)
    day1_result = day1(input)
    day2_result = day2(input)
    print(day1_result, day2_result)
    ...


if __name__ == "__main__":
    main()
