import copy
import re
import typing as t
from collections import deque


class CrateStack:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        self.stack3 = deque()
        self.stack4 = deque()
        self.stack5 = deque()
        self.stack6 = deque()
        self.stack7 = deque()
        self.stack8 = deque()
        self.stack9 = deque()

    def get_stack(self, index: int):
        match index:
            case 1:
                return self.stack1
            case 2:
                return self.stack2
            case 3:
                return self.stack3
            case 4:
                return self.stack4
            case 5:
                return self.stack5
            case 6:
                return self.stack6
            case 7:
                return self.stack7
            case 8:
                return self.stack8
            case 9:
                return self.stack9
    
    def set_stack(self, index, value):
        match index:
            case 1:
                self.stack1 = value
            case 2:
                self.stack2 = value
            case 3:
                self.stack3 = value
            case 4:
                self.stack4 = value
            case 5:
                self.stack5 = value
            case 6:
                self.stack6 = value
            case 7:
                self.stack7 = value
            case 8:
                self.stack8 = value
            case 9:
                self.stack9 = value
        
    def from_input_line(self, index: int, input_line: t.List[str]):
        for letter in input_line:
            stack = self.get_stack(index)
            if letter != ' ':
                stack.appendleft(letter)


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
    # data = [line.strip() for line in data]
    return data


def parse_input(
    input_data: str,
) -> t.Tuple[CrateStack, t.List[CraneProcedure]]:
    for index, line in enumerate(input_data):
        if line == "\n" or line == r"\n":
            left = input_data[0:index - 1]
            right = input_data[index + 1 :]
            break

    return (parse_stack(left), parse_procedure(right))


def parse_stack(input_data: str) -> CrateStack: # Won't work if there's an empty stack, but we move
    cs = CrateStack()
    transposed_per_char = list(map(list, zip(*input_data)))
    count = 1
    for line in transposed_per_char:
        if not any(item in ['\n', '[', ']'] for item in line) and not all(item == ' ' for item in line): # make sure it's not a brace line or end or input
            # We've got a data line
            cs.from_input_line(count, line)
            count += 1
    return cs


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


def day1(input_data: t.Tuple[CrateStack, t.List[CraneProcedure]]) -> int:

    cs, cps = copy.deepcopy(input_data)
    for procedure in cps:
        to_move = []
        from_stack = cs.get_stack(procedure.from_stack)
        to_stack = cs.get_stack(procedure.to_stack)
        while len(to_move) < procedure.amount:
            to_move.append(from_stack.pop())
        to_stack.extend(to_move)
    top_of_stacks = [cs.get_stack(i)[-1] for i in range(1,10)]

    return "".join(top_of_stacks)


def day2(input_data: t.List[t.Tuple[str, str]]) -> int:
    cs, cps = input_data
    for procedure in cps:
        to_move = []
        from_stack = cs.get_stack(procedure.from_stack)
        to_stack = cs.get_stack(procedure.to_stack)
        while len(to_move) < procedure.amount:
            to_move.append(from_stack.pop())
        while to_move:
            to_stack.append(to_move.pop())
        to_stack.extend(to_move[::-1])
    top_of_stacks = [cs.get_stack(i)[-1] for i in range(1,10)]

    return "".join(top_of_stacks)


def main():
    input = get_input("day5/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
