import typing as t


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


def parse_input(input_data: t.List[str]) -> t.List[t.List[int]]:
    data = [(i.split()[0], int(i.split()[1])) for i in input_data]
    return data


class Knot:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.positions = set()
        self.positions.add((0, 0))
        self.follower = None

    def is_adjacent(self):
        if self.parent is not None:
            if (
                abs(self.parent.position[0] - self.position[0]) > 1
                or abs(self.parent.position[1] - self.position[1]) > 1
            ):
                return False
            return True

    def move(self, command: t.Tuple[str, int]):
        count = 0
        while count < command[1]:
            match command[0]:
                case "U":
                    # up
                    self.position[1] += 1
                case "D":
                    # down
                    self.position[1] -= 1
                case "R":
                    # right
                    self.position[0] += 1
                case "L":
                    # left
                    self.position[0] -= 1
                case "DTR":
                    self.position[0] += 1
                    self.position[1] += 1
                case "DTL":
                    self.position[0] -= 1
                    self.position[1] += 1
                case "DBR":
                    self.position[0] += 1
                    self.position[1] -= 1
                case "DBL":
                    self.position[0] -= 1
                    self.position[1] -= 1
            count += 1

            self.positions.add(tuple(self.position))
            if self.follower is not None:
                if not self.follower.is_adjacent():
                    self.follower.follow()

    def follow(self):
        # get direction
        command = ["", 1]
        parent_coords = self.parent.position
        horz = parent_coords[0] - self.position[0]
        vert = parent_coords[1] - self.position[1]
        if abs(horz) > 0 and abs(vert) > 0:
            # moving diagonal
            if horz > 0 and vert > 0:
                command[0] = "DTR"
            elif horz > 0 and vert < 0:
                command[0] = "DBR"
            elif horz < 0 and vert > 0:
                command[0] = "DTL"
            else:
                command[0] = "DBL"
        else:

            if horz > 0 and abs(horz) > 1:
                command[0] = "R"
            elif horz < 0 and abs(horz) > 1:
                command[0] = "L"
            elif vert > 0 and abs(vert) > 1:
                command[0] = "U"
            elif vert < 0 and abs(vert) > 1:
                command[0] = "D"
            else:
                raise Exception("Shoudn't get here")
        self.move(command)


def day1(input_data: t.List[str]) -> int:
    head = Knot(parent=None, position=[0, 0])
    tail = Knot(head, position=[0, 0])
    head.follower = tail
    for command in input_data:
        head.move(command)
    return len(tail.positions)


def day2(input_data: t.List[str]) -> int:
    head = Knot(parent=None, position=[0, 0])
    tail = Knot(head, position=[0, 0])
    head.follower = tail
    for i in range(8):
        temp_tail = tail
        tail = Knot(temp_tail, position=[0, 0])
        temp_tail.follower = tail

    for command in input_data:
        head.move(command)
    return len(tail.positions)


def main():
    input_data = get_input("day9/input.txt")
    test = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20",
    ]
    parsed_data = parse_input(input_data)
    day1_result = day1(parsed_data)
    day2_result = day2(parsed_data)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
