import typing as t
import copy


class Grid:
    def __init__(self):
        self.wall_coords = set()
        self.sand_coords = set()
        self.active_sand = []
        self.spawn_locations = []
        self.spawned_sand = 0
        self.max_y = 0

    def spawn_sand(self):
        for location in self.spawn_locations:
            self.active_sand.append(location)
            self.spawned_sand += 1

    def move_sand(self, is_day2: bool = False):
        for index, coord in enumerate(self.active_sand):
            next_coord = (coord[0], coord[1] + 1)
            if is_day2 and (self.active_sand[index][1] + 1 == self.max_y[1] + 2):
                self.sand_coords.add(self.active_sand[index])
                self.active_sand.remove(coord)
            elif (
                next_coord not in self.wall_coords
                and next_coord not in self.sand_coords
            ):
                self.active_sand[index] = next_coord
            elif (
                next_coord := (coord[0] - 1, coord[1] + 1)
            ) not in self.wall_coords and next_coord not in self.sand_coords:
                self.active_sand[index] = next_coord
            elif (
                next_coord := (coord[0] + 1, coord[1] + 1)
            ) not in self.wall_coords and next_coord not in self.sand_coords:
                self.active_sand[index] = next_coord
            else:  # stop the sand
                self.sand_coords.add(self.active_sand[index])
                self.active_sand.remove(coord)
            if is_day2:
                if any([coord in self.sand_coords for coord in self.spawn_locations]):
                    return False
            elif self.active_sand and self.active_sand[index][1] >= self.max_y[1]:
                return False


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    data = [line.strip() for line in data]
    return data


def str_to_command(command_str: str) -> t.Tuple[int, int]:
    return tuple(int(i) for i in command_str.split(","))


def parse_input(input_data: t.List[str]) -> t.List:
    grid = Grid()
    for line in input_data:
        commands = [
            str_to_command(i) for i in (command.strip() for command in line.split("->"))
        ]
        for index in range(len(commands) - 1):
            x_coords = [commands[index][0], commands[index + 1][0]]
            y_coords = [commands[index][1], commands[index + 1][1]]
            commands_to_add = {
                (i, j)
                for i in range(min(x_coords), max(x_coords) + 1)
                for j in range(min(y_coords), max(y_coords) + 1)
            }
            grid.wall_coords.update(commands_to_add)
    return grid


def day1(grid: t.Type["Grid"]) -> int:
    grid.spawn_locations.append((500, 0))
    grid.max_y = max(grid.wall_coords, key=lambda x: x[1])
    sand_falling = True
    # end condition is the first block of sand that goes above the highest wall_coords
    while sand_falling:
        grid.spawn_sand()
        while grid.active_sand:
            if grid.move_sand() == False:
                sand_falling = False
                break
    return len(grid.sand_coords)


def day2(grid: t.Type["Grid"]) -> int:
    grid.spawn_locations.append((500, 0))
    grid.max_y = max(grid.wall_coords, key=lambda x: x[1])
    sand_falling = True
    # end condition is the first block of sand that goes above the highest wall_coords
    while sand_falling:
        grid.spawn_sand()
        while grid.active_sand:
            if grid.move_sand(is_day2=True) == False:
                sand_falling = False
                break
    return len(grid.sand_coords)


def main():
    input = get_input("day14/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(copy.deepcopy(parsed_input))
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
