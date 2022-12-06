import copy
import re
import typing as t
from collections import deque

class CraneProcedure:
    def __init__(self, amount, from_stack, to_stack):
        self.amount = amount
        self.from_stack = from_stack
        self.to_stack = to_stack
    
    def __repr__(self) -> str:
        return f"amount: {self.amount}, from: {self.from_stack}, to: {self.to_stack}"


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def parse_input(
    input_data: str,
) -> t.Tuple[t.List[deque], t.List[CraneProcedure]]:
    for index, line in enumerate(input_data):
        if line == "\n" or line == r"\n":
            left = input_data[0:index - 1]
            right = input_data[index + 1 :]
            break

    return (parse_stack(left), parse_procedure(right))


def parse_stack(input_data: str) -> t.List[deque]: # Won't work if there's an empty stack, but we move
    stack_array = [deque() for i in range(9)]
    transposed_per_char = list(map(list, zip(*input_data)))
    count = 0
    for line in transposed_per_char:
        if not any(item in ['\n', '[', ']'] for item in line) and not all(item == ' ' for item in line): # make sure it's not a brace line or end or input
            stack_array[count].extendleft(line)
            count += 1
    # Clear all the empty entries ' '
    for i in stack_array:
        while ' ' in i:
            i.remove(' ')
    return stack_array


def parse_procedure(input: str) -> t.List[CraneProcedure]:
    line_regex = re.compile(r"move (?P<amount>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)")
    procedures = []
    for line in input:
        re_match = line_regex.match(line)
        if re_match is not None:
            amount = int(re_match.group('amount'))
            from_stack = int(re_match.group('from_stack'))
            to_stack = int(re_match.group('to_stack'))
            procedures.append(CraneProcedure(amount, from_stack, to_stack))
    return procedures


def day1(input_data: t.Tuple[t.List[deque], t.List[CraneProcedure]]) -> int:
    stack_array, cps = copy.deepcopy(input_data)
    for procedure in cps:
        to_move = []
        from_stack = stack_array[procedure.from_stack - 1]
        to_stack = stack_array[procedure.to_stack - 1]
        while len(to_move) < procedure.amount:
            to_move.append(from_stack.pop())
        to_stack.extend(to_move)
    top_of_stacks = [stack[-1] for stack in stack_array]

    return "".join(top_of_stacks)


def day2(input_data: t.List[t.Tuple[str, str]]) -> int:
    stack_array, cps = input_data
    for procedure in cps:
        to_move = []
        from_stack = stack_array[procedure.from_stack - 1]
        to_stack = stack_array[procedure.to_stack - 1]
        while len(to_move) < procedure.amount:
            to_move.append(from_stack.pop())
        while to_move:
            to_stack.append(to_move.pop())
        to_stack.extend(to_move[::-1])
    top_of_stacks = [stack[-1] for stack in stack_array]

    return "".join(top_of_stacks)


def main():
    input = get_input("day5/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
