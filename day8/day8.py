import typing as t


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


def parse_input(input_data: t.List[str]) -> t.List[t.List[int]]:
    data = [[int(j) for j in i] for i in input_data]
    return data


def day1(input_data: t.List[str]) -> int:
    empty_grid = [[0] * len(input_data[0])] * len(
        input_data
    )  # empty grid full of zeros
    visible_trees = set()
    # go in order left->right, top-> bottom, right->left, bottom->top
    tb_max = [0] * len(input_data)
    bt_max = [0] * len(input_data)
    for row, row_val in enumerate(input_data):
        lr_max = 0
        rl_max = 0
        for column, column_val in enumerate(row_val):
            # boundaries
            if (
                row == 0
                or column == 0
                or row == len(input_data) - 1
                or column == len(input_data[0]) - 1
            ):
                visible_trees.add((row, column))

            # lr
            if input_data[row][column] > lr_max:
                visible_trees.add((row, column))
                lr_max = input_data[row][column]
            # rl
            if input_data[row][-(column + 1)] > rl_max:
                visible_trees.add((row, len(input_data[row]) - (1 + column)))
                rl_max = input_data[row][-(column + 1)]
            if input_data[row][column] > tb_max[column]:
                visible_trees.add((row, column))
                tb_max[column] = input_data[row][column]
            if input_data[-(row + 1)][column] > bt_max[column]:
                visible_trees.add((len(input_data) - (1 + row), column))
                bt_max[column] = input_data[-(row + 1)][column]

    return len(visible_trees), visible_trees


def day2(input_data: t.List[str], trees: set[t.Tuple[int, int]]) -> int:
    empty_grid = [
        [0 for i in range(len(input_data[0]))] for j in range(len(input_data))
    ]
    for row, row_val in enumerate(input_data):
        for column, column_val in enumerate(row_val):
            if (
                row == 0
                or column == 0
                or row == len(input_data) - 1
                or column == len(input_data[0]) - 1
            ):
                continue
            else:
                empty_grid[row][column] = get_scenic((row, column), input_data, trees)
    return max([max(row) for row in empty_grid])


def get_scenic(starting_coord, input_data, trees):
    value = input_data[starting_coord[0]][starting_coord[1]]
    # need to keep track of the lst highest value and check whether the next value is the same or larger for it to count
    up = [0, 0, 0]  # (is_done, trees visible, last tallest tree)
    down = [0, 0, 0]
    left = [0, 0, 0]
    right = [0, 0, 0]
    # going left
    for i in range(1, starting_coord[1] + 1):
        if left[0] == 1:
            break
        current_tree = input_data[starting_coord[0]][starting_coord[1] - i]
        if current_tree >= value:
            left[0] = 1
        # elif current_tree < left[2]:
        #     continue  # value smaller than last tallest so ignored
        left[1] += 1
        left[2] = current_tree

    # going right
    for i in range(1, len(input_data[0]) - starting_coord[1]):
        if right[0] == 1:
            break
        current_tree = input_data[starting_coord[0]][starting_coord[1] + i]
        if current_tree >= value:
            right[0] = 1
        # elif current_tree < right[2]:
        #     continue
        right[1] += 1
        right[2] = current_tree

    # going down
    for i in range(1, len(input_data) - starting_coord[0]):
        if down[0] == 1:
            break
        current_tree = input_data[starting_coord[0] + i][starting_coord[1]]
        if current_tree >= value:
            down[0] = 1
        # elif current_tree < down[2]:
        #     continue
        down[1] += 1
        down[2] = current_tree

    # going up
    for i in range(1, starting_coord[0] + 1):
        if up[0] == 1:
            break
        current_tree = input_data[starting_coord[0] - i][starting_coord[1]]
        if current_tree >= value:
            up[0] = 1
        # elif current_tree < up[2]:
        #     continue
        up[1] += 1
        up[2] = current_tree

    return up[1] * down[1] * left[1] * right[1]


def main():
    input_data = get_input("day8/input.txt")
    parsed_data = parse_input(input_data)
    test = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]
    day1_result, trees = day1(parsed_data)
    day2_result = day2(parsed_data, trees)
    print(day1_result, day2_result)
    # 233376 is too low


if __name__ == "__main__":
    main()
