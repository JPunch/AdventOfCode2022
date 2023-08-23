import copy
import re
import typing as t


class Volcano:
    def __init__(self):
        self.pressure = 0
        self.total_pressure = 0
        self.time_left = 30

    def is_finished(self) -> bool:
        if self.time_left <= 0:
            return True
        return False

    def tick(self):
        self.time_left -= 1
        self.total_pressure += self.pressure


class Valve:
    def __init__(self, parent, children, flow_rate):
        self.parent = parent
        self.children = children
        self.flow_rate = flow_rate


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    data = [line.strip() for line in data]
    return data


def parse_input(input_data: t.List[str]) -> t.List[str]:
    pattern = "^Valve ([A-Z]+) has flow rate=(\d+)\; tunnels lead to valves ((?:[A-Z]{2}(?:, )?)+)$"
    return []


def day1(sensors: t.List[str]) -> int:
    return 0


def day2(sensors: t.List[str]) -> int:
    return 0


def main():
    input = get_input("day16/input2.txt")
    parsed_input = parse_input(input)
    day1_result = day1(copy.deepcopy(parsed_input))
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
