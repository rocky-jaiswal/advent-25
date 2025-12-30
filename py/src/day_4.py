from utils import read_data_file


class Item:
    def __init__(self, x, y, neighbours, marker):
        self.x = x
        self.y = y
        self.neighbours = neighbours
        self.marker = marker

    def __str__(self):
        return f"Item: {self.marker} -> {self.x}, {self.y}"

    def __repr__(self):
        return f"Item: {self.marker} -> {self.x}, {self.y}"

    def mark_removed(self):
        self.marker = "x"
        return self


class Day4:
    def __init__(self):
        print("Hello from Day 4 ...")

    def get_neighbor_pos(self, x: int, y: int):
        return [
            (x - 1, y - 1),
            (x - 0, y - 1),
            (x + 1, y - 1),
            (x + 1, y + 0),
            (x + 1, y + 1),
            (x - 0, y + 1),
            (x - 1, y + 1),
            (x - 1, y - 0),
        ]

    def _build_grid(self, lines):
        all_items = {}

        for index_y, line in enumerate(lines):
            items = list(line)
            max_x = len(items)
            max_y = len(lines)
            for index_x, item in enumerate(items):
                neighbours = [
                    pos
                    for pos in self.get_neighbor_pos(index_x, index_y)
                    if 0 <= pos[0] < max_x and 0 <= pos[1] < max_y
                ]
                all_items[(index_x, index_y)] = Item(index_x, index_y, neighbours, item)

        return all_items

    def part_1(self):
        lines = read_data_file("day4_2.txt", "\n")

        all_items = self._build_grid(lines)

        pickable = []

        for key in all_items:
            c = 0
            item = all_items[key]
            for n in item.neighbours:
                ngbr = all_items.get(n)
                if ngbr.marker == "@":
                    c += 1
            if item.marker == "@" and c < 4:
                pickable.append(item)

        print(len(pickable))

    def part_2(self):
        lines = read_data_file("day4_2.txt", "\n")

        all_items = self._build_grid(lines)

        removed = 0
        more_left = True

        while more_left:
            # print(all_items)
            removable = []

            for key in all_items:
                c = 0
                item = all_items[key]
                for n in item.neighbours:
                    ngbr = all_items.get(n)
                    if ngbr.marker == "@":
                        c += 1
                if item.marker == "@" and c < 4:
                    removable.append(item)

            # print(removable)
            for item in removable:
                all_items[(item.x, item.y)] = item.mark_removed()
                removed += 1

            more_left = len(removable) != 0

        print(removed)


if __name__ == "__main__":
    Day4().part_1()
    Day4().part_2()
