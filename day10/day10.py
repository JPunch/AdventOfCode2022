import typing as t


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


class CPU:
    def __init__(self, cycles_to_report):
        self.cycles_to_report = cycles_to_report
        self.register = 1
        self.cycles = 0
        self.reports = []
        self.display = ["."] * 240

    def check_cycle(self):
        print(f"cycles: {self.cycles} - register: {self.register}")
        if self.cycles in self.cycles_to_report:
            # print(f"cycles: {self.cycles} - register: {self.register}")
            self.reports.append(self.register * self.cycles)

    def draw_display(self):
        if self.cycles % 40 in [self.register, self.register - 1, self.register + 1]:
            self.display[self.cycles] = "#"

    def noop(self):
        self.draw_display()
        self.cycles += 1
        self.check_cycle()

    def addx(self, val):
        self.draw_display()
        self.cycles += 1
        self.check_cycle()
        self.draw_display()
        self.cycles += 1
        self.check_cycle()
        self.register += val


def day1(input_data: t.List[str]) -> int:
    cpu = CPU([20, 60, 100, 140, 180, 220])
    for command in input_data:
        print(command.split())
        match command.split():
            case ["noop"]:
                cpu.noop()
            case ("addx", val):
                cpu.addx(int(val))
    day2(cpu)
    return sum(cpu.reports)


def day2(cpu) -> int:
    for i in range(6):
        print("".join(cpu.display[i * 40 : (i + 1) * 40]))


def main():
    input_data = get_input("day10/input.txt")
    day1_result = day1(input_data)
    # day2_result = day2(input_data)
    print(day1_result)


if __name__ == "__main__":
    main()
