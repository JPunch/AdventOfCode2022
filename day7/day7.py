import typing as t


def get_input(filename: str) -> str:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


class Tree:
    def __init__(
        self, name: str, parent: t.Optional[t.Type["Tree"]] = None, is_dir: bool = False
    ):
        self.parent = parent
        self.name = name
        self.children = []
        self.is_dir = is_dir
        self.data: t.Optional[int] = None

    def __repr__(self) -> str:
        return f"{self.name}, parent: {self.parent.name}, data: {self.data}"

    def add_child(self, child):
        if isinstance(child, Tree):
            self.children.append(child)

    @staticmethod
    def get_tree(
        starting_tree: t.Type["Tree"], tree_name: str
    ) -> t.Optional[t.Type["Tree"]]:
        # might need to get by delimited slash str
        if tree_name == "..":
            return starting_tree.parent
        elif tree_name == "/":
            return starting_tree  # ignore first case
        for tree in starting_tree.children:
            if tree_name == tree.name:
                return tree

    def calculate_sizes(self) -> int:
        count = 0
        for tree in self.children:
            if not tree.is_dir:
                count += tree.data
            else:
                count += tree.calculate_sizes()
        self.data = count
        return count

    def sum_day1(self) -> int:
        count = 0
        for tree in self.children:
            if tree.is_dir and tree.data <= 100000:
                print(f"Adding data from dir {tree.name} with size {tree.data}")
                count += tree.data + tree.sum_day1()
            elif tree.is_dir:
                print(f"recursing into dir {tree.name} with size {tree.data}")
                count += tree.sum_day1()
        return count

    def day2(self, target_size: int) -> t.List[t.Type["Tree"]]:
        tree_list = []
        for tree in self.children:
            if tree.is_dir and tree.data >= target_size:
                tree_list.append(tree)
                tree_list.extend(tree.day2(target_size))
        return tree_list


def create_tree(lines: t.List[str]) -> t.Type["Tree"]:
    start = Tree("/", None, True)
    last_tree = start
    for line in lines:
        match line.split():
            case ["$", *args]:
                match args:
                    case ["cd", directory]:
                        print(directory)
                        if (tree := Tree.get_tree(last_tree, directory)) is not None:
                            last_tree = tree
                    case ["ls"]:
                        print("Listing directory")
                        # do nothing as it's handled in the pattern matching
            case ["dir", name]:
                print(f"Adding {name} to {last_tree.name}")
                last_tree.add_child(Tree(name, last_tree, True))
            case [size, name]:
                file = Tree(name, last_tree)
                file.data = int(size)
                last_tree.add_child(file)
    return start


def day1(tree: t.Type["Tree"]) -> int:
    tree.calculate_sizes()
    count = tree.sum_day1()
    return count


def day2(tree: t.Type["Tree"]) -> int:
    # sizes already calculated
    size = 70_000_000
    needed_space = 30_000_000
    free_space = needed_space - (size - tree.data)
    dirs = tree.day2(free_space)
    return min([tree.data for tree in dirs])


def main():
    input = get_input("day7/input.txt")
    tree_structure = create_tree(input)
    day1_result = day1(tree_structure)
    day2_result = day2(tree_structure)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
