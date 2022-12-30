import copy
import re
import typing as t

import numpy as np


class Sensor:
    def __init__(self, coord: t.Tuple[int, int], b_coord: t.Tuple[int, int]):
        self.coord = coord
        self.b_coord = b_coord
        self.manhattan_distance = Sensor.manhattan_dictance_from_coord(coord, b_coord)

    def coord_in_range(self, coord: t.Tuple[int, int]) -> bool:
        if (
            Sensor.manhattan_dictance_from_coord(self.coord, coord)
            <= self.manhattan_distance
        ):
            return True
        return False

    @staticmethod
    def manhattan_dictance_from_coord(start_coord, end_coord):
        return abs(start_coord[0] - end_coord[0]) + abs(start_coord[1] - end_coord[1])


def is_sensor_in_y_range(sensor: t.Type["Sensor"], y_value: int) -> bool:
    if (
        (sensor.coord[1] < y_value)
        and (sensor.coord[1] + sensor.manhattan_distance >= y_value)
    ) or (
        (sensor.coord[1] > y_value)
        and (sensor.coord[1] - sensor.manhattan_distance <= y_value)
    ):
        return True
    return False


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    data = [line.strip() for line in data]
    return data


def parse_input(input_data: t.List[str]) -> t.List[t.Type["Sensor"]]:
    line_re = re.compile(
        r"^Sensor at x=(?P<sensor_x>\d+|-\d+),\sy=(?P<sensor_y>\d+|-\d+).*x=(?P<beacon_x>\d+|-\d+), y=(?P<beacon_y>\d+|-\d+)$"
    )
    sensors = map(
        lambda x: Sensor(
            (int(x.groups()[0]), int(x.groups()[1])),
            (int(x.groups()[2]), int(x.groups()[3])),
        ),
        [line_re.match(line) for line in input_data],
    )
    return list(sensors)


def day1(sensors: t.List[t.Type["Sensor"]]) -> int:
    """
    numbers are way too big for a grid to be reasonable
    Keep track of max x and max y
    need a good way of populating all points with a manhattan distance = to sensor manhattan distance, maybe combinations or permutations
    ALTERNATELY: I can check each coord compared to the 10 sensors, just if greater manhattan for all then increase counter
    """
    y = 10
    min_x = sensors[0].coord[0]
    max_x = sensors[0].coord[0]
    count = 0
    for sensor in sensors:
        if sensor.coord[0] - sensor.manhattan_distance < min_x:
            min_x = sensor.coord[0] - sensor.manhattan_distance
        if sensor.b_coord[0] < min_x:
            min_x = sensor.b_coord[0]
        if sensor.coord[0] + sensor.manhattan_distance > max_x:
            max_x = sensor.coord[0] + sensor.manhattan_distance
        if sensor.b_coord[0] > max_x:
            max_x = sensor.b_coord[0]
    sensors_in_range = list(filter(lambda x: is_sensor_in_y_range(x, y), sensors))
    beacons = [sensor.b_coord for sensor in sensors_in_range]
    coords = [
        (x_coord, y)
        for x_coord in range(min_x, max_x + 1)
        if (x_coord, y) not in beacons
    ]
    for coord in coords:
        for sensor in sensors_in_range:
            if sensor.coord_in_range(coord):
                count += 1
                break
    return count


def day2(sensors: t.List[t.Type["Sensor"]]) -> int:
    coords = [
        (x_coord, y_coord)
        for x_coord in range(0, 4_000_000 + 1)
        for y_coord in range(0, 4_000_000 + 1)
    ]
    for coord in coords:
        if not any([sensor.coord_in_range(coord) for sensor in sensors]):
            return 4_000_000 * coord[0] + coord[1]


def main():
    input = get_input("day15/input2.txt")
    parsed_input = parse_input(input)
    day1_result = day1(copy.deepcopy(parsed_input))
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
