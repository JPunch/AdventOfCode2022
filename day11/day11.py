import typing as t
from enum import Enum
from functools import reduce
from operator import mul


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.read()
    return data


def parse_data(input_data: str) -> t.Type["MonkeyBusiness"]:
    mb = MonkeyBusiness()
    monkeys = [monkey.split("\n") for monkey in input_data.split("\n\n")]
    for monkey in monkeys:
        num = int(monkey[0][7 : monkey[0].find(":")])
        starting_items = [
            int(i) for i in monkey[1][monkey[1].find(":") + 1 :].split(",")
        ]
        op = Operation(monkey[2][23])
        if (val := monkey[2][25:]) == "old":
            if op == Operation.multiply:
                op = Operation.square
            else:
                raise Exception("Don't go there!")
        else:
            val = int(val)

        div_val = int(monkey[3][monkey[3].find("by") + 2 :])
        true_monkey = int(monkey[4][monkey[4].find("monkey") + 6 :])
        false_monkey = int(monkey[5][monkey[5].find("monkey") + 6 :])
        new_monkey = Monkey(
            mb, starting_items, op, val, div_val, true_monkey, false_monkey
        )
        mb.add_monkey(new_monkey, num)
    return mb


class MonkeyBusiness:
    def __init__(self):
        self.monkeys = {}
        self.round = 0

    def add_monkey(self, monkey, key):
        self.monkeys[key] = monkey

    def move_item(self, monkey_key, item):
        monkey = self.monkeys[monkey_key]
        monkey.items_to_huck.append(item)

    def run_rounds(self, num, is_day2=False):
        for i in range(num):
            for j in range(len(self.monkeys)):
                if is_day2:
                    self.monkeys[j].do_stuff2()
                else:
                    self.monkeys[j].do_stuff()
        self.round += num


class Operation(Enum):
    add = "+"
    multiply = "*"
    square = 0
    double = 1


class Monkey:
    def __init__(
        self,
        mb: t.Type["MonkeyBusiness"],
        items,
        operation,
        operation_value,
        divisible,
        if_true,
        if_false,
    ):
        self.mb = mb
        self.inspected_items = 0
        self.items_to_huck = items
        self.operation = operation
        self.operation_value = operation_value
        self.divisible = divisible
        self.if_true = if_true
        self.if_false = if_false
        self.day2_divisible = 1

    def do_stuff(self):
        for item in self.items_to_huck:
            match self.operation:
                case Operation.square:
                    worry_level = item * item
                case Operation.multiply:
                    worry_level = item * self.operation_value
                case Operation.add:
                    worry_level = item + self.operation_value
            worry_level = worry_level // 3
            if worry_level % self.divisible == 0:
                self.mb.move_item(self.if_true, worry_level)
            else:
                self.mb.move_item(self.if_false, worry_level)
            self.inspected_items += 1
        self.items_to_huck = []

    def do_stuff2(self):
        for item in self.items_to_huck:
            match self.operation:
                case Operation.square:
                    worry_level = item * item
                case Operation.multiply:
                    worry_level = item * self.operation_value
                case Operation.add:
                    worry_level = item + self.operation_value
            # worry_level = worry_level // 3
            if worry_level % self.divisible == 0:
                self.mb.move_item(self.if_true, worry_level % self.day2_divisible)
            else:
                self.mb.move_item(
                    self.if_false,
                    worry_level % self.day2_divisible,
                )
            self.inspected_items += 1
        self.items_to_huck = []


def day1(mb: t.Type["MonkeyBusiness"]) -> int:
    mb.run_rounds(20)
    monkey_hucked_times = [monkey.inspected_items for monkey in mb.monkeys.values()]
    monkey_hucked_times.sort()
    return monkey_hucked_times[-1] * monkey_hucked_times[-2]


def day2(mb) -> int:
    divisors = [monkey.divisible for monkey in mb.monkeys.values()]
    common_factor = reduce(mul, divisors, 1)
    for monkey in mb.monkeys.values():
        monkey.day2_divisible = common_factor
    mb.run_rounds(10000, True)
    monkey_hucked_times = [monkey.inspected_items for monkey in mb.monkeys.values()]
    monkey_hucked_times.sort()
    return monkey_hucked_times[-1] * monkey_hucked_times[-2]


def main():
    input_data = get_input("day11/input.txt")
    monkey_business = parse_data(input_data)
    day1_result = day1(monkey_business)
    monkey_business = parse_data(input_data)
    day2_result = day2(monkey_business)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
