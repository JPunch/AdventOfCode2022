import typing as t


def get_input(filename: str) -> str:
    with open(filename, "r") as f:
        data = f.read()
    data = data.strip()
    return data


def day1(input: str) -> int:
    for i in range(len(input) - 4):
        window = input[i : i + 4]
        if len(set(window)) == 4:
            return i + 4


def day2(input: str) -> int:
    for i in range(len(input) - 14):
        window = input[i : i + 14]
        if len(set(window)) == 14:
            return i + 14


def main():
    input = get_input("day6/input.txt")
    day1_result = day1(input)
    day2_result = day2(input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
